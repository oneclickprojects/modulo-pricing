#!/usr/bin/env python3
"""
Monta o histórico de versões a partir de historico/ e injeta dentro do
index.html, como um selo no canto que abre um painel.

Autor, data e número da versão vêm do git — nunca do conteúdo do arquivo.
Rodado pelo workflow no momento da publicação; não precisa rodar na mão.

Uso: python3 .github/scripts/injetar_historico.py
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

PASTA = Path("historico")
# Qual arquivo recebe a injeção. O workflow aponta para a cópia na raiz.
ALVO = Path(os.environ.get("ALVO_HTML", "index.html"))
ABRE = "<!-- historico-de-versoes -->"
FECHA = "<!-- /historico-de-versoes -->"

# O protótipo já vinha versionado à mão até a v8, então a contagem continua
# de onde ela parou: a primeira entrada registrada é a v9.
BASE = int(os.environ.get("VERSAO_BASE", "8"))

MESES = ["jan", "fev", "mar", "abr", "mai", "jun",
         "jul", "ago", "set", "out", "nov", "dez"]


def git(*args):
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def bullets(caminho):
    """Extrai os bullets do arquivo. Tolera texto solto e linhas em branco."""
    itens = []
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#"):
            continue
        itens.append(re.sub(r"^[-*+]\s*", "", linha))
    return itens[:4]


def entradas():
    """Uma entrada por arquivo em historico/, ordenada por data do commit."""
    achadas = []
    for caminho in sorted(PASTA.glob("*.md")):
        # Primeiro commit que adicionou este arquivo.
        info = git("log", "--diff-filter=A", "--format=%an%x1f%aI%x1f%h",
                   "-1", "--", str(caminho))
        if info:
            autor, iso, sha = info.split("\x1f")
        else:
            # Arquivo ainda não commitado (rodando local): usa o estado atual.
            autor, iso, sha = "não publicado", "", "-"
        achadas.append({"autor": autor, "iso": iso, "sha": sha,
                        "itens": bullets(caminho), "arquivo": caminho.name})

    # Empate de segundo no commit é possível: o nome do arquivo (que começa
    # com a data) desempata de forma estável.
    achadas.sort(key=lambda e: (e["iso"] or "9999", e["arquivo"]))
    for i, e in enumerate(achadas, start=1):
        e["versao"] = BASE + i
        e["data"] = ""
        e["hora"] = ""
        if len(e["iso"]) >= 10:
            e["data"] = f"{e['iso'][8:10]} {MESES[int(e['iso'][5:7]) - 1]}"
        if len(e["iso"]) >= 16:
            e["hora"] = e["iso"][11:16]
    achadas.reverse()  # mais recente primeiro
    return achadas


# Sem quebra de linha antes do marcador: a remoção consome exatamente
# ABRE..FECHA mais um \n, então injetar e remover é reversível byte a byte.
# Com uma quebra sobrando aqui, cada publicação deixaria uma linha em branco nova.
TEMPLATE = """<!-- historico-de-versoes -->
<style>
#hv-selo{position:fixed;right:10px;bottom:calc(70px + env(safe-area-inset-bottom));z-index:2147483646;
font:11px/1.35 system-ui,-apple-system,"Segoe UI",sans-serif;font-weight:500;
padding:6px 11px;border-radius:999px;border:1px solid rgba(255,255,255,.22);
background:rgba(18,22,28,.86);color:#e6edf3;-webkit-backdrop-filter:blur(6px);
backdrop-filter:blur(6px);cursor:pointer;display:flex;align-items:center;gap:6px;
box-shadow:0 2px 10px rgba(0,0,0,.35)}
#hv-selo .hv-pt{width:5px;height:5px;border-radius:50%;background:#35b060;
flex:0 0 auto}
#hv-painel{position:fixed;inset:0;z-index:2147483647;display:none;
background:rgba(8,10,14,.94);-webkit-backdrop-filter:blur(6px);
backdrop-filter:blur(6px);overflow-y:auto;-webkit-overflow-scrolling:touch;
font:14px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;color:#e6edf3;
text-align:left}
#hv-painel.open{display:block}
#hv-painel .hv-topo{position:sticky;top:0;display:flex;align-items:center;
justify-content:space-between;gap:12px;padding:14px 16px;
background:rgba(8,10,14,.96);border-bottom:1px solid #232a33}
#hv-painel h2{margin:0;font-size:15px;font-weight:600;color:#fff}
#hv-fechar{border:0;background:#232a33;color:#e6edf3;font-size:13px;
padding:6px 12px;border-radius:6px;cursor:pointer}
#hv-painel ol{list-style:none;margin:0;padding:10px 16px 40px}
#hv-painel li{padding:13px 0;border-bottom:1px solid #1c222b}
#hv-painel li:last-child{border-bottom:0}
#hv-painel .hv-cab{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap;
margin-bottom:5px}
#hv-painel .hv-v{font-size:11px;font-weight:600;color:#7ee2a8;
border:1px solid #2f6f4f;border-radius:999px;padding:1px 7px}
#hv-painel li.hv-atual .hv-v{background:#173a28}
#hv-painel .hv-quem{font-weight:500;color:#fff}
#hv-painel .hv-quando{color:#8b949e;font-size:12px}
#hv-painel .hv-itens{margin:0;padding-left:16px;color:#c7d0da}
#hv-painel .hv-itens li{padding:1px 0;border:0;list-style:disc}
#hv-painel .hv-vazio{color:#8b949e;font-style:italic}
#hv-painel .hv-rodape{padding:0 16px 40px;color:#6e7681;font-size:11.5px}
</style>
<div id="hv-painel" role="dialog" aria-modal="true" aria-label="Histórico de versões">
  <div class="hv-topo">
    <h2>Histórico de versões</h2>
    <button id="hv-fechar" type="button">fechar</button>
  </div>
  <ol id="hv-lista"></ol>
  <p class="hv-rodape">Cada versão corresponde a uma publicação. Autor e data vêm
  do commit. Para voltar a uma versão anterior, use o código ao lado da data em
  Actions &rsaquo; Publicar prototipo &rsaquo; Run workflow.</p>
