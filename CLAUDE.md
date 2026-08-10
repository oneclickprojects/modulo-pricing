# Regras deste repositório

Protótipo navegável do módulo de pricing mobile do OneClick. Arquivo único
(`v8/index.html`), sem build. Editado em paralelo por três pessoas: Leonardo,
Ronaldo e Thiago, cada um em sua própria branch.

**A versão viva é `v8/index.html`.** É o único arquivo de protótipo a editar.
O workflow publica essa pasta na raiz do site.

Não crie pastas `v9`, `v10` e afins. Versão agora é commit: cada alteração
registrada em `historico/` vira uma versão numerada, visível no painel dentro do
próprio protótipo. As pastas `v4` a `v7` são arquivo morto — não mexa nelas.

## Obrigatório em toda alteração do v8/index.html

Crie um arquivo **novo** em `historico/`:

    historico/AAAA-MM-DD-descricao-curta.md

Conteúdo: de 1 a 3 bullets em português, dizendo o que mudou para quem **usa** o
protótipo — não para quem lê o código.

Exemplo (`historico/2026-08-11-margem-fixa.md`):

```markdown
- Margem estimada agora fica fixa no topo ao rolar a tela
- Notional saiu do cabeçalho
```

Não escreva seu nome, a data nem o número da versão. Os três são preenchidos
automaticamente na publicação, a partir do commit.

Nunca edite um arquivo que já existe em `historico/`. Sempre crie um novo — é
isso que evita conflito entre as três branches.

**O deploy falha se o `v8/index.html` mudar sem uma entrada nova em `historico/`.**

## Escopo das alterações

Não reescreva o `v8/index.html` inteiro. Altere apenas os trechos necessários.

Outras duas pessoas estão editando o mesmo arquivo em paralelo. Uma reescrita
completa gera um diff ilegível e um conflito que não dá para resolver — mesmo que
o resultado final pareça correto isoladamente.

Se uma mudança exigir mexer em muitos pontos do arquivo, faça em etapas e
registre cada uma no histórico.

## Não altere sem pedido explícito

- O bloco de logos em base64 (são geradas a partir do arquivo oficial da marca)
- `MARKET_CURVES` (dados mock calibrados de propósito)
- O selo de versão e o painel de histórico injetados no rodapé pelo workflow

## Contexto de produto

A margem estimada é o único número grande da tela. Tudo que não entra na árvore
do P&L fica fora da tela de simulação. O princípio, definido na daily de 24/07:
simular o P&L em segundos, no celular, durante uma conversa.

Antes de adicionar qualquer campo à tela de simulação, considere se ele não
deveria ficar na etapa de salvar/enviar.
