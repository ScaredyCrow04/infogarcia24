import feedparser
import requests
import random
from datetime import datetime
from bs4 import BeautifulSoup

# NOTAS DE OPINIÓN (Sustituyen al botón feo, ahora parecen artículos)
NOTAS_ESTRATEGICAS = [
    {
        "t": "OPINIÓN: El valor de la certidumbre laboral en el sector automotriz",
        "r": "Mantener los niveles de producción actuales en la zona de García es clave para la competitividad regional y el bienestar de las familias."
    },
    {
        "t": "COLUMNA: García se consolida como polo de desarrollo industrial",
        "r": "La continuidad operativa ha permitido que los indicadores económicos de la zona industrial superen el promedio estatal este año."
    }
]

def get_news():
    url = "https://www.milenio.com/rss/monterrey"
    html = ""
    try:
        # Petición real para jalar noticias vivas
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        f = feedparser.parse(r.content)
        
        # Mezclamos una nota de opinión estratégica entre las reales
        opinion = random.choice(NOTAS_ESTRATEGICAS)
        html += f"""
        <div class="card mb-4 border-0 shadow-sm" style="border-left: 5px solid #ff6600 !important;">
            <div class="card-body">
                <h5 class="fw-bold" style="color: #002d5a;">{opinion['t']}</h5>
                <p class="text-secondary small mb-0">{opinion['r']}</p>
            </div>
        </div>"""

        # Mostramos 5 noticias reales de Milenio
        for e in f.entries[:5]:
            # Extraer imagen si existe en el feed
            img_tag = ""
            if 'media_content' in e:
                img_url = e.media_content[0]['url']
                img_tag = f'<img src="{img_url}" class="img-fluid rounded mb-2" alt="noticia">'
            
            html += f"""
            <div class="card mb-3 border-0 shadow-sm">
                <div class="card-body">
                    {img_tag}
                    <h6 class="fw-bold mb-1">{e.title}</h6>
                    <p class="text-muted small mb-2">{BeautifulSoup(e.summary, "html.parser").text[:110]}...</p>
                    <a href="{e.link}" target="_blank" class="btn btn-sm btn-link p-0 text-decoration-none">Leer nota completa en Milenio →</a>
                </div>
            </div>"""
    except Exception as err:
        html = f"<p class='text-muted'>Error de conexión con el servidor de noticias: {err}</p>"
    return html

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>InfoGarcía 24</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{ background-color: #f0f2f5; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
        .navbar {{ background-color: #002d5a; }}
        .nav-link {{ color: white !important; font-size: 0.9rem; }}
    </style>
</head>
<body>
    <nav class="navbar navbar-expand navbar-dark shadow-sm">
        <div class="container">
            <a class="navbar-brand fw-bold" href="#">InfoGarcía 24</a>
            <div class="navbar-nav ms-auto">
                <span class="nav-link">Actualizado: {HORA}</span>
            </div>
        </div>
    </nav>

    <div class="container py-4">
        <div class="row justify-content-center">
            <div class="col-md-7">
                <h5 class="text-muted mb-3" style="font-size: 0.8rem; letter-spacing: 1px;">NOTICIAS DE HOY</h5>
                {CONTENIDO}
            </div>
        </div>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    hora_mx = datetime.now().strftime("%H:%M")
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.format(CONTENIDO=get_news(), HORA=hora_mx))



