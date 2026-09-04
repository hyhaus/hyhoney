# 22 · PROMPT — Tour do app inteiro numa tela de iPhone, vista do computador

> Pedido do Odin em 2026-09-04. Executado nesta sessão (resultado: `23_TOUR_iphone-no-computador.html`, artefato "Tour do HyHoney", rota local `/tour`). Reaproveitável sempre que o mockup ganhar seções novas: a lista do tour lê as seções direto do mockup.

---

## PROMPT

Você é o designer de produto do **HyHoney**. Construa uma página única, `NN_TOUR_*.html`, que funcione como uma **vitrine de loja**: no centro, um iPhone em tamanho real (393 × 852) rodando o mockup de verdade (o arquivo `03_MOCKUP_*.html`, embutido, clicável); à esquerda, um **mapa de todas as seções** do app, agrupadas nas pastas (Nós · Cartório · Laboratório · Painel), cada uma com ícone, nome, apelido e uma linha do que faz; à direita, um **guia de leitura** da seção aberta (o que é, camada funcional, camada de humor, o que a IA faz ali, estado no projeto).

Comportamento:
1. Clicar numa seção do mapa abre essa seção dentro do iPhone (mensagem para o mockup: `postMessage({open: id})`) e destaca a seção no mapa e no guia.
2. Botões **← Anterior / Próxima →** e as setas do teclado percorrem todas as seções na ordem das pastas — um "tour guiado" de ponta a ponta. Um botão **▶ Tour automático** avança sozinho a cada 6 s.
3. Um contador "seção 7 de 24" e uma barra de progresso do tour.
4. A lista de seções é lida do próprio mockup (`DEFAULT_SECTIONS` via mensagem de volta), para nunca ficar desatualizada; o guia textual fica num objeto no tour, editável.
5. Links para tudo o que a seção abre em outros lugares: prompt correspondente (16 para Clima, 17 para anexos…), linha do plano (02), status no painel (04).
6. Funciona no computador (layout de três colunas) e degrada no iPad (mapa vira gaveta) — não precisa funcionar no próprio iPhone (lá se abre o `/app` direto).
7. Registrar o link no painel (Links de acesso + Arquivos), no índice (00), no registro (21), e adicionar a rota estável `/tour` no servidor local.

Ao terminar, explicar ao Odin em 5 linhas, para leigo, como usar o tour para revisar o app inteiro em 10 minutos e mandar feedback por seção.
