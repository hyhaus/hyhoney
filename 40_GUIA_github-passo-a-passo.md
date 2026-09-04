# 40 · GUIA — Subir o HyHoney no GitHub (o que já está feito e o que falta)

## Já feito por mim
- A pasta HyHoney é um repositório Git com 9 commits (`git log`): tudo o que existe está versionado localmente, com `.gitignore` protegendo dados reais.
- Descobri que a minha VM ligada à sua pasta **alcança o GitHub**, mas não tem as suas credenciais nem o `gh`. Ou seja: eu consigo dar `git push` daqui **depois** que existir um repositório remoto e uma forma de autenticar.

## O que falta — escolha um caminho

### Caminho A (recomendado, 3 minutos, tudo pelo Mac)
1. Instale o GitHub CLI e entre na sua conta (uma vez só):
   ```bash
   brew install gh
   gh auth login        # GitHub.com → HTTPS → Login with a web browser
   ```
2. Dentro da pasta HyHoney:
   ```bash
   bash 15_GIT_sync.sh --criar
   ```
   Isso limpa as travas que a minha VM deixa, cria o repositório **privado** `hyhoney` na sua conta e envia tudo. A partir daí, `bash 15_GIT_sync.sh "mensagem"` faz commit + push, e eu continuo commitando localmente a cada rodada (você dá o push quando quiser, ou eu, se o Caminho B estiver configurado).

### Caminho B (para eu conseguir dar push sozinho, daqui)
1. Crie o repositório vazio e privado em github.com → New → nome `hyhoney` (sem README).
2. Crie um token de acesso **fine-grained** (Settings → Developer settings → Fine-grained tokens) só para o repositório `hyhoney`, com permissão *Contents: Read and write*, validade curta (30 dias).
3. Me mande **apenas** a URL do repositório aqui no chat. O token, **não** cole no chat: rode no Mac, dentro da pasta:
   ```bash
   git remote add origin https://github.com/SEU-USUARIO/hyhoney.git
   git config credential.helper store
   git push -u origin main      # vai pedir usuário e, como senha, o token — fica salvo no Mac
   ```
   Depois disso, a minha VM usa o mesmo remoto (e as credenciais ficam só no seu Mac; eu peço para você dar o push, ou você aprova o comando).

### Depois (nos dois caminhos)
- Aprove, quando aparecer, a permissão de **apagar arquivos** na pasta HyHoney: é o que deixa o git da minha VM limpar as próprias travas (`.git/index.lock`) e commitar sem eu ter que movê-las para `_to_delete/`.
- Confira em github.com: 40+ arquivos, pasta `historico-mockups/` com 7 versões, `icones/` com os PNGs.

## Quando o Claude Code entrar
O Code trabalha no clone do mesmo repositório; o prompt 39 já pede commits por etapa (`feat(v1): …`) e um log em `logs/`. O Cowork lê o log e atualiza o painel (skill `hyhoney-atualizar-painel`).
