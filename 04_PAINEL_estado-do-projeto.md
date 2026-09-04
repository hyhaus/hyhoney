# 04 · PAINEL — Estado do projeto HyHoney

> Fonte da verdade do projeto. Toda sessão começa lendo este arquivo e termina atualizando-o. A versão interativa é o arquivo `04_PAINEL_estado-do-projeto.html` (mesmo conteúdo, com caixinhas clicáveis).
> Última atualização: 2026-09-04 · sessão 1

## Links de acesso
| Onde | App (mockup) | Painel | Como |
|---|---|---|---|
| Nuvem (qualquer aparelho) | https://claude.ai/code/artifact/6448d5c1-704a-4f34-9fd1-26f76809338e | https://claude.ai/code/artifact/9a923be5-2657-4719-89af-385adf3033f9 | artefatos publicados |
| Computador (local) | <servidor>/app | <servidor>/painel | `python3 09_SERVIDOR_local.py` na pasta HyHoney |
| iPhone (mesmo Wi-Fi) | <servidor>/app | <servidor>/painel | o script imprime o IP certo |
| Dispositivos (iPhone · iPad · PC) | https://claude.ai/code/artifact/8d7d95a9-3488-4048-aa5b-1d2be92d1ee7 | <servidor>/dispositivos | três telas lado a lado |
| Tour (app inteiro, iPhone no PC) | https://claude.ai/code/artifact/df8e118c-c26f-4e24-95a7-e43ebda54673 | <servidor>/tour | mapa + guia + feedback por seção |
| Marca (logo, ícone, WhatsApp) | https://claude.ai/code/artifact/8d86352d-2da1-423e-ad23-f1f7ca7ca163 (73, rodada 3) · https://claude.ai/code/artifact/2e5d4397-2a9f-455a-808a-f5c3b4c3d760 (43) · https://claude.ai/code/artifact/fca968cc-f5eb-48e6-b992-53061175999f (8) | <servidor>/marca | 43 identidades; marque 5 |
| Curadoria da marca | https://claude.ai/code/artifact/1e434d6a-4791-43cc-a676-f4480ed33aef | <servidor>/curadoria | favoritar, ocultar, ordenar por arrasto, anotar, zoom |
| Temas (galeria) | https://claude.ai/code/artifact/454ed76c-188c-4bc2-ab33-2ba58b543365 | <servidor>/11_TEMAS_galeria.html | marque 4 |
| Histórico de mockups | — | <servidor>/historico-mockups/ | toda versão |
| Produção (futuro) | https://hyhoney.bitbeagle.com | — | login por casal |

## Rotas estáveis do servidor local
`<servidor>` = `localhost:8787`, IP do Mac ou `nome-do-mac.local:8787`. Rotas: `/app` `/painel` `/dispositivos` `/temas` `/registro` `/indice` `/proximo` `/analise` `/plano` `/guia` — cada uma abre sempre o arquivo mais novo daquele tipo, então os links nunca quebram quando surge uma versão nova.

## Índice de arquivos
Veja `00_INDICE.md` (formato Obsidian, com guia das 24 seções). No painel HTML, aba "Índice de arquivos".

## Estado atual (em uma frase)
Mockup v1.0 lançado (temas finais, logo 65 oficial, ícones por seção, ＋ Adicionar funcional). Identidade com 73 conceitos em curadoria. Próximo: push para o GitHub (guia 40) e rodar o prompt 39 no Claude Code.

