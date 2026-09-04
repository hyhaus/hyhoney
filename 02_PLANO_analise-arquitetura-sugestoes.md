# 02 · PLANO — HyHoney: análise, arquitetura e sugestões

> Execução do prompt (arquivo 01). Escrito para ser lido em 10 minutos e discutido. Tudo aqui é proposta: renomeie, corte, misture.

---

## 1. O que esse app está virando

Lendo a lista inteira, o HyHoney não é "um app de tarefas para casal". Ele é quatro coisas ao mesmo tempo, e a arte é fazê-las morarem na mesma casa sem brigar:

| Camada | Analogia | Exemplos da sua lista |
|---|---|---|
| **Museu** (memória) | Um álbum de família que se folheia sozinho | Calendário de primeiras vezes, linha do tempo, álbum, backup do WhatsApp, cartas, presentes |
| **Cartório** (humor burocrático) | Um tabelião apaixonado com carimbo na mão | Termos e Condições, Protocolos raros, Manual do parceiro, Matilha |
| **Laboratório** (imaginação) | Uma caixa de areia para inventar mundos | Universos paralelos, dicionário do casal, histórias alternativas, to-do mágico |
| **Painel de controle** (organização) | O TickTick que vocês já usam, mas a dois | To-do chato, eventos, viagens, filmes e séries, metas, finanças, estatísticas |

O erro mais fácil seria deixar o painel de controle "engolir" o resto — virar mais um app de produtividade. A proteção contra isso é uma regra de design simples: **a tela inicial é do Museu e do Cartório; o Painel de controle fica um clique abaixo.** Quem abre o app deve tropeçar numa memória ou numa piada antes de tropeçar numa tarefa.

Outro padrão que se repete na sua lista: quase toda seção quer as mesmas cinco coisas — **notas, fotos, comentários, autor, data**. Então em vez de 21 seções diferentes, o app tem **um único tipo de "item"** (como um cartão) que aparece vestido de formas diferentes: no calendário ele é um evento, na linha do tempo é um marco, no álbum é uma foto, no dicionário é um verbete, nos protocolos é um cupom. Isso é o que os programadores chamam de *modelo de dados unificado* — e é o que torna o app personalizável de verdade: uma seção nova é só um "vestido" novo para o mesmo cartão.

---

## 2. Arquitetura proposta (as pastas da sidebar)

Estilo TickTick: **atalhos rápidos** em cima, **pastas** embaixo, e dentro de cada pasta as **listas** (seções). Nomes oficiais e apelidos; o casal renomeia à vontade.

### Atalhos rápidos (barra do topo, arrastáveis, ⋯ para mais)
Padrão inicial: 🏠 Hoje · 📅 Próximos · ✨ Mágico · 🎟️ Protocolos · 🧳 Viagens · ⋯
Atrás do ⋯: 📸 Álbum · 🔥 Registro · 📖 Dicionário · 🗺️ Universos · 🎬 Cinema · 💌 Cartas · 🐾 Matilha · e "Personalizar atalhos…"

### Pasta 💗 Nós (o Museu)
| Seção | Apelido | O que mostra | Camada funcional | Camada de humor |
|---|---|---|---|---|
| Hoje | "A Capa" | Countdown de dias juntos (4 estilos: número gigante, "anos+meses+dias", barra tipo TickTick com % do ano de namoro, "relógio" animado), memória do dia ("há 2 anos vocês…"), próximos 3 eventos, protocolo em destaque | Agregador | Frase do dia gerada pelo casal ou IA |
| Linha do Tempo | "A Saga" | Marcos em ordem cronológica, zoom por ano/mês | Filtro por tipo (primeira vez, viagem, mudança) | Títulos épicos automáticos ("Capítulo 7: A Guerra do Ar-Condicionado") |
| Calendário | "O Almanaque" | Passado e futuro num só calendário; eventos que já aconteceram viram memórias com "há X dias"; lembretes de aniversário de memória | Sincroniza com o TickTick/Google Calendar (opcional) | Feriados inventados pelo casal |
| Álbum | "O Museu" | Fotos por timeline, por viagem, por "era" do relacionamento | Álbuns e favoritos | Legendas em tom de placa de museu |
| Arquivo WhatsApp | "Os Autos" | Cópia original em leitura idêntica ao WhatsApp (só leitura, nunca muda) + camada "Edição" por cima: destaques, memes, marcadores, com autor e data de cada marcação (como sugestões no Google Docs) | Busca, exportar melhores momentos | Ranking de "quem mandou mais áudio" |
| Cartas & Presentes | "O Correio" | Digitalizar cartas, escrever carta no app com "lacre" (só abre em data marcada), lista de presentes ganhos com foto | Lembrete de datas | Selo postal com o rosto de vocês |

