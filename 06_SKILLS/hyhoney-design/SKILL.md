---
name: hyhoney-design
description: Dar ao HyHoney um design profissional de app de celular (referências TickTick, Things, Notion, Apple Reminders, Duolingo) e gerar opções de tema para o Odin escolher até restarem 3 temas alternáveis. Use em "melhora o design do HyHoney", "gera temas", "quero escolher o visual", "deixa com cara de app profissional".
---

# hyhoney-design

Objetivo: o mockup e o app final devem parecer feitos por um estúdio, não gerados. Foco em iPhone; iPad e desktop derivam do mobile.

## Referências (o que copiar de cada uma, sem copiar marca)
- **TickTick**: organização — atalhos, pastas, listas, gaveta, barra inferior, painel de detalhe; contadores nas listas.
- **Things 3**: espaço em branco generoso, tipografia grande nos títulos, animações curtas ao concluir.
- **Apple Reminders / iOS**: sheets que sobem de baixo, cabeçalhos grandes que encolhem ao rolar, safe areas, toques de 44px.
- **Duolingo**: gamificação com cor e forma (raridades, streaks, selos), sem infantilizar.
- **Notion**: emoji como ícone de seção, blocos editáveis, sensação de "é meu".

## Base em neurociência e psicologia do uso (por que cada regra existe)
Cada escolha de design deve citar, em uma frase, o princípio que a sustenta. Os que valem para o HyHoney:
- **Lei de Fitts** (alvos grandes e próximos do polegar): ações principais na metade inferior da tela, 44–56px; barra inferior, não menu no topo.
- **Lei de Hick** (menos opções = decisão mais rápida): 4 atalhos + "Mais"; um botão primário por tela; o resto atrás do ⋯.
- **Chunking / 7±2** (memória de trabalho): listas agrupadas em pastas de até 6 itens; números grandes isolados (o countdown) com um só rótulo.
- **Efeito von Restorff** (o diferente é lembrado): uma só coisa "brilha" por tela — o cupom Lendário, a memória do dia.
- **Regra do pico-fim** (lembramos do melhor momento e do final): ao concluir algo, uma micro-celebração curta; ao fechar o app, a "memória surpresa" como última imagem.
- **Recompensa variável** (dopamina por surpresa, não por repetição): memória surpresa aleatória, protocolos raros, títulos automáticos do mês. Nunca notificação vazia.
- **Efeito Zeigarnik** (tarefas incompletas ficam na cabeça): barras de progresso visíveis (série 75%, meta 35%) puxam de volta — usar com moderação nas seções "chatas", nunca no Museu.
- **Fluência de processamento** (o fácil de ler parece verdadeiro e bonito): contraste ≥ 4,5:1, uma família para títulos e uma para corpo, espaçamento generoso, alinhamento à esquerda.
- **Efeito de posse (endowment)**: o que o casal personaliza (nome, emoji, ordem) vira "nosso" — por isso tudo é renomeável e arrastável.
- **Carga cognitiva e divulgação progressiva**: detalhe só ao tocar (folha que sobe); a tela inicial mostra 3 blocos, não 12.
- **Cor e emoção**: quentes (mel, rosa) para memória e afeto; frios (azul, verde) para organização; vermelho reservado para "atenção" real. Escuro para contemplação noturna, claro para uso diurno — por isso 3 temas alternáveis.
- **Consistência e affordance**: o que parece botão é botão; o que arrasta mostra alça; mesmo gesto = mesmo resultado em todas as seções.

## Regras de design (aplicar sempre)
1. Toque mínimo 44×44; texto corrido 15–17px no iPhone; títulos com serifa suave (Fraunces) e corpo humanista (Nunito) — ou o par do tema escolhido, sempre do Google Fonts com fallback.
2. Sistema de tokens: `--bg --surface --surface2 --line --ink --ink2 --muted --accent --accent-soft --rose --sage --sky --r --shadow`. Nenhuma cor solta fora dos tokens. Modo claro e escuro para cada tema.
3. Hierarquia: uma coisa grande por tela (o countdown, o cupom, a foto), o resto quieto. Cards só onde separam objetos de verdade; listas usam divisórias, não cards.
4. Estados visíveis: feito, rascunho privado (🙈), admin (👑), PIN (🔐), raridade por cor de borda. Semântica (bom/atenção/crítico) separada do accent.
5. Micro-interações com propósito: cupom "rasga" ao usar; concluir tarefa faz "tick" curto; countdown anima só na abertura. `prefers-reduced-motion` respeitado.
6. Humor mora no conteúdo (nomes, carimbos, legendas), não em cores gritantes. O visual é sério; o texto é engraçado.
7. Cada seção pode ter uma "pele" própria (ex.: Viagens em Passaporte) — mas o app tem um tema base.

## Processo de escolha de temas (funil)
1. **Rodada 1 — 8 opções**: gerar/atualizar `NN_TEMAS_galeria.html` com 8 temas, cada um num mini-iPhone mostrando a mesma tela (Capa) e a mesma lista; nome, paleta (5 cores), par tipográfico, "para quem é". O Odin marca favoritos no próprio arquivo (localStorage) e cola a escolha no chat.
2. **Rodada 2 — 4 finalistas**: aplicar cada finalista ao mockup real (`data-skin`), republicar, e mostrar em `10_PREVIEW_dispositivos` lado a lado. Pedir uma escolha por vez com AskUserQuestion.
3. **Rodada 3 — 3 temas finais**: fixar 3 temas alternáveis (um claro padrão, um escuro, um "especial"); remover os outros do mockup; registrar D-n no painel com os nomes e tokens. A partir daí, temas novos só substituem um dos 3.

## Entregáveis de cada rodada
- Galeria/preview republicada (mesmo artefato quando existir).
- Painel atualizado: pergunta aberta "tema" → decisão quando fechar.
- Uma tabela curta no chat: tema · vibe em 5 palavras · quando usar.
