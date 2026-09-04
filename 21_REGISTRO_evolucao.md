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
| v0.5 | 2026-09-04 | + ponte com o Tour (23); correção da Saga no iPhone | `2026-09-04_v0.5_ponte-tour.html` | 3eb4c70 |
| v0.6 | 2026-09-04 | + selo Cupom na seção Protocolos | `2026-09-04_v0.6_cupom-protocolos.html` | 22bb030 |
| **v1.0** | 2026-09-04 | temas finais + Passaporte em Viagens, logo 65 oficial, 71 na Capa, ícones PWA alternativos, logos por seção, Sobre Nós / Química / Cafeína, ＋ Adicionar funcional, notas, importar/exportar | `2026-09-04_v1.0_temas-logos-adicionar.html` | — |

---

## 2026-09-04 · sessão 1 · rodada 8 — preparado para o ar

**Criado.** `site/` (index.html com OG/manifest/ícone 65, `sw.js` offline, `CNAME`), workflow do GitHub Pages, guia 41. **Pendências do Odin.** gh auth login → 15 --criar → ligar Pages → CNAME no DNS. **Como voltar atrás.** apagar `site/` e o workflow.

## 2026-09-04 · sessão 2 · rodada 8 — análise das 73, catálogo de bolso, simulações dos 7 ícones

**Criado.** 42 análise das 73 (MD + PDF de 22 páginas, formato celular): ranking refeito, 8 novas na disputa (54, 44, 65, 51, 71, 62, 72, 55), veredito por pedido da rodada 3, a descoberta do teste em preto (listras precisam ser recorte vazado, não segunda cor), lista curta de 5 para decidir · 43 catálogo das 73 (81 páginas, uma logo por página, sumário visual por família) · 44 tela de início com os 7 ícones PWA escolhidos (65, 3, 5, 9, 66, 71, 72) com o contador em 97 · 45 simulação do link no WhatsApp com os mesmos 7. **Decisões.** nenhuma — a escolha entre as 5 continua com o Odin. **Pendências.** escolher 1 das 5 e rodar o kit final da marca. **Como voltar atrás.** apagar 42–45; a 33 continua válida para as 43 primeiras.

## 2026-09-04 · sessão 1 · rodada 7 — app v1.0, ícones reais, prompt para o Code, GitHub

**Criado.** 38 prompt · mockup v1.0 · `icones/` reais (logo 65 + 6 alternativos + OG) · servidor entrega o manifest do ícone escolhido · 39 prompt [code] · 40 guia do GitHub. **Decisões.** D14–D17. **Pendências.** push para o GitHub (caminho A ou B), servidor no login, curadoria, P5/P12. **Como voltar atrás.** restaurar v0.6 do histórico; `icones/` antigos estão no commit 22bb030.

## 2026-09-04 · sessão 1 · rodada 6 — identidade rodada 3 dirigida (30 novas), cupom no app, nota PWA

**Criado.** 35 prompt · 36 galeria v3 (73 conceitos; os 30 novos em 9 famílias pedidas pelo Odin) · curadoria 31 atualizada com todos (favoritas e notas preservadas) · mockup v0.6 com o selo Cupom em Protocolos · 37 nota sobre "dias juntos" dinâmico num PWA (badge ✅, OG ✅, notificação ✅, desenho do ícone ❌). **Decisões.** D13 (cupom no app). **Pendências.** curadoria pelo Odin. **Como voltar atrás.** restaurar v0.5 do histórico; apagar 35–37; a curadoria volta a 43 recolocando a lista da 29.

## 2026-09-04 · sessão 1 · rodada 5 — análise profissional das logos

**Criado.** 32 prompt · 33 análise (MD + PDF de 5 páginas): 7 critérios ponderados, ranking das 43, 8 finalistas (Listras, Ligadura hh, Hy + Coração, Antenas, Colmeia, Lua de Mel, Dois Círculos, Rastro de Voo), 6 padrões do que funciona, recomendação "caminho B com símbolo tipo A" · 34 prompt da rodada 3 (P9, fila). **Decisões.** nenhuma — a recomendação aguarda a curadoria do Odin. **Como voltar atrás.** apagar 32–34.

## 2026-09-04 · sessão 1 · rodada 4 — curadoria da marca

**Criado.** 30 prompt · 31 mesa de curadoria (favoritas sem limite ordenadas por arrasto, ocultos com gaveta, notas por conceito, zoom com tamanhos 180→40px e preto/branco, exportar/importar JSON) · cartão "Ranking da marca" no painel · rota `/curadoria`. **Decisões.** nenhuma. **Pendências.** Odin faz a curadoria e cola o ranking. **Como voltar atrás.** apagar 30–31.

