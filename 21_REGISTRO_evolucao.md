# 21 · REGISTRO DE EVOLUÇÃO — HyHoney

> Diário de bordo do projeto, mais recente no topo. Uma entrada por rodada. Serve para acompanhar, voltar atrás e achar qualquer documento. Vai virar o `CHANGELOG.md` do repositório quando o código começar.

## Documentos por importância (abra nesta ordem)
| # | Documento | Por quê |
|---|---|---|
| 1 | `04_PAINEL_estado-do-projeto` (.md / .html) | estado, decisões, prompts, checklist — a verdade |
| 2 | `05_CLAUDE_texto-para-colar-no-projeto.md` | regras de trabalho de toda sessão |
| 3 | `07_PROMPT_proximo-passo-P5.md` | o que vem agora (🟡 rodando) |
| 4 | `03_MOCKUP_hyhoney-app.html` | o app, como está |
| 5 | `19_ANALISE_v2-replanejamento` (.pdf) | o que focar, esconder, otimizar; roadmap v2 |
| 6 | `02_PLANO_analise-arquitetura-sugestoes.md` | a arquitetura de referência |
| 7 | `21_REGISTRO_evolucao.md` | este diário |
| 8 | `00_INDICE.md` · `16` · `17` · `08` · `11` · `14` · skills | o resto, quando precisar |

## Linha do tempo de versões do mockup
| Versão | Data | O que entrou | Arquivo no histórico | Commit |
|---|---|---|---|---|
| v0 | 2026-09-04 | desktop, 22 seções, personalização, 5 temas | *(não arquivada)* | — |
| v0.1 | 2026-09-04 | mobile estilo TickTick (gaveta, barra inferior, folha) | `2026-09-04_v0.1_mobile-ticktick.html` | a6b79a7 |
| v0.2 | 2026-09-04 | passe de design (alvos 44px, escala, um botão primário) | *(não arquivada; só CSS, contido na v0.3)* | a6b79a7 |
| v0.3 | 2026-09-04 | + A Roleta (o que fazer hoje, deliverys, templates, IA) | `2026-09-04_v0.3_roleta.html` | a6b79a7 |
| v0.4 | 2026-09-04 | + Clima do Dia, busca geral ⌘K, merge de seções novas | `2026-09-04_v0.4_clima-busca.html` | a6b79a7 |

---

## 2026-09-04 · sessão 1 · rodada única — do briefing ao kit completo · commit `a6b79a7`

**Criado.** 00 índice (Obsidian) · 01 briefing · 02 plano · 03 mockup v0→v0.4 · 04 painel (.md + .html, com checklist das suas ideias, links e índice de arquivos) · 05 CLAUDE.md · 06 quatro skills (sessao, nova-secao, atualizar-painel + ponte Code, design) · 07 prompt P5 · 08 análise 1 (PDF) · 09 servidor local · 10 preview em 3 aparelhos · 11 galeria de 8 temas · 12 prompt design+neuro (executado) · 13 instalador do servidor no login · 14 guia Dock/iPhone/IP fixo · 15 git sync · 16 prompt Clima do Dia · 17 prompt anexos/tags/busca · 18 prompt análise v2 (executado) · 19 análise v2 + roadmap (PDF) · 20 prompt deste registro · 21 este registro · `historico-mockups/` · `icones/` · `logs/` · `.gitignore`.

**Decisões.** D1 layout TickTick · D2 cartão único · D3 quatro pastas · D4 hyhoney.bitbeagle.com, uma casa por casal · D5 edição simétrica "o outro vê?" · D6 Cofre oculto, Placar com PIN · D7 IA só propõe · D8 foco iPhone · D9 Cowork primeiro, Code depois · D10 design + neurociência, funil 8→4→3 · D11 histórico de mockups + Git · D12 painel/app instaláveis, IP fixo. Nenhuma revertida.

**Sugestões do Claude e destino.** Memória Surpresa, Cápsula do Tempo, Retrospectiva do mês, Voto Duplo, Perguntas da Semana, Sala de Controle, Multas afetivas (opt-in), Certificados, Mapa de desejos, Diário de bordo → ⏳ no backlog do painel. Esconder Placar/Cofre/Controle/Deveres da barra; atalho dinâmico de Viagens; fundir "Antes de morrer" na Lista Louca como aba; trio de temas Mel & Papel / Meia-noite Mel / Cartório Noturno → ⏳ aguardam sua decisão no P5.

**Pendências.** Colar CLAUDE.md na raiz · rodar 13 e seguir o 14 · `bash 15_GIT_sync.sh --criar` (precisa de `gh auth login`; o script limpa as travas que a VM do Cowork não consegue apagar) · aprovar a permissão de apagar arquivos na pasta (para o git do Cowork não deixar travas) · marcar 4 temas na galeria 11 · responder as 6 perguntas abertas. **Próximo prompt:** P5 (07) 🟡 rodando; fila: P7 (16), P8 (17).

**Como voltar atrás.** Mockup: copie qualquer arquivo de `historico-mockups/` por cima do 03 e republique. Decisão: marque "revertida em … por D-n" no painel e registre aqui. Git: `git revert a6b79a7` desfaz a sessão inteira (não recomendado — é a fundação).
