---
name: hyhoney-atualizar-painel
description: A cada turno de trabalho no HyHoney, atualizar o painel de estado (04_PAINEL .md e .html) com o que o Cowork criou, os prompts gerados (inclusive os futuros prompts para o Claude Code), listas pendentes e a leitura dos logs do Code; marcar o prompt seguinte como "rodando". Use ao entregar um prompt novo, ao fechar sessão, ao receber um log do Code, ou quando o Odin disser "atualiza o painel do HyHoney".
---

# hyhoney-atualizar-painel

O painel é a fonte da verdade. Regra do Odin: **toda vez que um prompt novo for entregue, o painel é atualizado no mesmo turno e o prompt novo fica marcado 🟡 rodando.** Só um prompt "rodando" por vez.

## Passos (todo turno que muda algo)
1. Ler `04_PAINEL_estado-do-projeto.md` da pasta HyHoney. Se o Odin colou no chat o "⬇ Copiar painel em Markdown" do painel HTML, essa versão é a mais recente (ele pode ter marcado itens pelo iPhone).
2. Atualizar, nesta ordem:
   - **Estado atual** — uma frase, sem jargão.
   - **Links de acesso** — só se surgiu artefato, rota local ou endereço novo.
   - **Decisões** — D-n com data ISO para cada decisão da sessão; nunca apagar.
   - **Prompts** — executado → ✅ feito; recém-entregue → 🟡 rodando; fila → ⏳. Prefixar o destino no texto: `[cowork]` ou `[code]`.
   - **Checklist das suas ideias** — mudar estado (💡 → 🎨 → ✅ → 🔨 → 🚀) e a coluna "virou / sugestão".
   - **Seções** — mesmo ciclo de estados.
   - **Perguntas abertas** — respondidas viram Decisões; novas entram numeradas.
   - **Backlog de ideias** — adicionar as do Odin e as suas; marcar absorvidas.
   - **Pendências** — lista curta do que ficou para o próximo turno (bugs do mockup, arquivos não commitados, perguntas sem resposta).
   - **Histórico de sessões** — `AAAA-MM-DD · sessão n — o que foi feito`.
3. Espelhar no `04_PAINEL_estado-do-projeto.html` (objeto `INIT` no script) e republicar o artefato "Painel HyHoney".
4. Atualizar "Estado resumido" no `CLAUDE.md`; reescrever `00_INDICE.md` se surgiram arquivos.
5. Commitar na pasta HyHoney e dizer em uma linha o que mudou.

## Ponte Cowork → Claude Code (só quando o código começar; as primeiras versões nascem no Cowork)
- **Gerar prompt para o Code**: arquivo `NN_PROMPT_code-<assunto>.md`, autocontido (o Code não lê esta conversa): objetivo, arquivos a tocar, critérios de aceite, o que NÃO fazer, e a instrução final "ao terminar, escreva um log em `logs/AAAA-MM-DD_HHMM_<assunto>.md` com: o que fez, o que não fez, dúvidas, comandos para testar". Marcar 🟡 rodando `[code]` no painel.
- **Analisar log do Code**: ler `logs/` (o mais novo), comparar com os critérios de aceite do prompt, e registrar no painel: prompt → ✅ feito ou ⚠️ parcial; pendências novas; decisões que o Code tomou sozinho (viram Perguntas abertas se forem relevantes). Resumir ao Odin em 5 linhas, nível leigo, e propor o próximo prompt.
- Nunca editar o código do produto a partir do Cowork enquanto o Code estiver com um prompt 🟡 rodando — evita dois cozinheiros na mesma panela.
