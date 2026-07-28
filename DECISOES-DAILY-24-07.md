# Pontos de melhoria do protótipo mobile (OneClick Pricing)

**Fonte:** Daily OneClick — Alinhamento Diário, 24/07/2026 (1h28)
**Protótipo:** `oneclick-prototipo-v2.html`
**Participantes:** Ronaldo Bhering, Thiago Rodrigues, Leonardo Velani, Carlos Inácio

---

## Princípio norteador (Ronaldo)

Toda a revisão do protótipo gira em torno de uma regra: **o trader só quer saber se o negócio dá dinheiro ou não.**

> "Isso tem que ser muito, muito, muito simples. Para o cara estar em um café com a contraparte, conseguir simular o P&L em segundos — sem que a contraparte veja que ele está digitando."

Método sugerido para decidir o que entra na tela: **montar a "árvore do P&L"** — mapear o cálculo da margem do front office (com o Carlos) e manter na tela de simulação **apenas os campos que impactam esse cálculo**. Todo o resto vai para uma segunda etapa.

> "Nome do fornecedor é importante pra caramba, mas não para o cálculo do canal [P&L]."

Ronaldo também reforçou que quer usar o protótipo como **peça de apresentação/venda do sistema** — alguém que nunca fez trade deve conseguir abrir e simular um negócio. O nome é "OneClick", então tem que ser mais simples que qualquer outro sistema.

---

## 1. Barra de resumo do topo (Notional / P&L / Exposure FX)

| # | Ponto | Quem | Ação |
|---|---|---|---|
| 1.1 | **Remover o card "Notional" (R$ e US$)** do topo. O valor monetário já aparece embaixo do campo Quantidade — não precisa duplicar. | Ronaldo | Remover `prev-notional-brl` / `prev-notional-usd` |
| 1.2 | **Remover "Notional em Reais"** especificamente — "informação que o cara não vai usar para nada". Manter no máximo exposure em dólar. | Ronaldo | — |
| 1.3 | **Elogio / manter:** mostrar o valor aproximado da operação logo abaixo da quantidade (`≈ R$ 88,2M · US$ 15,7M`) foi aprovado. | Ronaldo | Manter |
| 1.4 | **Subir a Margem / P&L para o topo, como driver principal.** Hoje no front office a margem fica lá embaixo; no protótipo ela precisa estar em destaque e **fixa/sticky**, acompanhando a rolagem da tela. | Ronaldo / Leonardo | Reforçar `summaryBar` |
| 1.5 | **Deixar no topo apenas informação prioritária** (margem/P&L), removendo o resto. | Leonardo | — |

---

## 2. Bloco de cotação do algodão (topo)

| # | Ponto | Quem | Ação |
|---|---|---|---|
| 2.1 | "Tem muito preço de algodão aí em cima" — bloco está pesado demais. | Ronaldo | Reduzir |
| 2.2 | **Não deve haver uma "tela de algodão de referência" única.** Em vez disso, exibir **Average Cotton Price** e **Average FX Price**, ponderados pela distribuição das entregas. | Ronaldo | Substituir tela fixa por média ponderada |
| 2.3 | Exibir isso em **fonte/área pequena** — é referência, não protagonista. | Ronaldo | — |
| 2.4 | **Manter:** a variação do dia (alta/baixa/%) foi bem recebida. | Thiago | Manter |

---

## 3. Os 2 quadrados de "telas" (mini-cards) da tela de negociação

| # | Ponto | Quem | Ação |
|---|---|---|---|
| 3.1 | **Remover os 2 quadrados** da tela de negociação/boleto — "não tá legal não", estavam "voando" sem contexto. | Thiago | Remover |
| 3.2 | Contexto: eram as telas de bolsa das entregas. Ronaldo reforçou que **não faz sentido listar todas as telas** — contrato da Stonex chega a ter 10 entregas com 4-5 telas diferentes. O que importa é a **commodity média ponderada** usada como referência de marcação do P&L. | Ronaldo | Substituir por média ponderada |
| 3.3 | Ressalva do Thiago: os quadradinhos fazem sentido quando há várias entregas com prazos diferentes (visão de "plantio"), mas devem ser consolidados. | Thiago | Avaliar |

---

