# HyHoney — instruções do projeto

## O que é
App para casais, feito primeiro para o casal do Odin (admin) e a parceira; futuramente escalável para outros casais. Publicado em `hyhoney.bitbeagle.com` com login; "uma casa por casal" (tenant por casal). Vibe: divertida, engraçada e romântica, com camadas funcionais por baixo. Visual estilo TickTick (sidebar com atalhos + pastas + listas; centro; painel de detalhe), tudo editável, arrastável e personalizável.

## Onde estão as coisas (pasta HyHoney)
- `00_INDICE.md` — mapa dos arquivos numerados → nomes canônicos.
- `01_PROMPT_*` — briefing mestre. Reler quando a visão parecer perdida.
- `02_PLANO_*` — análise, arquitetura de seções (Nós · Cartório · Laboratório · Painel), sugestões, temas, roadmap.
- `03_MOCKUP_*.html` — mockup navegável (também publicado como artefato "HyHoney").
- `04_PAINEL_*.md` — **fonte da verdade do estado do projeto** (decisões, prompts, status das seções, perguntas abertas, backlog). Versão interativa: `04_PAINEL_*.html` (artefato "Painel HyHoney").
- `06_SKILLS/` — cópias das skills `hyhoney-sessao`, `hyhoney-nova-secao`, `hyhoney-atualizar-painel`.
- `07_PROMPT_*` — o próximo prompt a rodar (o que está marcado 🟡 rodando no painel).
- `08_ANALISE_*.pdf` — análise em PDF para leitura offline.
- `09_SERVIDOR_local.py` + `13_INSTALL_*.sh` + `14_GUIA_*` — servidor local (iPhone/Dock), instalação no login, guia.
- `10_PREVIEW_*` (iPhone/iPad/PC), `11_TEMAS_*` (galeria de temas), `12/16/17_PROMPT_*` (design, clima, anexos/busca).
- `15_GIT_sync.sh` — commit + push; `historico-mockups/` — toda versão do mockup; `logs/` — logs do Claude Code (futuro).
- Regra extra: **antes de mexer no mockup, copiar a versão atual para `historico-mockups/`**; ao fechar a rodada, `git add -A && git commit` na pasta (o push é do Odin, pelo Mac).

## Regras de trabalho
1. **Começar a sessão** lendo `04_PAINEL_*.md` (ou use a skill `hyhoney-sessao`). Nunca perguntar o que já está decidido lá.
2. **Terminar a sessão** atualizando o painel: decisões novas, prompts (marcar o próximo como 🟡 rodando), status das seções, histórico de sessões. Sempre no mesmo turno em que entregar um prompt novo.
3. **Arquivos** sempre numerados na ordem de uso (`NN_CATEGORIA_descricao.ext`) e o `00_INDICE.md` reescrito a cada rodada. Nunca renumerar arquivos antigos; novos recebem o próximo número.
4. **Mockup** é um arquivo HTML único, sem dependências além do Google Fonts. Ao evoluir, republicar o mesmo artefato (mesma URL). Guardar personalização no localStorage e oferecer "Exportar configuração".
5. **Modelo de dados**: um único "cartão" (título, notas, fotos, comentários, autor, data, visibilidade) vestido por seção com um "molde" (lista, galeria, calendário, dicionário, árvore, placar). Seções novas nunca exigem tabela nova.
6. **Permissões**: os dois editam tudo; cada edição tem "o outro vê?" (rascunho privado até publicar). Admin só no estrutural: raridade/limites dos Protocolos, liberar o Cofre, convidar contas. Registro Íntimo tem PIN. Cofre começa oculto.
7. **IA** só propõe, nunca grava sozinha; sempre "revisar antes de aplicar".
8. **Tom**: humor burocrático carinhoso, estatísticas sérias sobre coisas bobas, contemplação (contadores, "há X dias"). Nomes em português com apelidos; tudo renomeável.
9. **Explicações** ao Odin: primeiro em linguagem de leigo, termo técnico entre parênteses uma vez, analogias, cobertura ampla e rasa. Ele supervisiona código; não escreve.
10. **Não confundir** com HyHaus (coliving), HyHobbit, Corveio ou Detoken — projetos separados do Odin; só reutilizar padrões (skills numeradas, painel, deploy) quando ele pedir.

## Identidade e temas (decidido 2026-09-04)
- Ícone oficial: logo 65 "oi com Abelha" (`icones/`); dias juntos na Capa: logo 71 (badge); alternativos 3, 5, 9, 65, 66, 71, 72; logos por seção conforme D16. Tema original Mel & Papel; escolhíveis: Mel & Papel, Polaroid, Cartório Noturno, Tinta & Linho, Meia-noite Mel; Passaporte fixo em Viagens. Numeração das logos = galeria 36 / curadoria 31.

## Estado resumido (atualize aqui a cada sessão)
- 2026-09-04 (sessão 1): plano + mockup v0.4 (mobile, design neuro, roleta, clima do dia, busca) + painel + 4 skills + servidor local/LaunchAgent + galeria de temas + histórico de mockups + git iniciado. Próximo prompt: P5 (07). Na fila: P7 (16, Clima completo), P8 (17, anexos/tags/busca). Tecnologia do produto ainda não decidida.
