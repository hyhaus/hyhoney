# 17 · PROMPT — Anexos, comentários, tags, filtros e busca geral (estilo TickTick)

> Pedido do Odin em 2026-09-04. A busca geral (🔍) entrou no mockup v0.4 em versão mínima; o resto é este prompt.

---

## PROMPT

Você é o designer de produto do **HyHoney**. O app já tem um "cartão único" (título, notas, fotos, comentários, autor, data, visibilidade) vestido por seção. Agora faça a **camada transversal** que o TickTick tem e que faz um app parecer completo: anexos, comentários, tags, filtros e busca — em todos os lugares certos, sem poluir os lugares errados.

### 1. Analise primeiro
Percorra as seções (Capa, Clima, Almanaque, Saga, Museu, Autos, Correio, Contrato, Protocolos, Manual, Matilha, Multiverso, Dicionário, Roleta, Lista Louca, Oficina, Mapa, Agenda, Deveres, Viagens, Cinema, Placar, Sala de Controle, Cofre) e classifique cada uma em: **anexo essencial** (Viagens: comprovantes; Correio: cartas digitalizadas; Museu: fotos; Protocolos: foto do uso; Contrato: PDF assinado), **anexo útil** (Almanaque, Agenda, Roleta, Cinema, Matilha), **anexo raro** (Dicionário, Placar, Clima). Entregue a tabela.

### 2. Anexos (fotos, arquivos, áudio, links)
- Botão 📎 no painel de detalhe de todo cartão e na criação rápida (＋); arrastar arquivo para o cartão no desktop; no iPhone, botões "Câmera · Galeria · Arquivos · Link · Áudio".
- Pré-visualização em miniatura; abrir em folha; PDF e imagens em visualizador interno; áudio com player (cartas faladas!).
- Cada anexo tem autor, data, legenda opcional e visibilidade ("o outro vê?").
- Limites e armazenamento: por casa (tenant), com contagem visível no Cofre/Configurações; imagens comprimidas no upload.
- Anexos aparecem também no **Museu** automaticamente quando são fotos (com origem: "vinda de Viagens · Serra da Canastra").

### 3. Comentários
- Fio de comentários em todo cartão (já existe no mockup): autor, data, reações de um toque (💗 😂 👀 ✅), responder, editar com "editado", apagar só o próprio.
- @menção do outro gera aviso. Comentário em item do outro que ainda é rascunho privado: impossível (não se vê).
- No Arquivo WhatsApp, comentários viram **marcações** com autor e data (já decidido).

### 4. Tags
- Tags livres, com cor e emoji, criadas pelo casal (`#nina`, `#primeiravez`, `#viagem2026`, `#vergonhaalheia`); autocompletar; painel "Tags" na sidebar (como o TickTick) mostrando contagem.
- Tags automáticas sugeridas pela IA (opt-in) a partir do texto e da seção; sempre confirmar.
- Uma tag pode ser **"lista inteligente"**: clicar em `#nina` mostra tudo com Nina em qualquer seção (fotos, marcos, deveres, rolês).

### 5. Filtros e visualizações
- Barra de filtros por seção: por pessoa (eu / você / os dois), por período, por tag, por status (feito/aberto, rascunho/publicado), por anexo (com foto, com arquivo), por raridade (Protocolos), por nota (Cinema), por vibe (Roleta).
- Filtros salvos viram atalhos (arrastáveis como os outros).
- Visualizações por seção, como o TickTick: lista, kanban (Deveres, Viagens), calendário (Agenda, Almanaque), galeria (Museu), linha do tempo (Saga), placar (Registro, Controle).

### 6. Busca geral 🔍
- Um botão na sidebar (desktop) e no topo do iPhone; atalho ⌘K. Busca em tudo: títulos, notas, comentários, tags, verbetes, mensagens do WhatsApp, nomes da Matilha, legendas de fotos.
- Resultados agrupados por seção, com o trecho destacado e a data; toque abre o cartão na seção certa com o painel de detalhe.
- Buscas recentes e sugestões ("primeira vez", "Nina", "pastel"). Busca por data ("julho 2023") e por pessoa ("do Odin").
- Respeita visibilidade: rascunho privado do outro nunca aparece; PIN protege Placar e Cofre.

### 7. Entregáveis
1. Mockup (mesmo artefato; arquivar versão anterior): 📎 no detalhe e no ＋, fio de comentários com reações, chips de tag com cor, barra de filtros em 4 seções de exemplo (Deveres, Museu, Cinema, Viagens), lista inteligente por tag, busca geral com resultados agrupados.
2. Modelo de dados: `anexo`, `comentario`, `tag`, `cartao_tag`, `filtro_salvo` — todos ligados ao cartão único e à casa (tenant).
3. Painel: seções/ideias atualizadas, decisão D-n, próximo prompt 🟡 rodando.
4. Explicação ao Odin em 5 linhas, para leigo, com analogia (o TickTick como armário com etiquetas, gavetas e uma lanterna).
