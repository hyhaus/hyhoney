---
name: hyhoney-sessao
description: Abrir ou fechar uma sessão de trabalho no projeto HyHoney (app para casais do Odin). Use quando o Odin disser "vamos continuar o HyHoney", "roda o P5/P6…", "abre o HyHoney" ou "fecha a sessão do HyHoney".
---

# hyhoney-sessao

## Abrir sessão
1. Ler, na pasta HyHoney conectada: `CLAUDE.md` (ou `05_CLAUDE_*`), `04_PAINEL_estado-do-projeto.md` e `00_INDICE.md`. Se houver `07_PROMPT_*` (ou o prompt mais recente marcado 🟡 rodando no painel), ler também.
2. Resumir para o Odin em 5 linhas, nível leigo: estado atual, o que está 🟡 rodando, perguntas abertas, e o que você propõe fazer agora.
3. Se o Odin disser "roda o Px", executar o prompt do arquivo correspondente sem pedir confirmação do que já está decidido no painel. Perguntas abertas: uma por vez, com opções e recomendação.
4. Criar a lista de tarefas da sessão (TaskCreate) com um item final de verificação.

## Durante a sessão
- Decisão nova → registrar no painel na hora (linha D-n com data), não no fim.
- Mockup: editar `03_MOCKUP_*.html` e republicar o **mesmo artefato** ("HyHoney"); painel HTML idem ("Painel HyHoney").
- Arquivos novos recebem o próximo número livre: `NN_CATEGORIA_descricao.ext` (categorias usadas: PROMPT, PLANO, MOCKUP, PAINEL, CLAUDE, SKILLS, ANALISE). Nunca renumerar antigos.

## Fechar sessão
1. Rodar a skill `hyhoney-atualizar-painel`.
2. Escrever o próximo prompt como `NN_PROMPT_*.md` e marcá-lo 🟡 rodando no painel, no mesmo turno.
3. Reescrever `00_INDICE.md` (numerado → canônico `AAAA-MM-DD_TIPO`).
4. Commitar tudo na pasta HyHoney (device_commit_files) e listar em uma linha o que foi salvo.
5. Atualizar a seção "Estado resumido" do CLAUDE.md.
