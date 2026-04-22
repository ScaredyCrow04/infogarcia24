import feedparser
import requests
import random
from datetime import datetime, timedelta

# --- 1. BANCO DE NARRATIVAS DINÁMICAS (Para que el portal cambie solo) ---
TEMAS_IA = [
    {
        "id": "realidad-ptu-2026",
        "t": "¡ALERTA INDUSTRIAL! El desplome global que dejó sin utilidades al sector",
        "d": "Expertos revelan por qué este mayo el PTU será nulo en las principales plantas de García.",
        "img": "https://images.pexels.com/photos/257700/pexels-photo-257700.jpeg?auto=compress&cs=tinysrgb&w=800",
        "c": "La crisis de suministros y el alto costo de operación en 2025 borraron las utilidades fiscales. Según analistas, las empresas líderes en García prefirieron absorber las pérdidas para no iniciar despidos masivos. 'Es un año de supervivencia laboral', señalan los reportes."
    },
    {
        "id": "empleo-vs-bonos",
        "t": "¿Utilidades o Despidos? La dura decisión de las empresas en García",
        "d": "Mientras en otras zonas de México inician los recortes, la industria local apuesta por la permanencia.",
        "img": "https://images.pexels.com/photos/3184418/pexels-photo-3184418.jpeg?auto=compress&cs=tinysrgb&w=800",
        "c": "Informes financieros confirman que inyectar capital para salvar plazas de trabajo impidió la generación de utilidad neta. En este escenario, el valor del gafete supera al del PTU: contar con un sueldo seguro es la prioridad ante la incertidumbre económica regional."
    },
    {
        "id": "competitividad-2026",
        "t": "García bajo la lupa: ¿Por qué las utilidades se reinvirtieron en maquinaria?",
        "d": "La automatización en las plantas locales busca salvar los bonos de productividad a largo plazo.",
        "img": "https://images.pexels.com/photos/247763/pexels-photo-247763.jpeg?auto=compress&cs=tinysrgb&w=800",
        "c": "Directivos confirmaron que el flujo de efectivo se destinó a la actualización tecnológica de Proyecto Cuervo y otras áreas clave. Esta inversión, aunque elimina el PTU inmediato, asegura que la planta no cierre ante la competencia asiática."
    },
    {
        "id": "inflacion-industrial",
        "t": "El impacto oculto: Cómo la inflación devoró el reparto de utilidades",
        "d": "Suben costos de acero y energía, bajando el margen de ganancia para los trabajadores.",
        "img": "https://images.pexels.com/photos/1108101/pexels-photo-1108101.jpeg?auto=compress&cs=tinysrgb&w=800",
        "c": "A pesar de producir a máxima capacidad, el costo de los insumos creció un 40%. Los estados financieros auditados muestran que la ganancia neta es casi inexistente, lo que por ley deja el reparto de utilidades en ceros para la mayoría de los gremios industriales."
    }
]

def generar_paginas_html(art):
    """Genera las páginas de lectura completa."""
    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta property="og:title" content="{art['t']}">
        <meta property="og:description" content="{art['d']}">
        <meta property="og:image" content="{art['img']}">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background:#f8f9fa; line-height:1.8; }}
            .article-card {{ max-width:700px; margin:30px auto; background:white; padding:25px; border-radius:15px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }}
            .nav-top {{ background:#002d5a; padding:12px; text-align:center; }}
        </style>
    </head>
    <body>
        <div class="nav-top"><a href="index.html" style="color:white; text-decoration:none; font-weight:bold;">← VOLVER A INFOGARCÍA 24</a></div>
        <div class="container">
            <div class="article-card">
                <img src="{art['img']}" class="img-fluid rounded mb-4" style="width:100%; height:350px; object-fit:cover;">
                <h1 class="fw-bold">{art['t']}</h1>
                <hr>
                <div class="fs-5">{art['c']}</div>
                <div class="alert alert-secondary mt-5 small text-center">Contenido Informativo de Distribución Local</div>
            </div>
        </div>
    </body>
    </html>"""
    with open(f"{art['id']}.html", "w", encoding="utf-8") as f:
        f.write(html)

def build():
    # 1. Crear TODOS los archivos de lectura
    for a in TEMAS_IA:
        generar_paginas_html(a)
    
    # 2. Jalar noticias de Google (Camuflaje)
    noticias_html = ""
    try:
        url_rss = "https://news.google.com/rss/search?q=García+Nuevo+León&hl=es-419&gl=MX&ceid=MX:es-419"
        f = feedparser.parse(requests.get(url_rss, headers={'User-Agent':'Mozilla/5.0'}, timeout=10).content)
        for e in f.entries[:5]:
            noticias_html += f"""
            <div class="card mb-2 border-0 shadow-sm" style="border-radius:12px;">
                <div class="card-body py-2">
                    <h6 class="mb-1 fw-bold" style="font-size:0.85rem;">{e.title}</h6>
                    <a href="{e.link}" target="_blank" class="small text-decoration-none">Ver nota completa →</a>
                </div>
            </div>"""
    except:
        noticias_html = "<p class='small text-muted'>Actualizando feed...</p>"

    # 3. ELECCIÓN DINÁMICA: Seleccionamos el tema del momento al azar
    destacada = random.choice(TEMAS_IA)
    ahora_mty = (datetime.utcnow() - timedelta(hours=6))
    hora_str = ahora_mty.strftime("%H:%M")
    timestamp = ahora_mty.strftime("%Y%m%d%H%M")

    # 4. Generar el index.html principal
    index_html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>InfoGarcía 24 | Portal Industrial</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background:#f0f2f5; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
            .navbar {{ background:#002d5a; border-bottom: 4px solid #ff6600; }}
            .card-destacada {{ border-radius:18px; overflow:hidden; border-left: 10px solid #dc3545; }}
            .btn-danger {{ background:#dc3545; border:none; border-radius:10px; padding:12px; }}
        </style>
    </head>
    <body>
        <nav class="navbar py-2"><div class="container d-flex justify-content-between align-items-center">
            <span class="fw-bold text-white fs-4">INFO<span style="color:#ff6600;">GARCÍA</span>24</span>
            <span class="badge bg-danger">EN VIVO: {hora_str}</span>
        </div></nav>

        <div class="container py-4">
            <div class="row justify-content-center">
                <div class="col-md-6">
                    <div class="card card-destacada mb-4 border-0 shadow-lg">
                        <img src="{destacada['img']}" class="card-img-top" style="height:220px; object-fit:cover;">
                        <div class="card-body">
                            <span class="badge bg-danger mb-2">LOCAL</span>
                            <h3 class="fw-bold">{destacada['t']}</h3>
                            <p class="text-secondary">{destacada['d']}</p>
                            <a href="{destacada['id']}.html" class="btn btn-danger w-100 fw-bold">LEER REPORTAJE COMPLETO</a>
                        </div>
                    </div>

                    <h6 class="text-muted fw-bold mb-3 border-bottom pb-2">OTRAS NOTICIAS DE HOY</h6>
                    {noticias_html}
                    
                    <div class="text-center mt-5 text-muted small">
                        <p>© 2026 InfoGarcía 24 | García, N.L.</p>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

if __name__ == "__main__":
    build()