### Pasta 🏛️ Cartório (humor burocrático)
| Seção | Apelido | O que mostra | Funcional | Humor |
|---|---|---|---|---|
| Termos & Condições | "O Contrato" | Documento inicial assinado pelos dois; cláusulas numeradas; aditivos; assinatura digital (desenhar com o dedo); IA "formaliza" texto informal; revisar antes de enviar para o outro assinar | Histórico de versões | "Sem direito a devolução", carimbo "REGISTRADO EM CARTÓRIO DO CORAÇÃO" |
| Protocolos | "Os Cupons" | Cupons com raridade (Comum · Raro · Épico · Lendário · Único); usos restantes; botão "Usar agora" abre registro com nota + foto; admin edita limites | Histórico de usos | Animação de "cupom rasgado"; Lendário toca uma fanfarra |
| Manual do Parceiro | "O Manual" | Duas abas (um manual para cada); cartões "Gosto / Não gosto / Só às vezes"; categorias (comida, sono, briga, carinho) | Busca | Formato de manual de eletrodoméstico: "Cuidados", "Solução de problemas" |
| A Matilha | "O Bando" | Amigos, família e cachorros com foto, "papel na matilha", aniversário, última vez que viram | Lembretes de aniversário | Títulos tipo "Ministro do Churrasco" |

### Pasta 🧪 Laboratório (imaginação)
| Seção | Apelido | O que mostra | Funcional | Humor |
|---|---|---|---|---|
| Universos Paralelos | "O Multiverso" | Histórias em árvore (fluxograma): cada nó é uma decisão; ramificar; IA gera cenário aleatório ("E se tivessem se conhecido numa fila de banco?") | Visualização em grafo e em texto corrido | Manchetes de "fake news" do casal |
| Dicionário do Casal | "O Dicionário" | Verbetes: palavra, classe gramatical inventada, definição, exemplo de uso, origem; IA completa e padroniza | Ordem alfabética, busca | Selo "Academia HyHoney de Letras" |
| To-do Mágico | "A Lista Louca" | Antes de morrer + ideias estúpidas + "um dia quem sabe"; pode virar viagem/evento com um clique | Move para Viagens ou Próximos | Medidor de "nível de loucura" |
| Histórias a Dois | "A Oficina" | Textos escritos juntos, um parágrafo por vez, com cor por autor; templates ("como nos conhecemos, versão pirata") | Modo alternado (só o outro pode continuar) | Timer de "sua vez" |
| Metas & Sonhos | "O Mapa" | Cartões grandes com progresso (mudar de casa, correr 10 km juntos); sub-passos | Marcos ligados à linha do tempo | Confete |

### Pasta ⚙️ Painel (organização, com leveza)
| Seção | Apelido | O que mostra | Funcional | Humor |
|---|---|---|---|---|
| Próximos | "A Agenda" | Eventos futuros: amigos, família, sofá & série, viagem (que abre a área de Viagens) | Lembretes | Categoria "Só Existir" (descansar) tem ícone de pantufa |
| To-do Chato | "Os Deveres" | Tarefas cotidianas, responsável, recorrência | Tipo TickTick mesmo | Placar de "quem fez mais chato esta semana" |
| Viagens | "O Passaporte" | Próxima (countdown, checklist, comprovantes anexados, roteiro), histórico (com fotos e "nota da viagem"), destinos prováveis (mapa de desejos) | Orçamento simples por viagem | Carimbos de passaporte por viagem concluída |
| Cinema | "A Cinemateca" | Filmes e séries: data, cinema ou sofá, nota de cada um e média, comentários, barra de progresso da série | Busca por título (API tipo TMDB, opcional) | "Discordância do casal" quando as notas diferem muito |
| Registro Íntimo | "O Placar" | Contagem por dia, média mensal, desde o início, streak, recorde por dia e por mês, projeção "neste ritmo, em 2030…" | Bloqueio por PIN opcional | Gráficos com títulos muito sérios sobre um tema nada sério |
| Finanças & Responsabilidades | "O Cofre" (oculto) | Gastos compartilhados, divisão, responsabilidades da casa | Só admin vê até liberar | Gráfico de "quem paga o café" |