## 4. Campos de entrada da simulação (Quantidade / Preço / Precificação)

| # | Ponto | Quem | Ação |
|---|---|---|---|
| 4.1 | **Elogio:** o bloco quantidade / preço / precificação / tipo ficou simples e agradou. | Thiago | Manter |
| 4.2 | **Reorganizar em linha:** colocar **Quantidade e Preço lado a lado**, com **Precificação acima** deles (ou os dois embaixo do rótulo), formando uma linha só. | Thiago | Reagrupar layout |
| 4.3 | **Remover o toggle "Fixo / A Fixar"** — a modalidade já indica isso, e se o dólar não for fixado ele fica fixado por padrão. É automático. | Ronaldo + Thiago | Remover |
| 4.4 | Preço e precificação podem ser trazidos "para a frente" (mesma linha do lançamento). | Thiago | — |

---

## 5. Fornecedor e campos não relacionados ao P&L

| # | Ponto | Quem | Ação |
|---|---|---|---|
| 5.1 | **Tirar o campo Fornecedor da tela principal de simulação.** Ele não impacta o cálculo do P&L. | Ronaldo | Mover para etapa 2 |
| 5.2 | **Fornecedor deve ser campo livre de texto** — o originador digita qualquer coisa e o backoffice ajusta depois. | Thiago | Alterar tipo de campo |
| 5.3 | **Qualidade, Safra e Mercado**: divergência a resolver. Leonardo argumenta que impactam o P&L; Thiago propõe subir junto com o fornecedor para o pop-up de envio. → **Definir via árvore do P&L.** | Leonardo × Thiago | ⚠️ Pendente de decisão |
| 5.4 | Esses campos reaparecem em um **pop-up** no momento de salvar a ordem ou enviar para aprovação. | Leonardo / Thiago | Criar modal |

---

## 6. Fluxo: Simular → Salvar → Enviar para aprovação

| # | Ponto | Quem | Ação |
|---|---|---|---|
| 6.1 | Adicionar **botão de simulação** na tela de negociação; não obrigar o envio. | Thiago | Novo botão |
| 6.2 | Após preencher: oferecer **"Save Order" ou "Descartar"**. | Thiago | Duas ações |
| 6.3 | Simulações salvas caem na aba **Operação** com status **"Simulação"**. O usuário pode simular quantas quiser. | Thiago | Novo status |
| 6.4 | **Ao clicar em uma simulação salva, a tela reabre para edição/ajuste.** | Thiago | Reabrir em modo edição |
| 6.5 | Só ao **enviar para aprovação** abre o pop-up pedindo cliente/fornecedor, qualidade, safra, mercado — o que o sistema precisa. | Thiago / Leonardo | Modal de complemento |
| 6.6 | Espelhar a lógica de botões do front office atual: **Save the Order / Book the Trade / Book the Trade and Hedge** (equivalente a Salvar / Confirmar / Confirmar com Hedge). | Ronaldo | Renomear ações |
| 6.7 | Premissa: o trader **simula muito mais do que fecha** — de 10 ofertas, fecha ~3. O fluxo tem que ser otimizado para simulação descartável. | Ronaldo | Princípio |

---

## 7. Bloco de Logística e Entregas

| # | Ponto | Quem | Ação |
|---|---|---|---|
| 7.1 | **Está confuso** — não dá para saber onde começa o frete, onde começa a rota e onde termina. | Thiago | Reestruturar |
| 7.2 | **Separar visualmente em duas linhas distintas: uma linha "Logística" e uma linha "Entregas"** (ou diferenciar por cor). | Thiago | Separar blocos |
| 7.3 | **Elogio:** o bloco de logística/rota, isoladamente, ficou bom e simples. Usar como modelo para o de entregas. | Thiago | Manter padrão |
| 7.4 | **Entregas devem ser resumidas:** apenas quantidade e data de entrega final, datas bem reduzidas. | Thiago / Leonardo | Simplificar |
| 7.5 | **Adicionar uma linha-resumo de média ponderada** ao fechar o modal de entregas: cotação média ponderada + FX médio ponderado (espelhando a última linha do front office atual). Independente de quantas entregas forem incluídas, o trader bate o olho em uma linha só e vê o P&L. | Thiago / Ronaldo | Nova linha consolidada |
| 7.6 | Referência técnica: no front office, a margem em dólar (ex.: 305) é calculada com a **cotação média ponderada (70,6)** e o **FX médio ponderado (6,42)** — calcular individualmente ou pela ponderada dá o mesmo resultado. | Ronaldo | Replicar lógica |
| 7.7 | Ronaldo pediu explicitamente ajuda para **simplificar a parte de logística** — ponto ainda em aberto. | Ronaldo | ⚠️ Em aberto |
| 7.8 | Observação: os blocos recolhem/expandem — Thiago não tinha percebido. Está OK, mas indica que a **affordance de recolher não está clara**. | Thiago | Melhorar affordance |

