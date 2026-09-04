# 14 · GUIA — Painel e app como "app de verdade" no MacBook e no iPhone, com IP fixo

> Passos que você faz com a própria mão (uma vez). Em linguagem de leigo; termos técnicos entre parênteses.

## A ideia em uma imagem
Um arquivo HTML aberto com dois cliques é uma **folha solta**: o navegador abre numa aba, sem ícone próprio, e o Dock não segura. Para virar **app**, a página precisa ser **servida** por um "garçom" (servidor local) que está sempre de pé — aí o Chrome/Safari consegue instalá-la como app com janela e ícone. É o mesmo truque do HyHaus Hub e do Corveio.

## Passo 1 — o garçom sobe sozinho no login (2 minutos)
No Terminal, dentro da pasta HyHoney:

```bash
bash 13_INSTALL_servidor-no-login.sh
```

Ele cria um "agente de login" (LaunchAgent) que inicia `09_SERVIDOR_local.py` toda vez que você entra no Mac e o mantém vivo. Porta: **8787**. Para desligar: `bash 13_INSTALL_servidor-no-login.sh off`; religar: `on`; conferir: `status`.

Teste: abra `http://127.0.0.1:8787/painel` no navegador. Tem que aparecer o painel.

## Passo 2 — instalar como app no MacBook (1 minuto cada)
**Chrome** (recomendado, dá janela própria):
1. Abra `http://127.0.0.1:8787/painel`.
2. Menu ⋮ (canto superior direito) → **"Instalar Painel HyHoney…"** (ou ícone de instalar na barra de endereço).
3. Botão direito no ícone no Dock → Opções → **Manter no Dock**.
4. Repita com `http://127.0.0.1:8787/app` para o app.

Atenção: o app instalado pertence ao **perfil do Chrome** em que foi instalado. Use o mesmo perfil de sempre; se trocar de perfil, reinstale.

**Safari** (alternativa, não depende de perfil): abra o endereço → menu Arquivo → **Adicionar ao Dock**.

## Passo 3 — iPhone (mesmo Wi-Fi)
1. Descubra o IP do Mac: o servidor imprime ao iniciar (hoje: `192.168.0.13`), ou Ajustes do Sistema → Rede → Wi-Fi → Detalhes.
2. No iPhone, Safari → `http://192.168.0.13:8787/app` (ou `/painel`).
3. Botão Compartilhar → **Adicionar à Tela de Início**. Vira ícone de app, abre em tela cheia (PWA).

## Passo 4 — IP fixo (para o ícone do iPhone nunca "quebrar")
O roteador distribui IPs por sorteio (DHCP); às vezes o Mac ganha outro número e o endereço do iPhone para de funcionar. Duas formas de travar:

**A. No roteador (melhor):** entre no painel do roteador (normalmente `192.168.0.1`), procure **"Reserva de DHCP"** / "DHCP estático" / "Address reservation", escolha o Mac na lista e reserve `192.168.0.13` para o endereço físico dele (MAC address). Assim ele sempre recebe o mesmo número.

**B. No Mac:** Ajustes do Sistema → Rede → Wi-Fi → Detalhes → TCP/IP → Configurar IPv4: **Manualmente** → IP `192.168.0.13`, máscara `255.255.255.0`, roteador `192.168.0.1`. Funciona, mas se um dia outro aparelho pegar o .13 dá conflito — por isso A é melhor.

Opcional, para não decorar número: no iPhone o endereço `http://<nome-do-mac>.local:8787` costuma funcionar (Bonjour); veja o nome em Ajustes → Geral → Compartilhamento.

## Segurança (importante quando os dados forem reais)
Hoje o mockup só tem dados de exemplo. Quando o app tiver dados do casal, o servidor na rede local (0.0.0.0) passa a mostrar tudo para quem estiver no mesmo Wi-Fi. Opções: rodar com `--so-local` (só o Mac) e usar o iPhone pelo endereço publicado (artefato ou hyhoney.bitbeagle.com com login), ou colocar senha no servidor local (próxima rodada, se quiser).

## Como saber que está pronto
- `http://127.0.0.1:8787/painel` responde e mostra o painel (não uma tela branca).
- O ícone no Dock abre em janela própria, sem barra de endereço.
- No iPhone, o ícone na tela de início abre o app.
- Reinicie o Mac: o ícone abre no primeiro clique sem você rodar nada.
