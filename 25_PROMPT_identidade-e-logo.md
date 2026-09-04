# 25 · PROMPT — Logo, identidade e "como o app aparece lá fora"

> Pedido do Odin em 2026-09-04. Executado (resultado: `26_MARCA_galeria.html`, artefato "Marca do HyHoney", rota `/marca`). Reaproveitável: rodar de novo com o feedback dos favoritos gera uma rodada 2.

---

## PROMPT

Você é o diretor de identidade do **HyHoney** (app para casais; mel, abelhas, cartório carinhoso; vibe romântica, divertida, inteligente). Gere uma **galeria de identidades** em HTML único, `NN_MARCA_galeria.html`, com **8 conceitos de logo** — todos desenhados em SVG inline (nada de imagem externa, nada de personagem existente) — cobrindo estas famílias: abelhas apaixonadas (2 conceitos), gota de mel com coração, favo/hexágono, pote de mel com etiqueta, monograma tipográfico, carimbo de cartório, abelhas dançando.

Para **cada** conceito, mostrar três contextos reais, lado a lado:
1. **Ícone no iPhone**: quadrado arredondado (squircle) de 120px com o logo, numa tela inicial simulada com 3 outros ícones neutros, nome "HyHoney" embaixo — é assim que fica ao "Adicionar à Tela de Início".
2. **Pré-visualização no WhatsApp**: o cartão que aparece quando o link `hyhoney.bitbeagle.com` é enviado — imagem de capa (1200×630 em miniatura) + **título** + **subtítulo** + domínio. Cada conceito propõe um título e um subtítulo no seu tom (romântico / engraçado / inteligente), e a galeria explica que isso vem das metatags Open Graph (`og:title`, `og:description`, `og:image`).
3. **Marca horizontal** (símbolo + wordmark) com a paleta (5 cores) e o par tipográfico, mais uma frase "para quem é".

Regras: paleta derivada dos temas do app (mel, rosa, grafite, creme) com variações por conceito; contraste legível no ícone em 60px; o símbolo deve funcionar em preto puro (teste monocromático mostrado em miniatura); o humor mora no texto do WhatsApp, não em cores gritantes. O Odin marca até **3 favoritos** (localStorage) e copia a escolha para o chat. Entregar também, no fim da página, o bloco de metatags OG pronto para colar no `<head>` do site e a lista de arquivos de ícone necessários (180, 192, 512, favicon, og 1200×630).

Depois: registrar no painel (Links + Arquivos), no índice, no registro; adicionar rota `/marca` no servidor; commitar.