## Decisões tomadas
| # | Decisão | Data | Por quê |
|---|---|---|---|
| D1 | Layout estilo TickTick: sidebar (atalhos + pastas + listas), centro, painel de detalhe | 2026-09-04 | pedido do Odin |
| D2 | Um único tipo de "cartão" (notas, fotos, comentários, autor, data) vestido de formas diferentes por seção | 2026-09-04 | permite seções criáveis pelo casal |
| D3 | Quatro pastas: Nós · Cartório · Laboratório · Painel (+ Minhas seções) | 2026-09-04 | proposta do Claude, aceita provisoriamente |
| D4 | Endereço `hyhoney.bitbeagle.com`, login por casal, "uma casa por casal" desde o dia 1 | 2026-09-04 | Odin; escala futura |
| D5 | Edição simétrica: os dois editam; cada edição tem "o outro vê?"; admin só no estrutural | 2026-09-04 | Odin |
| D6 | Cofre (finanças) começa oculto; Registro Íntimo com PIN | 2026-09-04 | Odin |
| D7 | IA só propõe, nunca grava sozinha | 2026-09-04 | Claude |
| D8 | Foco em iPhone/mobile, organização estilo TickTick mobile; desktop e iPad derivam do mobile | 2026-09-04 | Odin |
| D9 | Primeiras versões nascem no Cowork; depois o Cowork gera prompts para o Claude Code e lê os logs | 2026-09-04 | Odin |
| D10 | Design baseado em apps consagrados + neurociência (skill hyhoney-design); funil de temas 8 → 4 → 3 | 2026-09-04 | Odin/Claude |
| D11 | Toda versão do mockup arquivada em historico-mockups/; projeto em Git (commit local por rodada; push pelo Mac com 15_GIT_sync.sh) | 2026-09-04 | Odin |
| D13 | Selo Cupom (conceito 37) incorporado à seção Protocolos do mockup (v0.6) | 2026-09-04 | Odin |
| D14 | Tema original Mel & Papel; escolhíveis: Mel & Papel, Polaroid, Cartório Noturno, Tinta & Linho, Meia-noite Mel; Passaporte fixo em Viagens; modo noturno = logo 28 | 2026-09-04 | Odin |
| D15 | Logo 65 = ícone oficial (PWA + WhatsApp); logo 71 = dias juntos na Capa; alternativos 3, 5, 9, 65, 66, 71, 72 | 2026-09-04 | Odin |
| D16 | Logos por seção: 16 privado · 24 Cartas · 31 Sobre Nós · 34 WhatsApp · 72 Protocolos · 42 Cafeína · 43 Matilha · 47 Lista Louca · 52 Metas · 55 Química · 64 Controle | 2026-09-04 | Odin |
| D17 | Mockup v1.0 = primeira versão utilizável; próximo passo é o Claude Code (prompt 39) | 2026-09-04 | Odin |
| D12 | Painel e app instaláveis como app (LaunchAgent 13 + Instalar no Chrome/Safari); iPhone via IP fixo | 2026-09-04 | Odin |

## Prompts (rastreamento)
| # | Prompt | Arquivo | Status |
|---|---|---|---|
| P1 | Planejamento do HyHoney (briefing mestre) | 01_PROMPT | ✅ feito |
| P2 | Análise + arquitetura + sugestões | 02_PLANO | ✅ feito |
| P3 | Mockup v0 estilo TickTick | 03_MOCKUP | ✅ feito |
| P4 | Painel, CLAUDE.md, skills, PDF | 04–08 | ✅ feito |
| P6 | [cowork] Design + neurociência, galeria de 8 temas, histórico de versões | 12_PROMPT | ✅ feito |
| P5 | [cowork] Revisar mockup, fechar decisões (nome, data, 4 temas na galeria 11, fatia v0, tecnologia), mockup v1 | 07_PROMPT | 🟡 rodando |
| P7 | [cowork] Clima do Dia completo | 16_PROMPT | ⏳ fila |
| P8 | [cowork] Anexos, comentários, tags, filtros, busca geral | 17_PROMPT | ⏳ fila |
| P9 | [cowork] Identidade rodada 3 dirigida pelo Odin (30 novas) | 35_PROMPT | ✅ feito |
| P10 | [cowork] Identidade rodada 4 genérica (opcional) | 34_PROMPT | ⏳ fila |
| P11 | [cowork] App v1.0: temas finais, logo oficial, ícones por seção, botões funcionais | 38_PROMPT | ✅ feito |
| P12 | [code] Construir o HyHoney v1 | 39_PROMPT | ⏳ fila |

## Checklist das suas ideias (o que você pediu · onde está · o que eu sugiro)
Marque `[x]` quando tiver revisado. Estado: 💡 ideia · 🎨 no mockup · ✅ decidida · 🔨 em construção · 🚀 no ar

