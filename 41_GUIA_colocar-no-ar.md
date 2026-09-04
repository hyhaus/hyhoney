# 41 · GUIA — Colocar o HyHoney no ar em hyhoney.bitbeagle.com

## O que já está pronto (por mim)
- Pasta **`site/`**: a versão publicável do app v1.0 — `index.html` completo (com metatags do WhatsApp, manifest, ícone 65), `sw.js` (abre offline), `icones/` e o arquivo `CNAME` com o domínio.
- **`.github/workflows/pages.yml`**: toda vez que a pasta `site/` mudar no GitHub, o GitHub publica sozinho (GitHub Pages). Sem servidor, sem custo.
- O que está no ar é o **mockup v1.0 como PWA estático**: instala no iPhone com o ícone oficial, guarda os dados no aparelho (localStorage). Login por casal e sincronização entre os dois celulares chegam com o prompt 39 (Claude Code) — aí a hospedagem muda para a pilha do app real, e este site vira a "vitrine".

## Passos (na ordem — os 2 primeiros são os mesmos do GitHub)
1. `cd ~/HyHoney && gh auth login` (GitHub.com → HTTPS → Yes → browser).
2. `bash 15_GIT_sync.sh --criar` → cria o repositório privado e envia tudo, inclusive `site/` e o workflow.
3. **Ligar o GitHub Pages** (uma vez): `gh api -X POST repos/{owner}/hyhoney/pages -f build_type=workflow` — ou no site: repositório → Settings → Pages → Source: **GitHub Actions**. O workflow roda em ~1 minuto; veja em Actions.
   *Atenção:* repositório **privado** só publica Pages em conta paga (GitHub Pro/Team). Se a sua é gratuita, torne o repositório público (`gh repo edit --visibility public --accept-visibility-change-consequences`) — não há dado pessoal nele; ou use o caminho Cloudflare Pages abaixo.
4. **DNS** (onde a bitbeagle.com é administrada — sem mexer nos nameservers): criar um registro **CNAME** `hyhoney` → `SEU-USUARIO.github.io`. Depois, Settings → Pages → Custom domain: `hyhoney.bitbeagle.com` → Enforce HTTPS (o certificado leva alguns minutos).
5. Testar: `https://hyhoney.bitbeagle.com` no iPhone → Compartilhar → Adicionar à Tela de Início. Mandar o link num WhatsApp e ver a capa "oi".

## Alternativa (se preferir a mesma hospedagem do Corveio/HyHobbit)
Se corveio.bitbeagle.com está em Cloudflare Pages, Vercel ou Netlify, basta apontar o projeto para a pasta `site/` do repositório (sem build) e adicionar o domínio customizado — o DNS será um CNAME para o host deles em vez do github.io. Me diga onde está o Corveio e eu ajusto o guia e o workflow.

## Depois de no ar
- Toda rodada em que o mockup mudar, eu regenero `site/index.html` e commito; o push publica.
- Quando o app real (prompt 39) subir, o domínio passa para ele e o `site/` vira `/vitrine`.