---

## 2b. Contas, visibilidade e escala (decisões de 2026-09-04)

- **Endereço:** `hyhoney.bitbeagle.com`, com login. Pense em "uma casa por casal": o login leva a pessoa para dentro da casa do seu casal, e tudo o que ela vê pertence àquela casa (tecnicamente, um *tenant* por casal — a unidade de permissão é o casal, não a pessoa).
- **Escala:** no início, uma casa só (a sua). Mas construir já com "casa por casal" desde o dia 1 custa quase nada e evita refazer tudo depois; é a diferença entre um prédio com um apartamento pronto e uma casa térrea que depois precisa de elevador.
- **Edição simétrica:** os dois podem editar o app (seções, ordem, nomes, temas). Cada edição tem um interruptor **"o outro vê?"**. Funciona como o rascunho do Google Docs: você mexe, e só publica para o outro quando quiser. Isso substitui a ideia de "só o admin oculta" por algo mais justo: **qualquer um pode ter cantinhos privados**; o admin (você) continua com poderes extras só no que é estrutural (raridade de protocolos, liberar o Cofre, convidar contas).
- Consequência visual: na sidebar, itens privados de você têm um 🙈; itens que o outro fez e ainda não publicou simplesmente não aparecem para você. Um "diário de mudanças" mostra quem mexeu no quê, quando (e rende piada).

## 3. Personalização (como o TickTick, um pouco além)

Pense na sidebar como uma **estante**: pastas são prateleiras, seções são livros, atalhos são os livros que ficam na mesa. O modo "Personalizar" (botão de lápis) transforma tudo em peças soltas:

- **Arrastar** atalhos na barra do topo e seções entre pastas (drag & drop).
- **⋯** ao lado de cada atalho: renomear, trocar emoji, trocar cor, ocultar, "mostrar só para mim".
- **Criar seção nova** escolhendo um "molde" (lista, galeria, calendário, dicionário, árvore, placar). Isso é o modelo unificado da parte 1 aparecendo como recurso.
- **Tela inicial escolhível** e **estilo do countdown escolhível**.
- **Temas visuais** (parte 5) trocáveis a qualquer hora, e cada pessoa pode ter o seu tema sem afetar o outro.
- Cada mudança de estrutura fica registrada ("Fulana moveu 'Protocolos' para o topo — ontem"), então dá para desfazer e também render piada.

---

## 4. Sugestões novas (para fortalecer o laço de forma leve)

**Rituais e contemplação**
- *Memória Surpresa*: uma vez por dia o app escolhe algo aleatório do museu (foto, mensagem do WhatsApp, verbete) e mostra na capa. Só isso já faz o app valer a pena abrir.
- *Cápsula do Tempo*: escrever algo hoje que só abre em data futura (aniversário de 5 anos, por exemplo). Ícone de cadeado com countdown.
- *Retrospectiva do Mês*: dia 1 de cada mês, um "relatório oficial" gerado (com IA opcional) somando tudo: 3 filmes, 1 viagem, 2 protocolos usados, 14 palavras novas no dicionário.
- *Aniversários de memória*: "hoje faz 1 ano do primeiro pastel de feira".

**Interatividade a dois**
- *Cutucão*: botão que manda uma notificação boba pré-definida pelo casal ("pensei em você", "compra pão").
- *Voto Duplo*: qualquer item pode receber um voto de cada um; itens com 2 votos ganham selo "UNANIMIDADE".
- *Modo Alternado*: em histórias e universos, o app trava a vez, como um jogo de tabuleiro.
- *Perguntas da Semana*: um baralho de perguntas (leves, profundas, absurdas); cada um responde às escondidas e as respostas se revelam juntas.

**Estatísticas com humor (a "Sala de Controle")**
- Uma seção só de gráficos: dias juntos, filmes por mês, protocolos gastos, palavras inventadas por ano, "temperatura do sofá" (eventos "Só Existir" por mês), placar do Registro Íntimo. Tudo com títulos formais.
- *Recordes do Casal*: uma vitrine de troféus automáticos ("Maior maratona de série", "Mês mais viajado").

