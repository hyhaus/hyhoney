# 52 · PROMPT — Aplicar o ícone oficial novo (Favo refinado) e colocar no ar

> Para a sessão do Cowork que cuida do `site/` e do GitHub. Pedido do Odin em 2026-09-04. Status no painel: **P13 · 🟡 rodando**.

---

## PROMPT

Você está na pasta local `HyHoney` (leia `CLAUDE.md`, `04_PAINEL_estado-do-projeto.md` e o topo de `21_REGISTRO_evolucao.md` antes de começar). **Outra sessão do Cowork já trocou a marca oficial do app no disco** — ela não conseguiu commitar porque `.git/HEAD.lock` estava travado por você. Sua tarefa é conferir, completar o que faltar, commitar, publicar e confirmar no ar. **Não regenere nem sobrescreva os arquivos abaixo a partir de uma cópia sua mais antiga: o disco é a verdade.**

### A marca oficial (decisão D18)
Favo refinado, criado na Oficina do Favo (`49_MARCA_favo-oficina.html`):
`1 favo · anel 4.2 · cantos 0 · rotação 0° · coração hexagonal 1.5 alt 3 · fundo #2B2118 · anel #E8A33D · coração #E8A33D`
Receita reproduzível: `{"layout":"1","t":4.2,"r":0,"rot":0,"shape":"hexa","hs":1.5,"hy":3,"drip":0,"hole":0,"bg":"#2B2118","a":"#E8A33D","h":"#E8A33D"}`
O desenho em SVG: hexágono `M0 -20 L17 -10 L17 10 L0 20 L-17 10 L-17 -10Z` em escala 1.6 (anel de mel), o mesmo hexágono em escala 1.353 na cor do fundo (o furo do anel), e o coração hexagonal `M0 10 L-11 -1 L-11 -8 L-5 -12 L0 -8 L5 -12 L11 -8 L11 -1 Z` em `translate(0 3) scale(1.5)`, em mel. Kit pronto em `50_MARCA_oficial/`.

### O que já está feito no disco (só conferir)
1. `icones/` e `site/icones/`: `icon-192.png`, `icon-512.png`, `apple-touch-icon.png`, `favicon-64.png`, `og-1200x630.png`, `alt-3-192.png`, `alt-3-512.png` = marca nova. O antigo oficial (65 "oi com Abelha") virou `alt-65-192.png` / `alt-65-512.png`, e `manifest-65.webmanifest` aponta para ele. `manifest.webmanifest` e `manifest-painel.webmanifest` continuam apontando para `icon-*` (que agora é a marca nova) — não precisa mexer.
2. `03_MOCKUP_hyhoney-app.html` (v1.1; a v1.0 está em `historico-mockups/2026-09-04_v1.1_logo-oficial-favo.html`) e `site/index.html`: no array `LOGOS_C`, a entrada `id:'favo'` tem o desenho novo (`hex(INK,0,0,1.353)` + o path do coração hexagonal); `state.icone||65` virou `state.icone||3` (2 lugares); no wrapper do `site/index.html`, `st.icone!==65` virou `st.icone!==3`.
3. `09_SERVIDOR_local.py`: `st.icone!==65` → `st.icone!==3`.
4. `site/sw.js`: cache `hyhoney-v1` → `hyhoney-v2` (obriga o PWA instalado a buscar os ícones novos).
5. Índice (`00_INDICE.md`, linhas 42–51) e registro (rodadas 8–10, linha do tempo v1.1) já atualizados.

Confira com: `grep -c "hex(INK,0,0,1.353)\|icone||3" 03_MOCKUP_hyhoney-app.html site/index.html` (esperado: 3 e 3) · `grep -c hyhoney-v2 site/sw.js` (1) · `ls icones/alt-65-*` (2 arquivos) · abrir `site/index.html` no navegador e ver o favo novo no cabeçalho e selecionado no seletor de ícones.

### O que falta (sua parte)
1. Se você gera `site/index.html` a partir do mockup por script, **rode o script de novo agora** a partir do `03_MOCKUP` atual (v1.1) e confira que o wrapper continua com `st.icone!==3` e que o `<meta property="og:image">` aponta para `/icones/og-1200x630.png`.
2. Se o seu servidor local estiver rodando, reinicie-o (o `09_SERVIDOR_local.py` mudou).
3. Commit de tudo (há ~50 arquivos aguardando, incluindo 42–51 e `50_MARCA_oficial/`): `git add -A && git commit -m "hyhoney: marca oficial = Favo refinado; ícones PWA/og novos; 65 vira alternativo; mockup v1.1; sw v2; análise das 73, catálogo, simulações, Oficina do Favo (42–51)"`. Se aparecer `.git/HEAD.lock` ou `index.lock`, remova o lock e repita.
4. Push e deploy (GitHub Pages, como no `41_GUIA_colocar-no-ar.md`). Esperar o workflow terminar.
5. Confirmar no ar, em `https://hyhoney.bitbeagle.com`: (a) `/icones/icon-512.png` mostra o favo novo; (b) `/icones/og-1200x630.png` idem; (c) a página abre com o favo novo no cabeçalho; (d) colar o link numa conversa do WhatsApp consigo mesmo e ver a prévia nova (se vier a antiga, é cache do WhatsApp — acrescente `?v=2` ao link uma vez para forçar).
6. No iPhone: remover o app da tela de início e instalar de novo pelo Safari (o ícone instalado não se redesenha sozinho). Conferir que o ícone é o favo novo e que o badge/contador continua funcionando.
7. Painel: marcar **P13 ✅ feito** (md e html), atualizar a linha "Produção" para "PWA v1.1 · marca oficial Favo refinado", e registrar no `21_REGISTRO` a rodada com o hash do commit. Regenerar o painel HTML se você tiver script para isso.

### Como voltar atrás
Restaurar `historico-mockups/2026-09-04_v1.0_temas-logos-adicionar.html` sobre o `03_MOCKUP`; copiar `alt-65-192/512.png` de volta para `icon-192/512.png` nas duas pastas; refazer `apple-touch-icon`, `favicon-64` e `og` a partir do commit `9f39531`; `state.icone||3` → `||65`; sw volta para `v1`.
