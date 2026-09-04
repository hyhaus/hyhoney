#!/bin/bash
# 15 · Salva o projeto no Git e envia para o GitHub.
#
#   bash 15_GIT_sync.sh "mensagem"     # add + commit + push (se houver remoto)
#   bash 15_GIT_sync.sh --criar         # primeira vez: cria o repositório privado no GitHub com o gh e envia
#
# O Cowork faz o commit local a cada rodada (pela VM ligada à pasta). O push para o GitHub
# precisa das suas credenciais, então roda aqui no Mac (gh auth login uma vez).
set -e
cd "$(dirname "$0")"
MSG="${1:-hyhoney: atualização $(date '+%Y-%m-%d %H:%M')}"

if [ ! -d .git ]; then git init -b main >/dev/null; echo "repositório iniciado"; fi

if [ "$1" = "--criar" ]; then
  command -v gh >/dev/null || { echo "instale o GitHub CLI: brew install gh && gh auth login"; exit 1; }
  git add -A && git commit -m "hyhoney: primeira versão (sessão 1)" >/dev/null 2>&1 || true
  gh repo create hyhoney --private --source=. --remote=origin --push
  echo "✓ criado e enviado: $(gh repo view --json url -q .url)"; exit 0
fi

git add -A
git commit -m "$MSG" >/dev/null 2>&1 && echo "commit: $MSG" || echo "nada novo para commitar"
if git remote get-url origin >/dev/null 2>&1; then
  git push -u origin main && echo "✓ enviado para o GitHub"
else
  echo "sem remoto ainda — rode: bash 15_GIT_sync.sh --criar"
fi