---

## 8. Aba Operação / Carteira

| # | Ponto | Quem | Ação |
|---|---|---|---|
| 8.1 | **Elogio:** o resumo da carteira + contratos enviados com status (aprovado / em análise) está bom. | Thiago | Manter |
| 8.2 | Na aba Operação, **exibir o P&L e as informações financeiras da ordem específica**, e não o total da carteira. | Thiago | Corrigir escopo |
| 8.3 | Na Operação **pode aparecer tudo** (informação completa), **exceto as telas de entrega**. | Thiago | Ajustar |
| 8.4 | Na simulação, o P&L exibido deve ser **o do contrato que está na tela**, não o total da carteira. | Thiago / Ronaldo | ⚠️ Correção crítica |

---

## 9. Aba Mercados

| # | Ponto | Quem | Ação |
|---|---|---|---|
| 9.1 | **Elogio / manter:** "isso aqui é legal, se o cara quiser sair navegando, ver a curva". | Thiago | Manter |

---

## 10. Visual e identidade

| # | Ponto | Quem | Ação |
|---|---|---|---|
| 10.1 | **Manter o tema escuro (visão homebroker)** — aprovado por Thiago e Carlos; é o padrão que traders esperam. | Thiago / Carlos | Manter |
| 10.2 | Sugestão: levar o dark mode também para o **OneClick web (compra e venda)**, via botão de sol/lua alternando o fundo. | Carlos | Backlog desktop |
| 10.3 | Refinamento visual (cores, organização, "deixar bonito") será feito pela **Rebeca**, não agora. O foco atual é **informação e fluxo**. | Thiago / Ronaldo | Fase 2 |
| 10.4 | Feedback geral do Ronaldo: **"ainda está muito confuso"** — a densidade de informação é o problema principal. | Ronaldo | Princípio |

---

## Ação técnica pré-requisito

**Leonardo + Carlos: mapear a árvore do cálculo da margem** no front office atual.

> "Foca nesse cálculo da margem e vê exatamente a árvore dela. Isso vai te dar uma visão crítica do que é necessário de input para o cálculo do resultado."

Esse mapa define, de forma objetiva, quais campos ficam na tela de simulação e quais vão para o pop-up de envio — resolvendo inclusive o item 5.3.

---

## Resumo por prioridade

**Alta — impacta o objetivo central (P&L em segundos)**

- Subir e fixar a Margem/P&L no topo (1.4)
- P&L da ordem, não da carteira (8.4)
- Remover Notional duplicado e em reais (1.1, 1.2)
- Tirar Fornecedor da tela de simulação (5.1)
- Separar Logística × Entregas (7.2)
- Linha-resumo de média ponderada nas entregas (7.5)
- Mapear a árvore da margem (pré-requisito)

**Média — simplificação de layout**

- Remover os 2 quadrados de telas (3.1)
- Substituir tela de referência por Average Cotton/FX Price (2.2)
- Reagrupar Quantidade + Preço + Precificação em linha (4.2)
- Remover toggle Fixo/A Fixar (4.3)
- Reduzir bloco de cotação do algodão (2.1)

**Fluxo**

- Botão Simular + Save Order / Descartar (6.1, 6.2)
- Status "Simulação" e reabertura para edição (6.3, 6.4)
- Pop-up de dados complementares no envio (6.5)
- Nomenclatura Save the Order / Book the Trade / Book and Hedge (6.6)

**Backlog**

- Fornecedor como texto livre (5.2)
- Dark mode no OneClick web (10.2)
- Refinamento visual com a Rebeca (10.3)
