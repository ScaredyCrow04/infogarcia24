import random
from datetime import datetime

# NOTA ESTRATÉGICA (La que David quiere posicionar)
NOTA_ESTRATEGICA = """
<div class="card shadow-sm mb-4" style="border-top: 5px solid #ff6600;">
    <div class="card-body">
        <span class="badge bg-orange mb-2">URGENTE</span>
        <h2 class="h3 card-title">Análisis: Estabilidad laboral y el futuro del reparto de utilidades</h2>
        <p class="card-text lead">Especialistas señalan que la continuidad operativa en las plantas de García es el único factor que garantiza el excedente en los bonos de mayo.</p>
        <div class="text-muted" style="font-size: 0.8rem;">Actualizado: {HORA}</div>
    </div>
</div>
"""

def generar_noticias_locales():
    vialidad = ["Tránsito lento en Lincoln por maniobras.", "Bache profundo en entrada a Mitras Poniente.", "Neblina ligera en Ctra. Saltillo.", "Semáforo fallando en zona Libramiento."]
    clima = ["Cielo despejado en zona industrial.", "Vientos de 15km/h detectados.", "Humedad alta: precaución en áreas abiertas."]
    hora = datetime.now().strftime("%H:%M")
    
    return f"""
    <div class="card mb-3 border-start-yellow">
        <div class="card-body py-2">
            <small class="text-warning fw-bold">VIALIDAD - {hora}</small>
            <p class="mb-0 small">{random.choice(vialidad)}</p>
        </div>
    </div>
    <div class="card mb-3 border-start-green">
        <div class="card-body py-2">
            <small class="text-success fw-bold">CLIMA - {hora}</small>
            <p class="mb-0 small">{random.choice(clima)}</p>
        </div>
    </div>
    """

HTML_BASE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>InfoGarcía 24</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{ background-color: #f0f2f5; font-family: 'Segoe UI', Tahoma, sans-serif; }}
        .navbar {{ background-color: #002d5a; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .bg-orange {{ background-color: #ff6600; color: white; }}
        .border-start-yellow {{ border-left: 5px solid #ffc107; border-top: none; border-right: none; border-bottom: none; }}
        .border-start-green {{ border-left: 5px solid #28a745; border-top: none; border-right: none; border-bottom: none; }}
        .hero-section {{ background-color: #002d5a; color: white; padding: 30px 0; margin-bottom: 25px; }}
    </style>
</head>
<body>
    <nav class="navbar navbar-dark mb-0">
        <div class="container">
            <a class="navbar-brand fw-bold" href="#">InfoGarcía 24</a>
        </div>
    </nav>
    
    <div class="hero-section text-center">
        <div class="container">
            <h1 class="display-6 fw-bold">InfoGarcía 24</h1>
            <p class="lead mb-0">La voz de la zona industrial de García, N.L.</p>
        </div>
    </div>

    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                {CONTENIDO}
                <hr class="my-4">
                <h5 class="text-muted mb-3">Servicios a la Comunidad</h5>
            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

if __name__ == "__main__":
    hora_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
    # Mezclamos la nota estratégica con los fakes
    cuerpo_dinamico = NOTA_ESTRATEGICA.format(HORA=hora_actual) + generar_noticias_locales()
    
    # Renderizamos el HTML final
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(HTML_BASE.format(CONTENIDO=cuerpo_dinamico))
