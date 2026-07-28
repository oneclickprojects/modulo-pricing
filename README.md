# OneClick — Pricing Mobile (protótipo)

Protótipo navegável do módulo de pricing mobile do OneClick, em arquivo único
(`index.html`, sem build e sem dependências — basta abrir no navegador).

**Demo:** https://oneclickprojects.github.io/modulo-pricing/

---

## O que é

Ferramenta de simulação rápida para o originador em campo: lançar quantidade,
preço, logística e entregas, e ler a **margem estimada** em segundos — sem
depender do desktop. Depois de aprovada, a ordem segue para o OneClick standard,
que é o motor completo de cálculo.

Princípio que guia o layout, definido na daily de 24/07:

> "Isso tem que ser muito, muito, muito simples. Para o cara estar em um café com
> a contraparte, conseguir simular o P&L em segundos."

Tudo que não entra na árvore do P&L saiu da tela de simulação e foi para a etapa
de salvar / enviar.

---

## Versão atual — v3

Revisão dos pontos levantados na daily de 24/07 (Ronaldo, Thiago, Leonardo, Carlos).
O mapeamento completo dos 32 pontos está em [`DECISOES-DAILY-24-07.md`](./DECISOES-DAILY-24-07.md).

Principais mudanças em relação à v2:

| Área | Mudança |
|---|---|
| Topo | Margem estimada virou o único número grande, fixo na rolagem. Notional removido |
| Referências | Tela de algodão fixa deu lugar a Average Cotton Price e Average FX Price, ponderados pelas entregas |
| Boleta | Precificação acima; Quantidade e Preço lado a lado. Toggle Fixo/A Fixar removido |
| Logística | Logística e Entregas em linhas e blocos visualmente separados |
| Consolidado | Linha única com qtd total, cotação méd. ponderada, FX méd. ponderado e frete total |
| Fornecedor | Saiu da tela de simulação; virou texto livre no pop-up de salvar/enviar |
| Fluxo | Descartar · Salvar ordem · Enviar para aprovação (ou com hedge) |
| Simulações | Status "Simulação" em Operações, reabríveis para ajuste |
| Escopo do P&L | A margem exibida é sempre a da ordem em tela, nunca o total da carteira |

---

## Pendências conhecidas

- **Árvore da margem.** O cálculo aqui é um MTM simplificado. Falta mapear com o
  Carlos a árvore real do cálculo da margem do front office, que é o que define
  em definitivo quais campos ficam na tela de simulação.
- **Frete na margem.** Esta versão desconta frete/ton × quantidade do resultado.
  A v2 ignorava logística no cálculo. Precisa de validação.
- **Cenário-semente.** Os valores de exemplo (200 ton a 4,35 BRL/Lb) foram
  calibrados para dar uma margem plausível contra a curva mock. Conferir a ordem
  de grandeza real.
- **Simplificação da logística.** Ponto deixado explicitamente em aberto na daily.
- **Design.** Cores, espaçamento e refinamento visual ficam com a Rebeca. Esta
  versão trata de informação e fluxo, não de acabamento.

---

## Estrutura

```
index.html                 protótipo completo (HTML + CSS + JS em arquivo único)
DECISOES-DAILY-24-07.md    mapeamento dos 32 pontos da transcrição
```

Dados de mercado são mock, embutidos em `MARKET_CURVES` no próprio arquivo.
Nenhuma chamada de rede, nenhum dado real de cliente.