</div>
<script>
(function(){
  var dados = __DADOS__;
  var painel = document.getElementById('hv-painel');
  var lista = document.getElementById('hv-lista');
  function esc(s){ return String(s).replace(/[&<>"]/g, function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
  dados.forEach(function(e, i){
    var li = document.createElement('li');
    if (i === 0) li.className = 'hv-atual';
    var itens = e.itens.length
      ? '<ul class="hv-itens">' + e.itens.map(function(t){
          return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>'
      : '<p class="hv-vazio">sem descrição</p>';
    li.innerHTML =
      '<div class="hv-cab">' +
        '<span class="hv-v">v' + e.versao + '</span>' +
        '<span class="hv-quem">' + esc(e.autor) + '</span>' +
        '<span class="hv-quando">' + esc(e.data) + (e.hora ? ' &middot; ' + esc(e.hora) : '') + ' &middot; ' + esc(e.sha) + '</span>' +
      '</div>' + itens;
    lista.appendChild(li);
  });
  // Abre/fecha reaproveitando o mesmo mecanismo dos outros modais do
  // prototipo (openSheet/closeSheet, definidos no script principal) — assim
  // o botao/gesto voltar do Android fecha este painel igual aos demais, sem
  // duplicar logica de historico do navegador aqui. Fallback simples caso
  // essas funcoes nao existam (outra versao do prototipo, por exemplo).
  function abrir(){
    if (typeof window.openSheet === 'function') window.openSheet('hv-painel');
    else painel.classList.add('open');
  }
  function fechar(){
    if (typeof window.closeSheet === 'function') window.closeSheet('hv-painel');
    else painel.classList.remove('open');
  }

  // Ponto de entrada: selo flutuante sempre visível na tela (não depende de
  // abrir a Toolbox). Mostra a versão atual; toca para ver o histórico.
  function montarSelo(){
    if (document.getElementById('hv-selo')) return;
    var selo = document.createElement('button');
    selo.id = 'hv-selo';
    selo.type = 'button';
    selo.setAttribute('aria-haspopup', 'dialog');
    selo.setAttribute('aria-label', 'Ver histórico de versões');
    selo.innerHTML = '<span class="hv-pt"></span><span>v__VERSAO__ &middot; histórico</span>';
    selo.addEventListener('click', abrir);
    document.body.appendChild(selo);
  }

  montarSelo();

  document.getElementById('hv-fechar').addEventListener('click', fechar);
  painel.addEventListener('click', function(ev){ if (ev.target === painel) fechar(); });
  document.addEventListener('keydown', function(ev){
    if (ev.key === 'Escape') fechar(); });
})();
</script>
<!-- /historico-de-versoes -->
"""


def main():
    if not ALVO.exists():
        print("index.html não encontrado", file=sys.stderr)
        return 1

    dados = entradas() if PASTA.is_dir() else []
    versao = dados[0]["versao"] if dados else BASE

    bloco = (TEMPLATE
             .replace("__DADOS__", json.dumps(dados, ensure_ascii=False))
             .replace("__VERSAO__", str(versao)))

    src = ALVO.read_text(encoding="utf-8")

    # Idempotente: remove só o bloco entre os marcadores, preservando o que vem
    # depois (</body></html>). Sem os dois marcadores isso comeria o fim do
    # arquivo a cada publicação.
    # O \n? final casa a quebra que o próprio bloco traz, para não sobrar linha
    # em branco acumulando a cada publicação.
    if ABRE in src:
        src = re.sub(re.escape(ABRE) + r".*?" + re.escape(FECHA) + r"\n?",
                     "", src, flags=re.S)

    pos = src.lower().rfind("</body>")
    src = (src[:pos] + bloco + src[pos:]) if pos != -1 else src + bloco

    ALVO.write_text(src, encoding="utf-8")

    resumo = f"v{versao} · {len(dados)} entradas no histórico"
    print(resumo)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as f:
            f.write(f"versao={versao}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
