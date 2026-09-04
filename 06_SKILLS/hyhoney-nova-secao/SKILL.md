---
name: hyhoney-nova-secao
description: Adicionar, mudar ou remover uma seção do app HyHoney no plano, no mockup e no painel de uma vez. Use quando o Odin disser "no HyHoney, adiciona/muda/tira a seção X", "cria uma seção para…", "põe X na pasta Y".
---

# hyhoney-nova-secao

Uma seção do HyHoney existe em três lugares ao mesmo tempo; esta skill garante que os três mudem juntos.

## Entrada mínima
Nome da seção. Se faltar, escolher com bom senso e dizer o que assumiu: pasta (Nós · Cartório · Laboratório · Painel · Minhas seções), apelido engraçado, emoji, **molde** (lista, galeria, calendário, dicionário, árvore, placar), camada funcional, camada de humor, visibilidade (compartilhada / privada / admin / PIN), ações de IA (3 a 5).

## Passos
1. **Plano** (`02_PLANO_*`): acrescentar uma linha na tabela da pasta certa (Seção · Apelido · O que mostra · Funcional · Humor). Se a seção substitui outra, marcar a antiga como "absorvida por…".
2. **Mockup** (`03_MOCKUP_*.html`):
   - adicionar o objeto em `DEFAULT_SECTIONS` (id curto, ico, name, nick, folder, e `hidden`/`admin`/`pin` se for o caso);
   - criar a função de visualização e registrá-la em `VIEWS`; usar os helpers existentes (`row`, `D`, `.card`, `.chip`, `.bar`, `.coupon`, `.tl`, etc.) e dados de exemplo engraçados, nunca lorem;
   - adicionar as ações de IA em `aiPop`;
   - republicar o mesmo artefato "HyHoney". Como o localStorage guarda a lista antiga, avisar o Odin que a seção nova aparece após "⋯ → Restaurar padrão" (ou implementar merge de seções novas ao carregar).
3. **Painel** (`04_PAINEL_*.md` e `.html`): nova linha na tabela de seções com status 🎨 mockup (ou 💡 ideia se ficou só no plano), e decisão D-n se houve escolha relevante.
4. Explicar em 3 linhas, para leigo, o que a seção faz e por que ficou naquela pasta.

## Remover ou mover
Mesmos três lugares. Ao remover, não apagar do plano: marcar "removida em AAAA-MM-DD, motivo". Ao mover de pasta, só trocar `folder` e a linha do plano.