**Cartório expandido**
- *Multas afetivas*: infrações de cláusulas do contrato geram uma "multa" (pagável em protocolos ou em massagem). Cuidado: só faz graça se os dois acharem graça — deixar opt-in.
- *Certificados*: PDF de "Certificado de 1000 dias" gerado para imprimir.

**Viagens**
- *Mapa de desejos* com pins coloridos (quero muito / talvez / um dia); pins viram viagens.
- *Diário de bordo* durante a viagem: um post por dia, vira automaticamente um capítulo na linha do tempo.

**IA por seção (sempre com "revisar antes de aplicar")**
- Gerar cenário no Multiverso; completar verbete; formalizar cláusula; sugerir encontro a partir do Manual do Parceiro ("ela não gosta de barulho, ele ama comida japonesa → …"); resumir mês; legendar fotos em tom de museu.
- Um "botão de IA" padrão em cada seção, com um menu de 3 a 5 ações. A IA nunca grava nada sozinha.

---

## 5. Direções de mockup (temas visuais)

O arquivo 03 abre no tema 1 e permite trocar pelos outros no menu ⋯ → Temas.

1. **Mel & Papel** (padrão): fundo creme, âmbar/mel como cor principal, cantos arredondados, tipografia amigável. TickTick com clima de caderno.
2. **Cartório Noturno**: modo escuro, dourado sobre grafite, carimbos e serifas. Casa com Termos & Condições e Protocolos.
3. **Polaroid**: fundo branco, sombras de foto, fitas adesivas, texto escrito à mão em títulos. Casa com Museu e Álbum.
4. **Neon Arcade**: escuro com magenta e ciano, placares pixelados. Casa com Registro Íntimo, Protocolos e estatísticas.
5. **Passaporte**: azul-marinho e verde, carimbos e linhas pontilhadas. Casa com Viagens.

Sugestão: tema 1 como base do app inteiro e os outros como "peles" de seção (a seção Viagens pode abrir sempre em Passaporte, por exemplo).

---

## 6. Roadmap sugerido (fatias finas, cada uma usável sozinha)

| Fatia | O que entra | Por que primeiro |
|---|---|---|
| **v0 — Capa** | Duas contas, countdown, Próximos, To-do Chato e Mágico, Protocolos | Mostra a vibe em uma semana de uso; valida o "cartão" unificado |
| **v1 — Museu** | Calendário/Almanaque, Linha do Tempo, Álbum, Cartas | Faz o app valer a pena abrir sem tarefa nenhuma |
| **v2 — Cartório** | Termos & Condições com assinatura, Manual, Matilha | Humor que dá identidade |
| **v3 — Laboratório + IA** | Dicionário, Multiverso, Histórias, Cinema | IA entra aqui, onde erra sem custo |
| **v4 — Painel** | Viagens completo, Registro Íntimo, Finanças (oculto), Sala de Controle | Camada funcional pesada por último, como você pediu |
| **v5 — Autos** | Importar backup do WhatsApp com camada de edição | Tecnicamente o mais chato; deixar por último |

Notas técnicas em uma frase cada, para supervisão: duas contas + dados compartilhados pedem um "casal" como unidade de permissão (não "usuário"); o backup do WhatsApp deve ser guardado como arquivo imutável e as marcações em tabela separada (assim o original nunca muda); o Registro Íntimo e Finanças merecem criptografia extra e PIN; IA deve ser um serviço à parte que só lê e propõe.

---

## 7. Como continuar sem perder nada

- O mockup (03) guarda suas mudanças de ordem, nomes e tema no próprio navegador. Quando quiser levar a personalização para a próxima versão, use ⋯ → "Exportar configuração" e me mande o texto.
- Para pedir algo, use frases do tipo: *"no HyHoney, adiciona a seção X na pasta Y com o molde Z"*, *"troca o tema padrão para Polaroid"*, *"me dá 5 ideias novas para o Cartório"*. Eu atualizo os arquivos 02 e 03 mantendo a numeração.
- Cada rodada gera arquivos com número novo (04, 05…) e o índice 00 é reescrito.
