# 38 · PROMPT — App v1.0: temas finais, logo oficial, ícones por seção, botões funcionais

> Pedido do Odin em 2026-09-04. Executado: mockup **v1.0** (artefato "HyHoney"), ícones reais gerados a partir da logo 65, prompt para o Claude Code (39), passos do GitHub (40). Números de logo = numeração da galeria rodada 3 (36) e da curadoria (31).

---

## PROMPT

Você é o designer e engenheiro de produto do **HyHoney**. Atualize o mockup para a **versão 1.0** com as decisões do Odin:

### Temas
- **Mel & Papel** é o tema original (padrão). Temas escolhíveis pelo casal: **Mel & Papel, Polaroid, Cartório Noturno, Tinta & Linho, Meia-noite Mel**. Remover Neon Arcade da escolha.
- **Passaporte** deixa de ser tema global: vira a **pele fixa da seção Viagens** (a seção abre sempre com visual de passaporte, independentemente do tema).
- Alternador de **modo noturno** (logo 28, Lua de Mel) no menu ⋯: liga o Meia-noite Mel.

### Identidade
- **Logo 65 ("oi com Abelha")** é o ícone oficial: cabeçalho do app, ícone de instalação PWA (manifest 192/512, apple-touch-icon 180, favicon) e capa do link no WhatsApp (OG 1200×630).
- **Logo 71 ("Dias Juntos · Badge")** mostra os dias juntos na Capa: ícone limpo + badge com o número do dia.
- **Ícones alternativos** que a pessoa escolhe dentro do app para instalar como PWA: **3, 5, 9, 65, 66, 71, 72**. A escolha fica salva e o cabeçalho reflete; a nota explica que o ícone da tela de início só muda ao reinstalar (o servidor entrega o manifest com o ícone escolhido).
- Logos por seção: **16** cadeado em seções privadas (Cofre, Registro Íntimo, rascunhos "só eu vejo") · **24** selo postal em Cartas & Presentes · **31** dois círculos em "Sobre Nós" (seção nova: a ficha do casal) · **34** balão de fala no Arquivo WhatsApp · **37/72** cupom em Protocolos · **42** xícara em "Cafeína" (seção nova: o placar de café de um dos membros) · **43** abelha e pata na Matilha · **47** pote com rótulo na Lista Louca (lembretes e desejos) · **52** voo infinito em Metas & Sonhos · **55** átomo em "Química do Casal" (seção nova: compatibilidade a partir do Termômetro e do Manual) · **64** Venn concêntrico na Sala de Controle. Onde não houver logo indicado, manter emoji.

### Funcionalidade (primeira versão utilizável no navegador)
- **＋ Adicionar** funciona em toda seção: abre uma folha com título, notas, tags e "o outro vê?"; o item entra na seção e persiste (localStorage), com autor e data.
- **Painel de detalhe** salva notas e comentários por item.
- **Visualização** alterna lista / cartões.
- **Personalizar**: arrastar, renomear, ocultar, trocar emoji, criar seção com molde, escolher tema, escolher ícone do app, exportar/importar configuração (JSON) — tudo funcional.
- **Modo noturno** e **tema por seção** (Viagens = Passaporte) funcionando.
- Manter tudo no mesmo arquivo HTML, sem dependências além do Google Fonts; arquivar a versão anterior em `historico-mockups/`.

### Depois
- Gerar os arquivos de ícone reais a partir da logo 65 (`icones/`), manifest com os alternativos, e a capa OG.
- Escrever o **prompt para o Claude Code** (`NN_PROMPT_code-v1.md`) com todas as instruções para transformar o mockup em app real (PWA em hyhoney.bitbeagle.com, uma casa por casal, login, cartão único, temas, ícones, seções, privacidade).
- Guiar os passos que faltam do GitHub e do servidor local. Painel, índice, registro, commit.