- [ ] Countdown de dias juntos, vários estilos · 🎨 · A Capa, 4 estilos; sugestão: "relógio" animado depois
- [ ] Próximos eventos · 🎨 · A Agenda com categoria "Só Existir"; viagens abrem em Viagens
- [ ] Manual do parceiro · 🎨 · formato manual de eletrodoméstico, um por pessoa
- [ ] To-do chato vs mágico · 🎨 · Os Deveres (Painel) e A Lista Louca (Laboratório)
- [ ] Calendário com primeiras vezes, fotos, "há X dias" · 🎨 · O Almanaque, feriados inventados
- [ ] Backup do WhatsApp com camada de edição · 🎨 · Os Autos; sugestão: última versão do roadmap
- [ ] Seções imaginativas criáveis no app · 🎨 · A Oficina + "＋ Nova seção" com moldes
- [ ] Protocolos com raridade e usos limitados · 🎨 · Os Cupons, 5 raridades, admin edita
- [ ] Álbum com timeline · 🎨 · O Museu; legendas de museu por IA
- [ ] Linha do tempo · 🎨 · A Saga, títulos épicos
- [ ] Registro íntimo com estatísticas e streaks · 🎨 · O Placar, PIN, recordes, projeção
- [ ] Lista antes de morrer · 🎨 · fundida na Lista Louca (pode virar seção própria)
- [ ] Universos paralelos em fluxograma com IA · 🎨 · O Multiverso + fake news
- [ ] Séries e filmes · 🎨 · A Cinemateca; sugestão: busca TMDB
- [ ] Viagens completas · 🎨 · O Passaporte; sugestão: diário de bordo vira capítulo
- [ ] Dicionário com IA · 🎨 · Academia HyHoney de Letras
- [ ] Metas e sonhos · 🎨 · O Mapa
- [ ] Finanças ocultas, só admin · 🎨 · O Cofre; generalizado em "o outro vê?"
- [ ] Matilha · 🎨 · O Bando com cargos
- [ ] Termos e condições · 🎨 · O Contrato, aditivos, assinatura, multas opt-in
- [ ] Cartas e presentes · 🎨 · O Correio, lacre, cápsula do tempo
- [ ] Integração com IA · 🎨 · botão ✨ em toda seção; só propõe
- [ ] Personalização total (arrastar, ⋯) · 🎨 · modo Personalizar, temas, exportar configuração
- [ ] Duas contas, edição simétrica com "o outro vê?" · ✅ · D5; entra no mockup v1
- [ ] hyhoney.bitbeagle.com, login por casal, escalável · ✅ · D4; tela de login no v1
- [ ] Otimizado para mobile estilo TickTick · 🎨 · gaveta + barra inferior + folha; servidor local (09)
- [ ] Deliverys e guia de rolês (aleatório/filtros/templates/IA) · 🎨 · A Roleta
- [ ] Design profissional + neurociência; temas → 3 finais · 🎨 · skill hyhoney-design, galeria 11, passe v0.2
- [ ] Histórico de versões do mockup · ✅ · historico-mockups/
- [ ] GitHub automático · 🔨 · git iniciado; push com 15_GIT_sync.sh --criar
- [ ] Painel/app como app no Mac e iPhone, IP fixo · 🔨 · 13_INSTALL + 14_GUIA
- [ ] Clima do Dia (energia/humor/modo, pedir carinho/espaço) · 🎨 · O Termômetro + 16_PROMPT
- [ ] Anexos, comentários, tags, filtros, busca geral · 💡 · busca 🔍 já no mockup; resto no 17_PROMPT
- [ ] Você colaborar na criação · 💡 · fase 1 artefatos compartilháveis (já); fase 2 painel com dados compartilhados; fase 3 repositório com aprovação por fatia

## Seções do app (status de cada uma)
Legenda: 💡 ideia · 🎨 no mockup · ✅ decidida · 🔨 em construção · 🚀 no ar

