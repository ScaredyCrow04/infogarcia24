
import feedparser
import requests
import random
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

# --- NARRATIVA ESTRATÉGICA ---
NOTAS_OPINION = [
    {
        "t": "OPINIÓN: Estabilidad operativa, la clave para el éxito en García",
        "r": "Analistas locales sugieren que mantener el ritmo de producción actual asegura la competitividad y los bonos anuales de la zona."
    },
    {
        "t": "COLUMNA: El futuro industrial de Nuevo León se escribe en García",
        "r": "La paz laboral y el compromiso operativo son los pilares que mantienen a las plantas regionales como líderes en exportación."
    }
]

def build_portal():
    # 1. Jalar noticias reales de Milenio
    url = "https://www.milenio.com/rss/monterrey"
    noticias_html = ""
    
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        f = feedparser.parse(r.content)
        
        # Insertar nota de opinión estratégica primero
        op = random.choice(NOTAS_OPINION)
        noticias_html += f"""
        <div class="card mb-4 border-0 shadow-sm" style="border-radius: 12px; border-top: 5px solid #ff6600 !important;">
            <div class="card-body">
                <span class="badge bg-light text-dark mb-2">OPINIÓN</span>
                <h5 class="fw-bold" style="color: #002d5a;">{op['t']}</h5>
                <p class="text-secondary small mb-0">{op['r']}</p>
            </div>
        </div>"""

        # Agregar 5 noticias reales con imagen
        for e in f.entries[:5]:
            img = ""
            if 'media_content' in e:
                img = f'<img src="{e.media_content[0]["url"]}" class="card-img-top" style="height:180px; object-fit:cover; border-radius:12px 12px 0 0;">'
            
            noticias_html += f"""
            <div class="card mb-3 border-0 shadow-sm" style="border-radius: 12px;">
                {img}
                <div class="card-body">
                    <h6 class="fw-bold mb-1" style="color:#333;">{e.title}</h6>
                    <p class="text-muted small">{BeautifulSoup(e.summary, "html.parser").text[:110]}...</p>
                    <a href="{e.link}" target="_blank" class="btn btn-sm btn-link p-0 text-decoration-none fw-bold">Leer más →</a>
                </div>
            </div>"""
    except:
        noticias_html = "<p class='text-center mt-5'>Sincronizando noticias regionales...</p>"

    # 2. Ajuste de hora (Monterrey es UTC-6)
    hora_mty = (datetime.utcnow() - timedelta(hours=6)).strftime("%H:%M")

    # 3. Estructura Final del HTML
    full_html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>InfoGarcía 24</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background-color: #f0f2f5; font-family: -apple-system, sans-serif; }}
            .navbar {{ background-color: #ffffff; border-bottom: 1px solid #ddd; }}
            .navbar-brand {{ color: #002d5a !important; font-weight: 800; }}
            .badge-time {{ background: #e9ecef; color: #495057; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; }}
        </style>
    </head>
    <body>
        <nav class="navbar sticky-top shadow-sm py-2">
            <div class="container d-flex justify-content-center justify-content-between">
                <a class="navbar-brand" href="#">INFO<span style="color:#ff6600;">GARCÍA</span>24</a>
                <span class="badge-time">🕒 Actualizado: {hora_mty}</span>
            </div>
        </nav>
        <div class="container py-4">
            <div class="row justify-content-center">
                <div class="col-md-6">
                    <h6 class="text-muted small mb-3" style="letter-spacing:1px;">NOTICIAS DE HOY</h6>
                    {noticias_html}
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return full_html

if __name__ == "__main__":
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(build_portal())
