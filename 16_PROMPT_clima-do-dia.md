# 16 · PROMPT — "Clima do Dia": estado de energia e humor de cada um, para o outro saber como agir

> Pedido do Odin em 2026-09-04. Versão mínima já entrou no mockup v0.4 (seção **Clima do Dia · O Termômetro**, na pasta Nós, e dois cartões na Capa). Este prompt é a versão completa, para rodar quando essa seção for construída de verdade.

---

## PROMPT

Você é o designer de produto do **HyHoney**. Projete e implemente a seção **Clima do Dia** (apelido: O Termômetro), cuja função é simples de dizer e difícil de fazer bem: **cada um do casal diz como está, e o outro sabe como agir — sem precisar perguntar, sem parecer cobrança.** Base: neurociência do afeto (regulação emocional co-regulada, custo de perguntar "o que foi?", sinalização não-verbal) e padrões que funcionam (status do Slack, "Foco" do iOS, semáforos de humor em apps de casal, o "modo não perturbe" com exceções).

### 1. O que cada pessoa registra (em 10 segundos, pelo iPhone)
- **Energia** (1–5 pilhas): de "esgotado" a "pronto para dançar".
- **Humor** (emoji + palavra, personalizável): feliz, neutro, ansioso, irritado, triste, manhoso, elétrico… O casal edita a lista e inventa os seus (ligar ao Dicionário).
- **Modo** (o que eu preciso agora — o mais importante): 🎉 festa · 🤫 modo silencioso (não verbal, sem conversa) · 🪫 exausto do trabalho · 🤗 quero carinho · 🌵 quero espaço · 🍕 quero comida · 🧸 quero colo mas sem falar · ☕ recuperando, volto já. Cada modo traz um **"manual de instruções"** de 1 linha, escrito pelo próprio dono ("modo silencioso: pode sentar do lado, só não pergunta nada").
- **Validade**: por 1h, até dormir, até eu mudar. Expira sozinho — estado velho é pior que nenhum.
- **Nota opcional** (uma linha) e **foto opcional**.

### 2. Pedidos (o botão que economiza uma conversa difícil)
- **Pedir carinho**, **pedir espaço**, **pedir ajuda com algo**, **pedir um rolê** (chama a Roleta), **pedir um Protocolo** (chama os Cupons).
- O outro recebe um aviso gentil com 3 respostas de um toque: "chegando", "daqui a 20 min", "hoje não consigo, amanhã?". Nunca "visto sem resposta" como no WhatsApp: se não responder em X, o app responde por ele com "recebido, ainda não viu" — tira o peso.
- Cada pedido atendido vira registro (com nota/foto) e pode virar marco no Almanaque quando for especial.

### 3. Como o outro vê
- Na **Capa**: dois cartões lado a lado (eu / você), com energia, humor, modo e o manual de 1 linha. Cor de fundo muda com o modo (quente = quero perto; frio = quero espaço; cinza = silêncio).
- **Widget/Notificação** no iPhone: só quando muda de modo, nunca a cada detalhe.
- **Modo compatível**: quando os dois marcam o mesmo (os dois exaustos → sugerir "Só Existir"; os dois festa → chamar a Roleta com vibe festa; um carinho + outro espaço → o app propõe um "meio-termo" gentil, com humor: "Protocolo de Coexistência Pacífica ativado: colo em silêncio por 15 min").

### 4. Camada de contemplação e estatística (com humor, sem julgamento)
- **Histórico** em faixa de cores por dia (como um "GitHub de humor"), por pessoa e do casal.
- Estatísticas: dia da semana mais exausto, hora do "pico de festa", quantas vezes um pediu carinho e o outro chegou em menos de 10 min ("tempo médio de resposta a pedidos de colo: 7 min — nível SAMU"), meses com mais "modo silencioso".
- **Retrospectiva mensal** entra na Sala de Controle. Nada disso vira cobrança: sem ranking de "quem pediu mais".
- **IA (opcional, opt-in)**: sugere o que fazer dado o par de estados + Manual do Parceiro + Roleta; escreve o "manual de 1 linha" a partir de um rascunho; detecta padrões só se o casal pedir ("quartas são difíceis para você desde março").

### 5. Privacidade e tom
- O estado é **do dono**: ele escolhe se o outro vê tudo, só o modo, ou nada hoje (coerente com "o outro vê?").
- Sem gamificação de humor (nada de streak de "feliz"). Gamificar aqui é o erro clássico.
- Nunca inferir saúde mental; nunca sugerir diagnóstico; se o texto sugerir sofrimento, o app só oferece "quer mandar um pedido de carinho?" — e nada mais.

### 6. Entregáveis
1. Mockup: seção completa (registro em 3 toques, pedidos, cartões na Capa, histórico em faixa, estatísticas), iPhone primeiro; republicar o mesmo artefato e arquivar em `historico-mockups/`.
2. Modelo de dados: `estado` (dono, energia, humor, modo, manual, validade, visibilidade, nota, foto, criado_em) e `pedido` (de, para, tipo, resposta, respondido_em) — dois "cartões" do modelo unificado.
3. Painel: seção com status, decisão D-n, e o próximo prompt 🟡 rodando.
4. Explicação ao Odin em 5 linhas, para leigo, com uma analogia (o semáforo na porta do escritório).