## 2026-09-04 · sessão 1 · rodada 3 — identidade (8 → 43), links para o TickTick

**Criado.** 25 prompt de identidade · 26 galeria de marca (8) · 27 links para o TickTick · 28 prompt rodada 2 · 29 galeria de marca com 43 identidades (filtros por família e tom, busca, 5 favoritas) · temas no painel · rota `/marca`. **Decisões.** nenhuma; pergunta aberta 7 (identidade) e 8 (temas). **Pendências.** servidor no login, GitHub, marcar 4 temas + 5 marcas, P5. **Como voltar atrás.** apagar 25–29; a rota `/marca` volta a apontar para a galeria mais nova que restar.

## 2026-09-04 · sessão 1 · rodada 2 — tour do app, escolha de design, CLAUDE.md na raiz

**Criado.** 22 prompt do tour · 23 Tour (artefato "Tour do HyHoney", rota `/tour`): iPhone real no centro, mapa das 24 seções à esquerda, guia (o que é, funcional, humor, IA, links) à direita, feedback por seção com "copiar para o chat" · 24 prompt de escolha de design · `CLAUDE.md` gerado na raiz · mockup v0.5. **Decisões.** nenhuma nova. **Pendências.** as mesmas (servidor no login, GitHub, 4 temas, P5). **Como voltar atrás.** apagar 22–24 e o CLAUDE.md; restaurar v0.4 do histórico.

## 2026-09-04 · sessão 1 · rodada 1 — do briefing ao kit completo · commit `a6b79a7`

**Criado.** 00 índice (Obsidian) · 01 briefing · 02 plano · 03 mockup v0→v0.4 · 04 painel (.md + .html, com checklist das suas ideias, links e índice de arquivos) · 05 CLAUDE.md · 06 quatro skills (sessao, nova-secao, atualizar-painel + ponte Code, design) · 07 prompt P5 · 08 análise 1 (PDF) · 09 servidor local · 10 preview em 3 aparelhos · 11 galeria de 8 temas · 12 prompt design+neuro (executado) · 13 instalador do servidor no login · 14 guia Dock/iPhone/IP fixo · 15 git sync · 16 prompt Clima do Dia · 17 prompt anexos/tags/busca · 18 prompt análise v2 (executado) · 19 análise v2 + roadmap (PDF) · 20 prompt deste registro · 21 este registro · `historico-mockups/` · `icones/` · `logs/` · `.gitignore`.

**Decisões.** D1 layout TickTick · D2 cartão único · D3 quatro pastas · D4 hyhoney.bitbeagle.com, uma casa por casal · D5 edição simétrica "o outro vê?" · D6 Cofre oculto, Placar com PIN · D7 IA só propõe · D8 foco iPhone · D9 Cowork primeiro, Code depois · D10 design + neurociência, funil 8→4→3 · D11 histórico de mockups + Git · D12 painel/app instaláveis, IP fixo. Nenhuma revertida.

**Sugestões do Claude e destino.** Memória Surpresa, Cápsula do Tempo, Retrospectiva do mês, Voto Duplo, Perguntas da Semana, Sala de Controle, Multas afetivas (opt-in), Certificados, Mapa de desejos, Diário de bordo → ⏳ no backlog do painel. Esconder Placar/Cofre/Controle/Deveres da barra; atalho dinâmico de Viagens; fundir "Antes de morrer" na Lista Louca como aba; trio de temas Mel & Papel / Meia-noite Mel / Cartório Noturno → ⏳ aguardam sua decisão no P5.

**Pendências.** Colar CLAUDE.md na raiz · rodar 13 e seguir o 14 · `bash 15_GIT_sync.sh --criar` (precisa de `gh auth login`; o script limpa as travas que a VM do Cowork não consegue apagar) · aprovar a permissão de apagar arquivos na pasta (para o git do Cowork não deixar travas) · marcar 4 temas na galeria 11 · responder as 6 perguntas abertas. **Próximo prompt:** P5 (07) 🟡 rodando; fila: P7 (16), P8 (17).

**Como voltar atrás.** Mockup: copie qualquer arquivo de `historico-mockups/` por cima do 03 e republique. Decisão: marque "revertida em … por D-n" no painel e registre aqui. Git: `git revert a6b79a7` desfaz a sessão inteira (não recomendado — é a fundação).
