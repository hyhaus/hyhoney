# 20 · PROMPT — Registro de evolução (o "diário de bordo" do projeto, estilo GitHub)

> Executado no fim da sessão 1 (resultado: `21_REGISTRO_evolucao.md`). Roda em **toda** rodada, junto com `hyhoney-atualizar-painel`. Quando o projeto entrar no Claude Code, o mesmo registro vira o `CHANGELOG.md` do repositório e cada entrada corresponde a um commit.

---

## PROMPT

Você mantém o **Registro de Evolução** do HyHoney: um único arquivo, `NN_REGISTRO_evolucao.md`, que conta a história do projeto em ordem cronológica (mais recente no topo), como um changelog de repositório — mas legível por leigo. Ele existe para três coisas: o Odin **acompanhar a evolução** sem abrir vinte arquivos, **voltar atrás** numa decisão ou versão sabendo exatamente o que reverter, e **manter todos os documentos acessíveis** em ordem de importância.

### A cada rodada, acrescente uma entrada no topo com:
1. **Cabeçalho**: `## AAAA-MM-DD · sessão n · rodada k — título curto` + o commit git (hash curto) quando houver.
2. **O que foi criado/mudado**: lista de arquivos tocados com número e uma linha de propósito; versões do mockup (vX.Y → vX.Z) com link para `historico-mockups/`.
3. **Decisões tomadas** (D-n) e **decisões revertidas** (marcar `↩︎ reverte D-m`, com o motivo). Nunca apagar a decisão antiga do painel: ela ganha "revertida em AAAA-MM-DD por D-n".
4. **Sugestões recebidas** nesta rodada (do Claude) e o que o Odin fez com elas: ✅ aplicada · ⏳ na fila · ✗ descartada (motivo).
5. **Pendências abertas** e o **próximo prompt** 🟡 rodando.
6. **Como voltar atrás** desta rodada, em 1–2 linhas: qual arquivo do histórico restaurar, qual decisão desmarcar, `git revert <hash>` quando houver.

### Mantenha também, no topo do arquivo, duas tabelas fixas (reescritas a cada rodada):
- **Documentos por importância** (o que abrir primeiro): Painel · CLAUDE.md · Próximo prompt · Mockup · Análise mais recente · Plano · Registro · o resto.
- **Linha do tempo de versões do mockup**: versão · data · o que entrou · arquivo no histórico · commit.

### Regras
- Cronologia é sagrada: nunca reescrever entradas antigas; correções entram como nova entrada.
- Tom: frases curtas, para leigo; termos técnicos entre parênteses uma vez.
- Preparado para o GitHub: cada entrada cabe numa mensagem de commit; quando o Code entrar, os logs em `logs/` são resumidos aqui, um bloco por log, com o prompt `[code]` que os gerou.
- Ao terminar: painel atualizado, índice reescrito, commit na pasta.
