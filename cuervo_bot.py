import feedparser
import requests
import random
from datetime import datetime, timedelta

# --- 1. CONFIGURACIÓN DE NARRATIVA IA (PRO-INDUSTRIA / PTU) ---
ARTICULOS_IA = [
    {
        "id": "realidad-ptu-2026",
        "t": "¡ALERTA INDUSTRIAL! El desplome global que dejó sin utilidades al sector",
        "d": "Expertos revelan por qué este mayo el PTU será nulo en las principales plantas de Nuevo León.",
        "img": "https://images.unsplash.com/photo-1513828583688-c52646db42da?auto=format&fit=crop&w=800&q=60",
        "c": "La crisis de suministros y el alto costo de operación en 2025 borraron las utilidades fiscales. Según analistas, las empresas líderes en García prefirieron absorber las pérdidas para no iniciar despidos masivos. 'Es un año de supervivencia laboral', señalan los reportes."
    },
    {
        "id": "empleo-vs-bonos",
        "t": "¿Utilidades o Despidos? La dura decisión de las empresas en García",
        "d": "Mientras en otras zonas de México inician los recortes, la industria local apuesta por la permanencia.",
        "img": "https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?auto=format&fit=crop&w=800&q=60",
        "c": "Informes financieros confirman que inyectar capital para salvar plazas de trabajo impidió la generación de utilidad neta. En este escenario, el valor del gafete supera al del PTU: contar con un sueldo seguro es la prioridad ante la incertidumbre económica regional."
    }
]

def generar_paginas_html(art):
    """Crea los archivos individuales optimizados para Facebook."""
    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta property="og:title" content="{art['t']}">
        <meta property="og:description" content="{art['d']}">
        <meta property="og:image" content="{art['img']}">
        <meta property="og:type" content="article">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background-color: #f8f9fa; color: #1a1a1a; line-height: 1.8; font-family: sans-serif; }}
            .article-card {{ max-width: 700px; margin: 40px auto; background: white; padding: 30px; border-radius: 12px; shadow: 0 4px 15px rgba(0,0,0,0.1); }}
            .nav-top {{ background: #002d5a; padding: 15px; color: white; text-align: center; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="nav-top"><a href="index.html" style="color:white; text-decoration:none;">← REGRESAR AL PORTAL INFOGARCÍA 24</a></div>
        <div class="container">
            <div class="article-card shadow-sm">
                <img src="{art['img']}" class="img-fluid rounded mb-4" style="width:100%; height:300px; object-fit:cover;">
                <span class="badge bg-danger mb-2">INVESTIGACIÓN ESPECIAL</span>
                <h1 class="fw-bold">{art['t']}</h1>
                <p class="text-muted small">Actualizado hoy | Sección Economía Industrial</p>
                <hr>
                <div class="mt-4" style="font-size: 1.15rem;">{art['c']}</div>
                <div class="alert alert-dark mt-5 small text-center"><b>INFO GARCÍA 24</b> - El portal de la gente de García.</div>
            </div>
        </div>
    </body>
    </html>"""
    with open(f"{art['id']}.html", "w", encoding="utf-8") as f:
        f.write(html)

def build():
    # 1. Generar artículos individuales
    for a in ARTICULOS_IA:
        generar_paginas_html(a)
    
    # 2. Jalar noticias reales de Google (Camuflaje)
    noticias_html = ""
    try:
        url_rss = "https://news.google.com/rss/search?q=García+Nuevo+León+noticias&hl=es-419&gl=MX&ceid=MX:es-419"
        f = feedparser.parse(requests.get(url_rss, headers={'User-Agent':'Mozilla/5.0'}, timeout=10).content)
        for e in f.entries[:5]:
            noticias_html += f"""
            <div class="card mb-2 border-0 shadow-sm" style="border-radius:10px;">
                <div class="card-body py-2">
                    <span class="text-muted fw-bold" style="font-size:0.6rem;">{e.source.get('title', 'LOCAL')}</span>
                    <h6 class="mb-1 fw-bold" style="font-size:0.85rem;">{e.title}</h6>
                    <a href="{e.link}" target="_blank" class="small text-decoration-none fw-bold" style="font-size:0.75rem;">VER NOTA ORIGINAL →</a>
                </div>
            </div>"""
    except Exception as e:
        noticias_html = f"<p class='small text-muted'>Sincronizando feed de noticias... ({str(e)})</p>"

    # 3. Selección de portada y hora de Monterrey
    dest = random.choice(ARTICULOS_IA)
    ahora_mty = (datetime.utcnow() - timedelta(hours=6))
    hora_str = ahora_mty.strftime("%H:%M")
    timestamp_secreto = ahora_mty.strftime("%Y%m%d%H%M%S") # Para forzar a GitHub a ver cambios

    # 4. Generar el index.html
    full_index = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>InfoGarcía 24 | El portal de la industria</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background:#f0f2f5; font-family: sans-serif; }}
            .navbar {{ background: #002d5a; border-bottom: 3px solid #ff6600; }}
            .card-destacada {{ border-radius: 15px; overflow: hidden; border-left: 8px solid #dc3545; }}
        </style>
    </head>
    <body>
        <nav class="navbar py-2"><div class="container d-flex justify-content-between align-items-center">
            <span class="fw-bold text-white">INFO<span style="color:#ff6600;">GARCÍA</span>24</span>
            <span class="badge bg-danger animate-pulse">EN VIVO: {hora_str}</span>
        </div></nav>

        <div class="container py-4">
            <div class="row justify-content-center">
                <div class="col-md-6 col-lg-5">
                    <div class="card card-destacada mb-4 border-0 shadow-lg">
                        <img src="{dest['img']}" class="card-img-top" style="height:200px; object-fit:cover;">
                        <div class="card-body">
                            <span class="badge bg-danger mb-2">LO MÁS LEÍDO EN GARCÍA</span>
                            <h4 class="fw-bold" style="letter-spacing:-1px;">{dest['t']}</h4>
                            <p class="text-secondary small">{dest['d']}</p>
                            <a href="{dest['id']}.html" class="btn btn-danger w-100 fw-bold rounded-pill">ABRIR REPORTAJE COMPLETO</a>
                        </div>
                    </div>

                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h6 class="text-muted fw-bold mb-0">NOTICIAS LOCALES Y CLIMA</h6>
                        <hr class="flex-grow-1 ms-3">
                    </div>
                    {noticias_html}
                    
                    <div class="text-center mt-5 text-muted small">
                        <p>© 2026 InfoGarcía 24 - Periodismo de Datos Industrial<br>García, Nuevo León, México</p>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(full_index)

if __name__ == "__main__":
    build()
