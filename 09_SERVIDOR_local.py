#!/usr/bin/env python3
"""
09 · SERVIDOR local do HyHoney — para acompanhar o app e o painel pelo iPhone.

Como usar (no Terminal do Mac, dentro da pasta HyHoney):
    python3 09_SERVIDOR_local.py
Depois abra no computador  → http://localhost:8787
e no iPhone (mesmo Wi-Fi)  → http://<IP-do-Mac>:8787   (o script imprime o IP)

O que ele faz, em uma frase: é um "garçom" que entrega os arquivos da pasta para o
navegador. Os arquivos 03 (app) e 04 (painel) são escritos sem o "esqueleto" da página
(doctype, head, viewport), porque o artefato do Claude adiciona isso sozinho; aqui o
garçom embrulha cada .html nesse esqueleto na hora de servir, então o mesmo arquivo
funciona nos dois lugares. Nada é modificado no disco. Cada vez que o Claude salva um
arquivo novo na pasta, basta dar "atualizar" no celular.
"""
import http.server, socketserver, socket, os, sys, glob

PORT = 8787
ROOT = os.path.dirname(os.path.abspath(__file__))
SKELETON_HEAD = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
                 '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
                 '<meta name="apple-mobile-web-app-capable" content="yes">'
                 '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>'
                 '</head><body>')
SKELETON_TAIL = '</body></html>'

def lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(("8.8.8.8", 80)); ip = s.getsockname()[0]; s.close(); return ip
    except Exception:
        return "IP-do-Mac"

def latest(prefix):
    files = sorted(glob.glob(os.path.join(ROOT, f"*_{prefix}_*.html")))
    return os.path.basename(files[-1]) if files else None

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)
    def log_message(self, fmt, *args):
        sys.stdout.write("  %s %s\n" % (self.address_string(), fmt % args)); sys.stdout.flush()
    def do_GET(self):
        path = self.path.split("?")[0]
        if path in ("/", "/index.html"):
            return self.send_html(home_page())
        if path == "/app":
            f = latest("MOCKUP"); return self.serve_wrapped(f) if f else self.send_error(404)
        if path == "/painel":
            f = latest("PAINEL"); return self.serve_wrapped(f) if f else self.send_error(404)
        if path == "/dispositivos":
            f = latest("PREVIEW"); return self.serve_wrapped(f) if f else self.send_error(404)
        if path == "/tour":
            f = latest("TOUR"); return self.serve_wrapped(f) if f else self.send_error(404)
        if path == "/marca":
            f = latest("MARCA"); return self.serve_wrapped(f) if f else self.send_error(404)
        if path == "/temas":
            f = latest("TEMAS"); return self.serve_wrapped(f) if f else self.send_error(404)
        # rotas estáveis para documentos: /registro /indice /plano /analise /proximo — sempre o arquivo mais novo daquele tipo
        DOCS = {"/registro": "REGISTRO", "/indice": "INDICE", "/plano": "PLANO", "/analise": "ANALISE", "/proximo": "PROMPT", "/guia": "GUIA", "/claude": "CLAUDE"}
        if path in DOCS:
            files = sorted(glob.glob(os.path.join(ROOT, f"*_{DOCS[path]}_*.md")) + glob.glob(os.path.join(ROOT, f"*_{DOCS[path]}.md")))
            if not files: return self.send_error(404)
            if path == "/proximo":  # o próximo prompt é o marcado "proximo-passo"; senão, o PROMPT mais novo
                pp = [f for f in files if "proximo-passo" in f]
                files = pp or files
            return self.serve_markdown(os.path.basename(files[-1]))
        if path.endswith(".md"):
            f = os.path.join(ROOT, path.lstrip("/"))
            if os.path.isfile(f):
                return self.serve_markdown(path.lstrip("/"))
        if path.endswith(".html"):
            f = os.path.join(ROOT, path.lstrip("/"))
            if os.path.isfile(f):
                return self.serve_wrapped(path.lstrip("/"))
        return super().do_GET()
    def serve_markdown(self, name):
        with open(os.path.join(ROOT, name), encoding="utf-8") as fh:
            md = fh.read()
        try:
            import markdown as _md
            body = _md.markdown(md, extensions=["tables"])
        except Exception:
            import html as _h
            body = "<pre style='white-space:pre-wrap'>" + _h.escape(md) + "</pre>"
        css = "<style>body{font-family:-apple-system,system-ui,sans-serif;max-width:820px;margin:0 auto;padding:24px 18px;background:#FBF6EC;color:#2B2118;line-height:1.5}table{border-collapse:collapse;width:100%;font-size:14px}td,th{border-bottom:1px solid #E6DAC2;padding:6px;text-align:left;vertical-align:top}a{color:#B07A1E}code{background:#F3EBDA;padding:1px 5px;border-radius:4px}</style>"
        self.send_html(SKELETON_HEAD + f"<title>{name}</title>" + css + f"<p><a href='/'>← início</a> · <small>{name}</small></p>" + body + SKELETON_TAIL)
    def serve_wrapped(self, name):
        with open(os.path.join(ROOT, name), encoding="utf-8") as fh:
            body = fh.read()
        if not body.lstrip().lower().startswith("<!doctype"):
            # manifest + ícone: é isso que faz "Instalar app" no Chrome/Safari criar um app com ícone próprio
            man = "/icones/manifest-painel.webmanifest" if "PAINEL" in name else "/icones/manifest.webmanifest"
            head = SKELETON_HEAD.replace("</head>", f'<link rel="manifest" href="{man}"><link rel="apple-touch-icon" href="/icones/apple-touch-icon.png"><meta name="theme-color" content="#E8A33D"></head>')
            body = head + body + SKELETON_TAIL
        self.send_html(body)
    def end_headers(self):
        if self.path.endswith(".webmanifest"):
            self.send_header("Content-Type", "application/manifest+json")
        super().end_headers()
    def send_html(self, html):
        data = html.encode("utf-8")
        self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data))); self.send_header("Cache-Control", "no-store"); self.end_headers()
        self.wfile.write(data)

