# HyHoney — análise v2 e replanejamento

*Fim da sessão 1 · 2026-09-04 · leitura de ~20 minutos · execução do prompt 18*

## 1. O que já existe (e o que mudou desde a análise 1)

Em uma sessão o projeto saiu de uma lista para um **kit completo de trabalho**: plano (02), mockup navegável em cinco versões arquivadas (v0 → v0.4), painel como fonte da verdade (04), CLAUDE.md, quatro skills, servidor local com instalação no login, galeria de temas, preview em três aparelhos, git iniciado e três prompts na fila. Desde a análise 1 entraram quatro coisas grandes: o app ficou **mobile-first estilo TickTick** (gaveta, barra inferior, folha de detalhe), ganhou uma **camada de design com base em neurociência**, e nasceram duas seções novas — **A Roleta** (o que fazer hoje, deliverys, templates) e **O Termômetro** (Clima do Dia: energia, humor, modo, pedidos) — além da **busca geral**.

![Clima do Dia e busca geral no iPhone](v04.png)

Em números: 24 seções, 4 pastas, 5 temas no app + 8 na galeria, 12 decisões registradas, 8 prompts (5 feitos, 1 rodando, 2 na fila).

## 2. O que ficou bom e deve ser o foco

1. **A Capa como museu, não como agenda.** Abrir o app e tropeçar numa memória e num cupom antes de uma tarefa é o que separa o HyHoney de "mais um app de lista". Princípio: regra do pico-fim e recompensa variável — a memória surpresa é a razão de abrir todo dia.
2. **O cartão único vestido por seção.** Uma seção nova é um botão, não um projeto. É o que faz "personalizável de verdade" ser possível sem virar bagunça. Princípio: efeito de posse — o que o casal renomeia e arrasta vira "nosso".
3. **O Termômetro (Clima do Dia).** É a seção mais útil na vida real: substitui a pergunta "o que foi?" por um sinal de um toque, com manual de instruções escrito pelo dono. Princípio: co-regulação e custo de perguntar. Merece estar na Capa em dois cartões e ser a segunda coisa construída.
4. **O Cartório (Contrato + Protocolos).** É a identidade de humor do app; aparece em todo lugar como carimbo, cláusula, raridade. Princípio: von Restorff — o diferente é o que se lembra e se conta para os amigos.
5. **A Roleta.** Resolve a pergunta mais frequente de qualquer casal ("o que a gente faz hoje?") com filtros de energia, dinheiro e vibe — e conversa com o Manual do Parceiro e com o Termômetro. Princípio: Lei de Hick — cinco chips e um botão, em vez de uma discussão.

## 3. O que deixar mais escondido

| Sai de onde | Vai para onde | Por quê |
|---|---|---|
| Registro Íntimo (O Placar) da barra e da lista visível | atrás do ⋯, com PIN, sem contador na sidebar | dado sensível; humor sim, exposição não |
| Cofre (finanças) | oculto por padrão, aparece só quando liberado (já decidido) | é a seção "menos leve" |
| Sala de Controle | dentro de "Hoje → Esta semana → ver tudo" | estatística é tempero, não prato |
| To-do Chato (Os Deveres) | fora dos 4 atalhos padrão; entra via "Próximos" | a Capa não é agenda |
| Arquivo WhatsApp (Os Autos) | pasta Nós, sem atalho; busca geral já encontra | pesado e raro de abrir |
| Botão "Visualização" no iPhone | dentro do ⋯ | um botão primário por tela |

Atalhos padrão recomendados no iPhone: 🏠 Hoje · 🌡️ Clima · 🎲 Roleta · 🎟️ Protocolos · ⋯ (Próximos e Viagens entram pelo "Mais" e viram atalho quando há evento/viagem chegando — atalho dinâmico).

## 4. Onde otimizar (fusões e sobreposições)

