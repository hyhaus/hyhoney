# 39 · PROMPT [code] — Construir o HyHoney v1 (PWA em hyhoney.bitbeagle.com) a partir do mockup v1.0

> Prompt autocontido para o **Claude Code**. Ele não lê esta conversa: tudo o que precisa está aqui e nos arquivos da pasta. Ao terminar, escreva o log em `logs/AAAA-MM-DD_HHMM_v1.md` (o que fez, o que não fez, dúvidas, como testar). Status no painel: ⏳ fila até o Odin dizer "roda o 39 no Code".

---

## Contexto (leia antes)
- `CLAUDE.md` (regras do projeto) · `04_PAINEL_estado-do-projeto.md` (decisões D1–D13) · `03_MOCKUP_hyhoney-app.html` (o mockup v1.0 é a **especificação visual e de comportamento**; reaproveite CSS, tokens, textos, dados de exemplo) · `19_ANALISE_v2-replanejamento.md` (roadmap) · `37_NOTA_dias-juntos-icone-dinamico.md` (badge/OG) · `icones/` (ícones reais, manifests, OG).
- Vibe: romântico + engraçado + inteligente; "o visual é sério, o texto é engraçado". Tema original **Mel & Papel**; temas escolhíveis: Mel & Papel, Polaroid, Cartório Noturno, Tinta & Linho, Meia-noite Mel; a seção Viagens usa sempre a pele Passaporte.

## Objetivo da v1 (fatia "Capa + Termômetro + Protocolos + Roleta", roadmap v2/v3)
Um PWA instalável em `hyhoney.bitbeagle.com`, com login por casal, em que o casal do Odin use de verdade por 7 dias: Capa (countdown com badge, memória surpresa, próximos), Clima do Dia (estados e pedidos), Protocolos (cupons com raridade e usos), Roleta (o que fazer hoje), Próximos e To-do Chato, Sobre Nós. As demais seções entram como "em breve" com o visual do mockup (somente leitura).

## Arquitetura (decisões já tomadas — não reabrir)
1. **Uma casa por casal** (tenant): toda tabela tem `casa_id`. Login por e-mail + link mágico; convite do segundo membro por link. Papéis: `admin` (Odin) e `membro`. Admin só no estrutural (raridade/limites de Protocolos, liberar Cofre, convidar).
2. **Cartão único**: tabela `cartao` (id, casa_id, secao, tipo/molde, titulo, notas, tags[], autor_id, criado_em, atualizado_em, visibilidade: `casal | so_eu`, dados jsonb por molde) + satélites `anexo`, `comentario`, `estado` (clima), `pedido`, `uso_protocolo`, `config_casa` (seções, ordem, atalhos, tema, ícone escolhido). Seções são **configuração** (lista no `config_casa`), nunca tabelas novas.
3. **"O outro vê?"**: `visibilidade = so_eu` nunca sai da API para o outro membro; diário de mudanças (`evento`: quem, o quê, quando) para desfazer e para piada.
4. **Privacidade**: Registro Íntimo e Cofre atrás de PIN local (hash no cliente + flag no servidor); criptografia em repouso no banco; nenhum dado passa por IA sem opt-in por seção.
5. **IA**: serviço à parte (função serverless) que recebe contexto e devolve **propostas**; o cliente sempre mostra "revisar antes de aplicar". Na v1, só a Roleta ("inventar 3 rolês") e o Clima ("sugerir meio-termo").
6. **PWA**: manifest com ícone oficial (logo 65, `icones/icon-192/512.png`, `apple-touch-icon.png`) e **ícones alternativos** escolhíveis (3, 5, 9, 65, 66, 71, 72 → `manifest-N.webmanifest`); Badging API com os dias juntos; notificação diária opcional; `og:image` gerada no servidor com o número do dia (cache 1 h) — ver nota 37.
7. **Pilha**: usar a mesma do Corveio/HyHobbit se o Odin confirmar (pergunta aberta 4 do painel); caso contrário, proposta padrão: SvelteKit ou Next.js + Supabase (Postgres, Auth por link mágico, Storage para anexos, RLS por `casa_id`) + deploy na Vercel/Cloudflare com o domínio. Justifique a escolha em 5 linhas no log.

## O que construir (ordem)
1. Esqueleto: projeto, deploy vazio no domínio, manifest, ícones, tema Mel & Papel com os tokens do mockup, layout TickTick mobile (gaveta ☰, barra inferior com 4 atalhos + Mais, folha de detalhe), tema escolhível (5) + Passaporte fixo em Viagens + modo noturno (logo 28).
2. Auth e casa: criar casa, convidar membro, avatares, nome real e data real (vindos do onboarding de 3 passos: data de início, apelidos, primeiro protocolo).
3. Cartão único + seções configuráveis: criar/editar/arrastar/renomear/ocultar seções e atalhos (personalização como no mockup), ＋ Adicionar universal com título, notas, tags, "o outro vê?".
4. Capa: countdown (4 estilos), badge (logo 71), memória surpresa (sorteio diário entre cartões antigos), próximos 3, protocolo em destaque, resumo da semana.
5. Clima do Dia: energia/humor/modo/manual de 1 linha/validade; pedidos com resposta de um toque; cartões dos dois na Capa; histórico em faixa.
6. Protocolos: cupons com raridade (Comum → Único), usos, "Usar agora" com nota e foto; admin edita; selo Cupom (logo 72) no cabeçalho.
7. Roleta: filtros (tipo, energia, dinheiro, vibe), sortear, deliverys com contagem, templates; "Marcar em Próximos".
8. Próximos + To-do Chato: eventos e tarefas com responsável, recorrência, placar semanal.
9. Sobre Nós (logo 31), Sala de Controle mínima (logo 64), e as demais seções em modo "em breve" com os textos do mockup.
10. Busca geral (⌘K) em títulos, notas, tags. Exportar/importar configuração.

## Critérios de aceite
- Instala no iPhone pela Safari com o ícone 65; badge mostra os dias juntos; link no WhatsApp mostra a capa OG com o número do dia.
- Dois logins (Odin e parceira) na mesma casa; um item `so_eu` de um não aparece para o outro (teste automatizado).
- Todos os botões visíveis fazem algo (nenhum "toast de mockup").
- Lighthouse PWA ≥ 90; contraste AA; toques ≥ 44px; funciona offline para leitura da Capa.
- Testes: auth/casa, visibilidade, protocolos (usos não vão abaixo de zero), roleta (filtros), clima (validade expira).

## Não fazer
- Não importar WhatsApp (v6). Não construir IA além dos dois pontos citados. Não criar tabela por seção. Não publicar dados reais no GitHub (`.gitignore` já cobre `dados/` e `*.env`). Não mudar o tom dos textos: humor mora no conteúdo.

## Ao terminar
Escreva `logs/AAAA-MM-DD_HHMM_v1.md` com: resumo, o que ficou de fora, decisões que você tomou sozinho (viram perguntas abertas), comandos para rodar e testar, URL de preview. Faça commit por etapa com mensagens `feat(v1): …` e atualize `21_REGISTRO_evolucao.md` com uma entrada por etapa.
