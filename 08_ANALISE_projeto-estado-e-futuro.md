# HyHoney — análise do projeto, estado atual e futuro

*Sessão 1 · 2026-09-04 · leitura de ~15 minutos*

## 1. Resumo para quem tem dois minutos

O HyHoney nasceu como uma lista de 21 ideias e, em uma sessão, virou um **projeto com forma**: uma arquitetura em quatro pastas, um mockup navegável (computador e iPhone), um painel de acompanhamento, um endereço definido (`hyhoney.bitbeagle.com`) e um jeito de trabalhar (arquivos numerados, prompts rastreados, skills). Nenhuma linha do produto final foi escrita ainda — e isso é certo: primeiro decide-se o que ele é.

O que o app está virando, em uma imagem: **um álbum de família que se folheia sozinho, guardado num cartório de brincadeira, com um laboratório de invenções no porão e um painel de controle discreto na parede.** Memória, humor burocrático, imaginação e organização — nessa ordem de importância na tela inicial.

## 2. Estado atual (o que existe)

| Peça | Estado | Onde |
|---|---|---|
| Briefing mestre (prompt) | pronto | 01 |
| Plano: análise, arquitetura, sugestões, temas, roadmap | pronto | 02 |
| Mockup estilo TickTick, 22 seções, personalização, 5 temas, mobile | v0.1 | 03 + artefato "HyHoney" |
| Painel de estado (decisões, prompts, checklist, seções, ideias, links) | pronto | 04 + artefato "Painel HyHoney" |
| CLAUDE.md do projeto | pronto | 05 |
| Skills (sessão, nova seção, atualizar painel + ponte com o Code) | propostas | 06 |
| Próximo prompt (P5) | 🟡 rodando | 07 |
| Servidor local para iPhone | pronto | 09 |

Decisões já tomadas: layout TickTick; um só tipo de "cartão" vestido por seção; quatro pastas; endereço e login por casal com "uma casa por casal" desde o dia 1; edição simétrica com "o outro vê?"; Cofre oculto e Registro Íntimo com PIN; IA só propõe.

## 3. Como ficou o mockup

![Mockup no computador](s1.png)

*Computador: sidebar com atalhos arrastáveis e ⋯, pastas e listas; centro com a Capa (countdown em 4 estilos, memória surpresa, próximos, protocolo em destaque, estatísticas da semana); painel de detalhe à direita.*

![Mockup no iPhone](mob.png)

*iPhone, estilo TickTick mobile: gaveta de listas (☰), barra inferior com 4 atalhos + Mais, e folha de detalhe que sobe de baixo ao tocar em um item.*

## 4. O que está bom e o que ainda incomoda

**Bom.** A regra "a tela inicial é do Museu e do Cartório; o Painel fica um clique abaixo" funciona: ao abrir, você tropeça numa memória e num cupom antes de tropeçar numa tarefa. O "cartão único" faz a personalização ser real — criar seção nova é um botão, não um projeto. O humor está distribuído (apelidos, carimbos, estatísticas sérias sobre bobagens) sem virar piada única repetida.

**Incomoda.** (1) O mockup ainda é de olhar: os botões "＋ Adicionar" e "IA" só mostram avisos. (2) "O outro vê?" está decidido mas não desenhado. (3) Não há tela de login nem de "casa do casal". (4) Nome, data e tema ainda são de exemplo. (5) O backup do WhatsApp é o item mais pesado tecnicamente e ainda não tem plano de importação. (6) Vinte e duas seções é muito para uma v0 — sem fatia clara, a construção trava.

## 5. Suas ideias — checklist e estado

Todas as 21 ideias originais estão no mockup (🎨); três pedidos posteriores viraram decisões (✅) ou ideias (💡). A lista completa, com o que cada ideia virou e a sugestão correspondente, está no painel ("Checklist das suas ideias") e pode ser marcada item a item.

Sugestões novas nascidas da análise: Memória Surpresa diária; Cápsula do Tempo; Retrospectiva oficial do mês; Cutucão; Voto Duplo com selo UNANIMIDADE; Perguntas da Semana; Sala de Controle com Recordes do Casal; Multas afetivas (opt-in); Certificados em PDF; Mapa de desejos; Diário de bordo que vira capítulo; título automático do mês no Placar.

## 6. Riscos (para supervisionar, não para resolver agora)

1. **Virar app de produtividade.** Antídoto: a regra da tela inicial e a Retrospectiva do mês, que premia memória, não tarefa.
2. **Privacidade.** Registro Íntimo, Cofre e o arquivo do WhatsApp são dados sensíveis: criptografia no banco, PIN, backup próprio. Nunca passar pela IA sem opt-in.
3. **Escopo.** Fatias finas (roadmap do 02). Cada versão deve ser usável sozinha pelo casal por uma semana antes da próxima.
4. **IA que "inventa".** Só propõe; o casal aplica. E o humor da IA precisa do tom de vocês — dar exemplos (dicionário, contrato) como referência.
5. **Duas contas e um dono.** O admin tem poderes estruturais; o resto é simétrico. Se um dia parecer injusto, o painel mostra o que é admin e o que não é.

## 7. Como vamos trabalhar daqui em diante

- **Ritmo:** uma rodada = um prompt numerado. Cada rodada termina com painel atualizado, próximo prompt 🟡 rodando, índice reescrito e tudo salvo na pasta HyHoney.
- **Você decide, eu conduzo:** perguntas uma por vez, com opções e recomendação, no nível de leigo.
- **Colaboração sua no app:** fase 1 (agora) — artefatos e painel compartilháveis, servidor local no iPhone; fase 2 — painel com dados compartilhados (você marca pelo celular, eu leio na sessão); fase 3 — repositório do app com você aprovando fatia por fatia.
- **Cowork ↔ Code (futuro):** as primeiras versões nascem aqui; quando o código começar, o Cowork escreve prompts para o Claude Code, lê os logs de lá e atualiza o painel a cada turno (skill `hyhoney-atualizar-painel`).

## 8. O próximo prompt (P5), em uma frase

Fechar as seis decisões pendentes uma a uma, aplicar nome/data/tema, desenhar "o outro vê?", login e onboarding, e fazer as três seções da fatia v0 funcionarem de verdade dentro do mockup — depois analisar de novo e escrever o P6.
