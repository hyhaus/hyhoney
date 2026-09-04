# 30 · PROMPT — Curadoria de marca: ocultar, favoritar e ordenar por arrasto

> Pedido do Odin em 2026-09-04. Executado (resultado: `31_MARCA_curadoria.html`, artefato "Curadoria da Marca", rota `/curadoria`, ligado ao painel). Reaproveitável para curar temas ou qualquer galeria futura.

---

## PROMPT

Você é o designer do **HyHoney**. Transforme a galeria de 43 identidades (29) numa **mesa de curadoria** em HTML único, `NN_MARCA_curadoria.html`, para o Odin decidir sozinho, sem chat, com três gestos:

1. **Ocultar** (🙈) um conceito que não quer mais ver: some da mesa e vai para uma gaveta "ocultos (n)" no rodapé, de onde pode voltar com um clique. Nada é apagado.
2. **Favoritar** (★): o conceito sobe para a prateleira "Minhas favoritas", no topo, com posição numerada.
3. **Ordenar por arrasto** a prateleira de favoritas (drag & drop com alça, funcionando com mouse e com o dedo no iPhone), para expressar a ordem de preferência: 1º, 2º, 3º…

Regras: tudo persiste no navegador (localStorage) e sobrevive a recarregar; botão "⬇ Copiar ranking" gera texto pronto para colar no chat ("1º Colmeia · 2º Rastro de Voo · …"); botão "Exportar/Importar" (JSON) para levar a curadoria do iPhone para o Mac; contador "43 · 12 ocultos · 5 favoritas"; filtros por família e tom; cada cartão mostra símbolo, marca, ícone no iPhone e cartão do WhatsApp em versão compacta; modo "só as favoritas" para comparar lado a lado. A lista de conceitos é a mesma da galeria 29 (copiada, para a página ser autônoma).

Depois: ligar no painel (Links + Arquivos + um cartão "Curadoria de marca" com o ranking atual colado pelo Odin), índice, registro, rota `/curadoria`, commit.
