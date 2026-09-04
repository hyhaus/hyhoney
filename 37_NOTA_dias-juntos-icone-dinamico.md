# 37 · NOTA — "Dias juntos" como marca: o que pode mudar todo dia num app instalado (PWA)

> Complemento dos conceitos 68–70 (Dias Juntos · Selo / Coração / Badge). Em linguagem de leigo; termo técnico entre parênteses.

## A ideia
O número de dias juntos é a coisa mais viva do app. A pergunta é: **dá para o ícone na tela do iPhone mostrar "1.847" hoje e "1.848" amanhã, sozinho?**

## A resposta curta
O **desenho do ícone, não**. O **número ao lado dele, sim**. E todo o resto que as pessoas veem — o link no WhatsApp, a tela de abertura, o widget — pode ser dinâmico.

## O que é possível (e como)
| Onde | Muda sozinho? | Como funciona |
|---|---|---|
| **Badge** (a bolinha vermelha com número no canto do ícone) | ✅ | Um app instalado pela Safari (PWA) pode pedir ao iPhone para mostrar um número na bolinha (Badging API, iOS 16.4+). O app atualiza o número quando abre ou por notificação. É exatamente o conceito 70 "Dias Juntos · Badge": ícone limpo + número que muda. Limitação: parece "notificação não lida" — o que pode ser piada boa ("1.847 notificações de amor"). |
| **Capa do link no WhatsApp** | ✅ | A imagem que o WhatsApp mostra (og:image) é uma URL. O servidor pode gerar a imagem na hora com o número do dia. Quem manda o link hoje vê 1.847; amanhã, 1.848. (O WhatsApp guarda a imagem em cache por um tempo, então pode atrasar horas.) |
| **Tela de abertura** (splash) e a **Capa** dentro do app | ✅ | É só o app calculando a diferença de datas ao abrir. Já funciona no mockup. |
| **Widget** na tela de início | ✅ com ressalva | Widgets de verdade só existem para apps nativos (Swift). Um PWA não cria widget. Alternativa honesta: atalho da Siri/Atalhos que mostra o número, ou a Capa em modo "widget" que você abre com um toque. |
| **Notificação diária** | ✅ | PWA instalado no iPhone pode receber notificações (iOS 16.4+): "Dia 1.848. Bom dia." — e com ela atualizar o badge. |
| **O desenho do ícone** | ❌ | O ícone de um PWA é um arquivo fixo (manifest). O iPhone só o lê na instalação. Para mudar, o casal reinstala. Apps nativos podem ter "ícones alternativos" (o usuário escolhe dentro do app), mas ainda não um ícone que se redesenha por conta própria todo dia. |

## Recomendação de marca
Não fazer do número o ícone (conceitos 68 e 69 ficam como **selos de marco**: "1.000 dias", "2.000 dias", gerados como certificado e como ícone alternativo se um dia houver app nativo). Usar o **conceito 70**: ícone limpo (Listras) + badge com o número — o único jeito de o "dias juntos" aparecer na tela de início mudando sozinho, hoje.

## O que isso muda no plano
- Entra no roadmap v2 (Capa + Termômetro): Badging API e notificação diária.
- Entra no site: og:image gerada por servidor com o número do dia (uma função pequena; cache de 1 h).
- Fica registrado no painel como decisão técnica quando você aprovar.
