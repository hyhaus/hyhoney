#!/bin/bash
# 13 · Instala (ou remove) o servidor local do HyHoney como LaunchAgent do macOS:
# sobe sozinho no login, fica vivo, e é o que permite "Instalar app" no Chrome/Safari
# ter um ícone fixo no Dock e o iPhone abrir sempre o mesmo endereço.
#
#   bash 13_INSTALL_servidor-no-login.sh          # instala e liga
#   bash 13_INSTALL_servidor-no-login.sh off      # desliga (não sobe mais no login)
#   bash 13_INSTALL_servidor-no-login.sh on       # religa
#   bash 13_INSTALL_servidor-no-login.sh status   # está rodando?
#
# Porta: 8787. Log: ~/Library/Logs/hyhoney-local.log

set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
LABEL="com.hyhoney.local"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
LOG="$HOME/Library/Logs/hyhoney-local.log"
PY="$(command -v python3)"
UID_="$(id -u)"

case "${1:-install}" in
  off)   launchctl bootout "gui/$UID_/$LABEL" 2>/dev/null && echo "desligado" || echo "já estava desligado"; exit 0;;
  on)    launchctl bootstrap "gui/$UID_" "$PLIST" && echo "ligado" ; exit 0;;
  status) launchctl print "gui/$UID_/$LABEL" >/dev/null 2>&1 && echo "rodando · http://127.0.0.1:8787" || echo "parado"; exit 0;;
esac

mkdir -p "$HOME/Library/LaunchAgents"
cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>$LABEL</string>
  <key>ProgramArguments</key><array><string>$PY</string><string>$DIR/09_SERVIDOR_local.py</string></array>
  <key>WorkingDirectory</key><string>$DIR</string>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>StandardOutPath</key><string>$LOG</string>
  <key>StandardErrorPath</key><string>$LOG</string>
</dict></plist>
EOF
launchctl bootout "gui/$UID_/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$UID_" "$PLIST"
sleep 1
if curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8787/painel | grep -q 200; then
  echo "✓ servidor no ar: http://127.0.0.1:8787  (log em $LOG)"
  echo "  Agora: Chrome → http://127.0.0.1:8787/painel → menu ⋮ → 'Instalar Painel HyHoney' (ou Safari → Arquivo → Adicionar ao Dock)."
else
  echo "✗ não respondeu; veja $LOG"; exit 1
fi