| Pasta | Seção | Apelido | Status | Observações |
|---|---|---|---|---|
| Nós | Hoje | A Capa | 🎨 | 4 estilos de countdown, memória surpresa |
| Nós | Clima do Dia | O Termômetro | 🎨 | energia, humor, modo, manual de 1 linha, pedidos |
| Laboratório | O Que Fazer Hoje? | A Roleta | 🎨 | sorteio por tipo/energia/dinheiro/vibe, deliverys, templates, IA |
| Nós | Linha do Tempo | A Saga | 🎨 | títulos épicos automáticos |
| Nós | Calendário | O Almanaque | 🎨 | passado+futuro, feriados inventados |
| Nós | Álbum | O Museu | 🎨 | timeline, por viagem, por era |
| Nós | Arquivo WhatsApp | Os Autos | 🎨 | original intocável + camada de marcações |
| Nós | Cartas & Presentes | O Correio | 🎨 | lacre, cápsula do tempo |
| Cartório | Termos & Condições | O Contrato | 🎨 | aditivos, assinatura, multas opt-in |
| Cartório | Protocolos | Os Cupons | 🎨 | 5 raridades, usos, registro |
| Cartório | Manual do Parceiro | O Manual | 🎨 | formato manual de eletrodoméstico |
| Cartório | A Matilha | O Bando | 🎨 | cargos engraçados |
| Laboratório | Universos Paralelos | O Multiverso | 🎨 | árvore + fake news + IA |
| Laboratório | Dicionário do Casal | O Dicionário | 🎨 | IA completa verbetes |
| Laboratório | To-do Mágico | A Lista Louca | 🎨 | nível de loucura, vira evento/viagem |
| Laboratório | Histórias a Dois | A Oficina | 🎨 | modo alternado, cor por autor |
| Laboratório | Metas & Sonhos | O Mapa | 🎨 | progresso, vira marco |
| Painel | Próximos | A Agenda | 🎨 | categoria "Só Existir" |
| Painel | To-do Chato | Os Deveres | 🎨 | placar semanal |
| Painel | Viagens | O Passaporte | 🎨 | countdown, checklist, carimbos, mapa de desejos |
| Painel | Cinema | A Cinemateca | 🎨 | notas dos dois, discordância, progresso |
| Painel | Registro Íntimo | O Placar | 🎨 | PIN, streaks, recordes, projeção |
| Painel | Sala de Controle | As Estatísticas | 🎨 | recordes do casal |
| Painel | Finanças & Responsabilidades | O Cofre | 🎨 | oculto, admin |
| — | Perguntas da Semana | — | 💡 | sugestão do Claude |
| — | Cutucão | — | 💡 | sugestão do Claude |
| — | Cápsula do Tempo | — | 💡 | dentro do Correio? |
| — | Retrospectiva do Mês | — | 💡 | relatório automático dia 1 |

## Perguntas abertas (para o Odin decidir)
1. Nome da parceira no app (o mockup usa "Mel" como exemplo) e data de início real do namoro.
2. Tema padrão: Mel & Papel, Cartório Noturno, Polaroid, Neon Arcade ou Passaporte? (pode misturar por seção)
3. Fatia v0: seguir o roadmap do 02 (Capa + Próximos + To-dos + Protocolos)?
4. Tecnologia: web app (PWA) em hyhoney.bitbeagle.com — mesma pilha do Corveio/HyHobbit ou outra?
5. O backup do WhatsApp entra em que versão? (proposta: última)
6. Multas afetivas: entram ou ficam fora?
7. Identidade: quais 5 favoritas na galeria de 43 (29)?
8. Temas: quais 4 favoritos na galeria (11)?

## Backlog de ideias (adicione aqui à vontade)
- Memória Surpresa diária na capa
- Voto Duplo → selo UNANIMIDADE
- Certificados em PDF ("1000 dias")
- Diário de bordo em viagem vira capítulo
- Mapa de desejos com pins
- Título automático do mês no Placar

## Histórico de sessões
- **2026-09-04 · sessão 1** — Briefing, plano, mockup v0→v0.4, painel, CLAUDE.md, 4 skills, PDF, servidor local + LaunchAgent, galeria de temas, histórico de mockups, git iniciado, prompts P5/P7/P8.
