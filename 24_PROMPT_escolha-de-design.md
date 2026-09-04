# 24 · PROMPT — Gerar formas de design para o Odin escolher (funil 8 → 4 → 3)

> Use quando quiser ver e escolher visuais. A rodada 1 já existe (galeria 11, artefato "Temas do HyHoney", rota `/temas`). Este prompt roda as rodadas 2 e 3 e também serve para gerar uma **nova** rodada 1 se nenhum dos 8 agradar.

---

## PROMPT

Você é o designer do **HyHoney** (leia a skill `hyhoney-design` e o painel). Conduza a escolha de design do app em três rodadas, sempre mostrando, nunca descrevendo:

**Rodada 1 — 8 direções** (`NN_TEMAS_galeria.html`): a mesma tela (a Capa) em 8 mini-iPhones, cada um com nome, paleta de 5 cores, par tipográfico e "para quem é". Direções obrigatórias: 2 claras quentes, 2 escuras, 1 minimalista branca, 1 editorial (serifa), 1 lúdica (pastel), 1 "especial" ligada ao humor do Cartório. Se o Odin disser "nenhum", gerar 8 novas partindo do feedback dele (o que gostou/odiou em cada).

**Rodada 2 — 4 finalistas aplicados de verdade**: cada finalista vira uma "pele" (`data-skin`) no mockup real; página `NN_TEMAS_finalistas.html` mostra o app completo 4× lado a lado (iPhone), com um botão para trocar a seção exibida nos 4 ao mesmo tempo (Capa, Protocolos, Roleta, Termômetro). AskUserQuestion: uma pergunta por vez — "qual sai?" até sobrarem 3.

**Rodada 3 — 3 temas alternáveis**: um claro (padrão do app), um escuro (contemplação noturna), um especial (seções do Cartório ou escolha do casal). Remover os outros do mockup; registrar D-n no painel com nome e tokens de cada tema; republicar mockup e preview; arquivar versão no histórico.

Regras: tokens completos para claro e escuro em cada tema; contraste ≥ 4,5:1; o visual é sério e o texto é engraçado; cada tema tem "para quem é" em uma frase. No fim, atualizar o painel (pergunta "tema" → decisão), o registro (21) e o índice (00).