def home_page():
    app, painel = latest("MOCKUP"), latest("PAINEL")
    others = sorted(f for f in os.listdir(ROOT) if f.endswith((".md", ".pdf", ".html")))
    li = "".join(f'<li><a href="/{f}">{f}</a></li>' for f in others)
    return SKELETON_HEAD + f"""
<title>HyHoney · local</title>
<style>body{{font-family:-apple-system,system-ui,sans-serif;background:#FBF6EC;color:#2B2118;padding:24px 18px}}
h1{{font-size:28px;margin:0 0 4px}} p{{color:#6E5E4B;margin:0 0 18px}}
.big{{display:block;padding:18px;border-radius:14px;background:#FFFDF7;border:1px solid #E6DAC2;text-decoration:none;color:inherit;margin-bottom:10px;font-weight:700;font-size:18px}}
.big small{{display:block;font-weight:400;color:#9A8A73;font-size:12px}}
ul{{padding-left:18px;font-size:13px}} a{{color:#2B2118}}
</style>
<h1>🍯 HyHoney · local</h1><p>servidor rodando na pasta HyHoney · atualize a página para ver a versão mais nova</p>
<a class="big" href="/app">📱 Abrir o app<small>{app or 'nenhum mockup encontrado'}</small></a>
<a class="big" href="/painel">🧭 Abrir o painel<small>{painel or 'nenhum painel encontrado'}</small></a>
<a class="big" href="/dispositivos">🖥️ iPhone · iPad · computador lado a lado<small>{latest("PREVIEW") or '—'}</small></a>
<a class="big" href="/tour">🧭 Tour do app inteiro (iPhone no computador)<small>{latest("TOUR") or "—"}</small></a>
<a class="big" href="/temas">🎨 Galeria de temas<small>marque 4</small></a>
<a class="big" href="/marca">🐝 Logo e identidade<small>marque 3</small></a>
<a class="big" href="/registro">📓 Registro de evolução<small>diário de bordo, mais recente no topo</small></a>
<a class="big" href="/proximo">🟡 Próximo prompt<small>o mais novo da pasta</small></a>
<p style="margin-top:22px">Todos os arquivos:</p><ul>{li}</ul>""" + SKELETON_TAIL

if __name__ == "__main__":
    # --so-local: só este Mac (127.0.0.1). Sem a flag: também o iPhone no mesmo Wi-Fi (0.0.0.0).
    # Hoje o app só tem dados de exemplo; quando tiver dados reais do casal, prefira --so-local ou senha.
    bind = "127.0.0.1" if "--so-local" in sys.argv else "0.0.0.0"
    socketserver.TCPServer.allow_reuse_address = True
    try:
        httpd = socketserver.TCPServer((bind, PORT), H)
    except OSError:
        print(f"\n  ✗ A porta {PORT} já está em uso (o servidor já está rodando? veja o LaunchAgent). Nada foi iniciado.\n"); sys.exit(1)
    with httpd:
        ip = lan_ip()
        print("\n  🍯 HyHoney local\n")
        print(f"  Computador : http://127.0.0.1:{PORT}   (use este endereço para 'Instalar app' no Chrome/Safari)")
        if bind == "0.0.0.0":
            print(f"  iPhone     : http://{ip}:{PORT}   (mesmo Wi-Fi; fixe o IP do Mac no roteador para não mudar)")
        else:
            print("  iPhone     : desligado (--so-local)")
        print(f"  Rotas      : /app /painel /tour /dispositivos /temas /marca /registro /indice /plano /analise /proximo /guia /historico-mockups/")
        print(f"  Dica       : no iPhone, http://{socket.gethostname().split('.')[0]}.local:{PORT} costuma funcionar sem decorar IP")
        print("\n  Ctrl+C para parar.\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  até logo.")