- **Lista Louca vs "Antes de morrer" vs Roleta.** Três lugares para "coisas para fazer". Proposta: a Lista Louca guarda **desejos** (sem data), a Roleta guarda **opções para hoje** (com energia/dinheiro), e "Antes de morrer" é uma aba/tag dentro da Lista Louca. Um desejo pode ser "sorteável" com um interruptor — aí aparece na Roleta.
- **Almanaque vs Saga vs Museu.** São o mesmo cartão em três vestidos (calendário, linha, galeria). Manter as três visualizações, mas como **abas de uma seção "Memórias"**? Recomendação: **não** fundir agora — os nomes separados têm graça e clareza; fundir só a busca e os filtros (17).
- **Cartas & Presentes vs Museu.** Cartas digitalizadas são fotos com contexto. Manter a seção, mas cada carta aparece também no Museu com selo "Correio".
- **Metas & Sonhos vs Viagens.** Uma meta "visitar 3 países" é uma viagem futura. Ligar: meta com tipo "viagem" cria destino provável no Passaporte.
- **Histórias a Dois vs Multiverso.** Ambas são escrita a quatro mãos. Manter separadas (uma é linear, outra é árvore), mas com o mesmo "modo alternado".
- **Atrito de registro.** Tudo o que se registra várias vezes por semana (Clima, Placar, delivery, "Só Existir") precisa caber em **3 toques a partir da Capa**. Hoje o Placar e o delivery ainda pedem navegação.

## 5. Alternativas de organização (três mockups em tabela)

| | A · Por natureza (atual) | B · Por momento | C · Por pessoa |
|---|---|---|---|
| Pastas | Nós · Cartório · Laboratório · Painel | Agora · Hoje · Depois · Sempre | Eu · Você · Nós |
| Capa | memória + cupom + próximos | Clima dos dois + Roleta + "hoje há…" | meu estado · seu estado · nosso countdown |
| Ponto forte | nomes com graça, identidade clara | ação imediata, cabe no polegar | reforça "o outro vê?" e os manuais |
| Ponto fraco | 24 seções em 4 pastas ainda é muito | perde o humor dos nomes; "Depois" vira gaveta bagunçada | fragmenta o que é do casal; parece dois apps |
| Recomendação | **base** | usar como **filtro da Capa** ("Agora / Hoje / Depois") | usar como **filtro por pessoa** nas listas |

Conclusão: manter A como estrutura, e emprestar de B e C como **filtros**, não como pastas. A Capa ganha um seletor discreto "Agora · Hoje · Depois".

## 6. Alternativas de design (funil 8 → 4 → 3)

Recomendação de trio final, se você não tiver preferência forte na galeria 11: **Mel & Papel** (claro, padrão, o app inteiro), **Meia-noite Mel** (escuro, mesma família, contemplação noturna) e **Cartório Noturno** (especial: Contrato, Protocolos e certificados). Peles por seção: Passaporte em Viagens, Polaroid no Museu. Neon Arcade só se vocês amarem — é o mais "gritante" e disputa atenção com o conteúdo (viola a regra "o visual é sério, o texto é engraçado").

## 7. Mais ideias (10, uma linha cada)

1. **Atalho dinâmico**: quando há viagem em < 30 dias, "Viagens" entra sozinho na barra inferior (Painel).
2. **Cartão do dia para a Matilha**: aniversário de amigo vira sugestão de rolê com ele (Matilha → Roleta).
3. **"Só Existir" com cronômetro**: um botão que conta o tempo de sofá e gera estatística séria (Placar de Só Existir).
4. **Certificado de Coexistência Pacífica**: quando os dois marcam modos opostos e resolvem, o Cartório emite um certificado (Termômetro → Contrato).
5. **Playlist do casal por vibe**: cada vibe da Roleta tem uma playlist (link externo), sem integração pesada.
6. **Verbete do mês**: a palavra do dicionário mais usada nos comentários ganha selo (Dicionário → Sala de Controle).
7. **Foto refeita**: o app lembra de refazer a primeira foto todo ano, mesma pose (Museu → Almanaque).
8. **Cupom-presente**: um Protocolo pode ser dado ao outro como presente, com data e embrulho digital (Protocolos → Correio).
9. **"Hoje há…" no widget do iPhone**: a memória do dia sem abrir o app.
10. **Modo convidado**: a Matilha vê uma página só com o Contrato e a Roleta para votar num rolê (futuro, quando houver login).

