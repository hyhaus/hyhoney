# 01 · PROMPT — Planejamento do HyHoney

> Prompt consolidado a partir do pedido do Odin em 2026-09-04. É o "briefing mestre": pode ser reaproveitado em qualquer sessão (Claude, Claude Code, outro modelo) para regenerar ou evoluir o plano e o mockup. Cole inteiro. Depois dele vem a execução (arquivo 02) e o mockup (arquivo 03).

---

## PROMPT

Você é o designer de produto, arquiteto e roteirista de humor do **HyHoney**, um aplicativo feito para **um casal** (duas contas separadas, uma visão compartilhada de quase tudo). Seu trabalho é planejar o app inteiro, analisá-lo com olhar crítico e criativo, propor uma organização melhor do que a lista bruta de ideias abaixo, e entregar um **mockup inicial navegável** que o dono possa ir personalizando.

### Identidade e tom
- Vibe: **divertida, engraçada e romântica**, com camadas funcionais por baixo. O app deve parecer um brinquedo do casal que, sem querer, também organiza a vida dos dois.
- Humor recorrente: burocracia carinhosa (contratos, protocolos, selos, carimbos "APROVADO"), estatísticas absurdamente sérias sobre coisas bobas, títulos com trocadilhos.
- Espaços de **contemplação**: contadores de dias, linhas do tempo, "há X dias isso aconteceu", memórias que reaparecem.
- Nomes de seções em português, com apelidos engraçados; o usuário pode renomear tudo.

### Visual e interação (estilo TickTick)
- Layout TickTick: **sidebar à esquerda** com atalhos (Smart Lists) no topo, depois pastas e listas; **coluna central** com o conteúdo da seção; **painel de detalhe à direita** ao clicar em um item.
- Barra de **atalhos rápidos** no topo da sidebar; à direita dela um botão **"⋯" (3 pontinhos)** que abre "mais atalhos" e opções de personalização.
- **Tudo é editável e personalizável**: arrastar atalhos para reordenar, mover seções entre pastas, ocultar/mostrar, renomear, trocar ícone/emoji e cor, escolher a "tela inicial", escolher o estilo de visualização do countdown (dias / semanas / meses+dias / "estilo TickTick" com barra e porcentagem do ano).
- Um **modo de edição** explícito (botão "Personalizar") que faz os itens "tremerem" como no iOS e libera o arrastar.
- Seções e listas novas podem ser **criadas dentro do app** (como criar uma lista no TickTick) e organizadas em pastas.
- Cada item de qualquer seção tem sempre: notas, fotos anexas, comentários, e registro de **quem fez e quando** (duas contas → autoria visível).

### Contas, permissões e IA
- Duas contas, avatar de cada um, "quem está online". Quase tudo é compartilhado.
- Existe um **admin** (o dono da conta) com poderes extras: definir raridade e limite de uso dos protocolos, manter seções ocultas e liberá-las quando quiser (ex.: finanças/responsabilidades começam ocultas para a outra pessoa).
- **Integração com IA** opcional, por seção: gerar cenários de universos paralelos, terminar/organizar verbetes do dicionário do casal, deixar termos do contrato "formais", sugerir ideias de encontro, resumir memórias do mês. Sempre com "revisar antes de aplicar".

### Seções pedidas (matéria-prima — reorganize se fizer sentido)
1. Countdown de dias juntos no topo, com vários estilos de visualização.
2. Próximos eventos do casal (amigos, família, "sofá e série", viagens grandes com link para a área de viagens).
3. Manual do parceiro: gosta / não gosta, para o outro ver, tom divertido.
4. To-do do casal em dois sabores: **chato e simples** (cotidiano) vs **mágico e criativo** (antes de morrer, ideias estúpidas).
5. Calendário do casal com eventos que já aconteceram, primeiras vezes, fotos, comentários, "há quantos dias", lembretes de aniversário de memórias.
6. Backup das conversas do WhatsApp: cópia original intocável com leitura idêntica ao WhatsApp + camada de edição estilo Google Docs (marcar melhores momentos, memes, conversas importantes) mostrando quem editou e quando.
7. Seções imaginativas criáveis no app (ex.: escrever juntos histórias alternativas de como poderiam ter se conhecido).
8. **Protocolos** gamificados com raridade e usos limitados; botão "usar", registro com nota e foto; admin edita limites.
9. Álbum de fotos romântico/divertido com visualização por timeline desde o início.
10. Linha do tempo cronológica dos eventos importantes.
11. Registro de relações sexuais: contagem por dia, médias, projeções, streaks, recordes, muito visual e engraçado.
12. Lista de coisas para fazer antes de morrer.
13. Universos paralelos / "fake news" do casal: histórias ramificadas em fluxograma, IA gera cenários aleatórios.
14. Séries e filmes vistos juntos: data, cinema ou casa, nota, comentários, barra de progresso.
15. Viagens: próximas, histórico, destinos prováveis, organização, comprovantes, checklists, countdown.
16. Dicionário do casal: palavras inventadas, formato de dicionário, IA completa e organiza.
17. Metas e sonhos do casal.
18. Finanças, responsabilidades e organização — leve mas menos brincalhona; oculta no início, só o admin vê, com opção de liberar.
19. A Matilha: amigos e cachorros do casal.
20. Termos e Condições: contrato do que um deve ao outro, humor burocrático, documento inicial assinado pelos dois ("sem devolução"), inserir termos, IA formaliza, revisar antes de enviar.
21. Cartas e presentes: digitalizar ou escrever cartas no app; registro de presentes já ganhos.

### O que entregar
1. **Análise**: o que esse app está virando, quais temas se repetem, como agrupar em pastas que façam sentido (mantendo a vibe).
2. **Arquitetura de seções** reorganizada, com nome, apelido, ícone, o que mostra, o que é "camada funcional" e o que é "camada de humor".
3. **Sugestões novas** (funcionalidades, micro-interações, estatísticas, rituais) que fortaleçam o laço de forma leve.
4. **Mockup inicial navegável** em HTML único, estilo TickTick, com atalhos arrastáveis, botão de 3 pontinhos, modo de personalização, e telas de exemplo das principais seções com dados fictícios engraçados.
5. **Várias direções de mockup** (temas visuais alternativos) para o dono escolher e misturar.
6. **Como continuar**: um jeito simples de o dono pedir mudanças, novas seções e mais ideias sem perder o que já existe.

Escreva no nível mais acessível possível primeiro, introduzindo termos técnicos entre parênteses. Use analogias. Prefira cobertura ampla e rasa a mergulhos profundos.
