import random
from datetime import datetime

# NOTA ESTRATÉGICA (El "Humo" para David)
NOTA_ESTRATEGICA = """
<div class="card-noticia" style="border-top: 5px solid #ff6600;">
    <span class="badge-alerta">URGENTE</span>
    <h2 class="mt-3">Análisis: Estabilidad laboral y el futuro del reparto de utilidades</h2>
    <p class="lead">Especialistas señalan que la continuidad operativa en las plantas de García es el único factor que garantiza el excedente en los bonos de mayo.</p>
    <small class="text-muted">Actualizado: {HORA}</small>
</div>
"""

def generar_noticias_locales():
    vialidad = ["Tránsito lento en Lincoln.", "Bache profundo en Mitras Poniente.", "Neblina en Ctra. Saltillo.", "Semáforo fallando en Libramiento."]
    clima = ["Cielo despejado en zona industrial.", "Vientos de 15km/h.", "Humedad alta detectada."]
    hora = datetime.now().strftime("%H:%M")
    return f"""
    <div class="card-noticia" style="border-left: 5px solid #ffc107;">
        <small class="text-warning fw-bold">VIALIDAD - {hora}</small>
        <p>{random.choice(vialidad)}</p>
    </div>
    <div class="card-noticia" style="border-left: 5px solid #28a745;">
        <small class="text-success fw-bold">CLIMA - {hora}</small>
        <p>{random.choice(clima)}</p>
    </div>"""

HTML_BASE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>InfoGarcía 24</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <style>
        body {{ background-color: #f4f7f6; font-family: sans-serif; }}
        .navbar {{ background-color: #002d5a; }}
        .hero {{ background-color: #002d5a; color: white; padding: 40px 0; text-align: center; }}
        .card-noticia {{ border: none; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-bottom: 20px; padding: 25px; background: white; border-radius: 8px; }}
        .badge-alerta {{ background-color: #ff6600; color: white; padding: 5px 12px; border-radius: 4px; font-weight: bold; font-size: 0.75rem; }}
    </style>
</head>
<body>
    <nav class="navbar navbar-dark p-3"><div class="container"><a class="navbar-brand" href="#">InfoGarcía 24</a></div></nav>
    <div class="hero"><h1>InfoGarcía 24</h1><p>La voz de la zona industrial de García, N.L.</p></div>
    <div class="container mt-4"><div class="row justify-content-center"><div class="col-md-9">
        {{CONTENIDO}}
    </div></div></div>
</body>
</html>
"""

if __name__ == "__main__":
    hora_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
    cuerpo = NOTA_ESTRATEGICA.format(HORA=hora_actual) + generar_noticias_locales()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(HTML_BASE.replace("{{CONTENIDO}}", cuerpo))