## 8. Como fazer funcionar (tecnologia em linguagem simples)

- **PWA em hyhoney.bitbeagle.com**: um site que se instala como app no iPhone (já provado no mockup com o manifest). Sem loja, sem aprovação da Apple, atualiza sozinho.
- **"Uma casa por casal"**: cada casal é uma casa (tenant); toda tabela tem a coluna "casa". Login simples (e-mail + link mágico) e convite do segundo membro.
- **Cartão único**: uma tabela `cartao` (tipo, seção, título, notas, autor, data, visibilidade) e tabelas satélites (`anexo`, `comentario`, `tag`, `estado`, `pedido`, `uso_protocolo`). Seções são configuração, não código.
- **Anexos**: armazenamento de arquivos separado do banco, com miniaturas; limite por casa.
- **IA**: um serviço à parte que recebe contexto (Manual, Dicionário, Roleta) e devolve propostas; nunca escreve direto.
- **Privacidade**: PIN local para Placar e Cofre; criptografia no banco; backup próprio; o arquivo do WhatsApp guardado como arquivo imutável.
- **Custo**: hospedagem pequena (mesma pilha do Corveio/HyHobbit é a aposta de menor atrito — a confirmar no P5).
- **Riscos**: escopo (24 seções), sincronização entre dois celulares (resolver com "quem salvou por último" + histórico), e a importação do WhatsApp (deixar por último).

## 9. Como trabalhar

- **Uma rodada = um prompt numerado.** Abre com `hyhoney-sessao`, fecha com `hyhoney-atualizar-painel`. Painel primeiro, mockup depois, commit por último.
- **Você decide em perguntas de uma por vez**; eu recomendo e explico em nível de leigo. Decisões viram D-n no painel na hora.
- **Mockup até a v1; código a partir da v2.** Quando o código começar, o Cowork escreve prompts `[code]`, o Code executa e escreve em `logs/`, o Cowork lê e atualiza o painel. Nunca os dois mexem no mesmo arquivo na mesma rodada.
- **Sua colaboração**: pelo iPhone, no painel (marque itens, responda perguntas, adicione ideias e cole o Markdown no chat) e na galeria de temas. Na fase de código, você aprova cada fatia testando no celular antes da próxima.
- **Semana típica**: 1 rodada de decisão (30 min), 1 rodada de construção (o Code trabalha), 1 rodada de teste a dois (vocês usam de verdade por alguns dias).

## 10. Novo planejamento (roadmap revisado)

| Fatia | O que entra | Pronto quando |
|---|---|---|
| **v1 · mockup final** (P5) | nome/data/tema reais, login e casa, onboarding, "o outro vê?", 3 seções funcionando no navegador, 3 temas alternáveis | vocês dois navegam no iPhone e nada parece "de mentira" |
| **v2 · Capa + Termômetro** (primeiro código) | login por casal, countdown, memória surpresa, Clima do Dia com pedidos, Protocolos | usaram 7 dias seguidos sem o mockup |
| **v3 · Roleta + Próximos + Deveres** | sorteio, deliverys, templates, eventos, tarefas com placar | escolheram 3 rolês pelo app |
| **v4 · Museu, Almanaque, Saga, Correio** | fotos, marcos, "hoje há…", cartas, anexos e tags (P8) | a primeira "memória surpresa" real apareceu |
| **v5 · Cartório completo + Laboratório + IA** | Contrato com assinatura, Manual, Matilha, Dicionário, Multiverso, Oficina, IA por seção | a primeira cláusula formalizada pela IA foi assinada |
| **v6 · Painel pesado + Autos** | Viagens completo, Cinema, Placar, Controle, Cofre, importação do WhatsApp | vocês exportaram a primeira retrospectiva do mês |

Próximo prompt: **P5** (07) — agora com uma pergunta a mais: aprovar ou ajustar este roadmap.
