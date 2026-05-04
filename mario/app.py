from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json

app = Flask(__name__)
app.secret_key = "marketplace_jmj_2025"

productos = [
    {
        "id": 1,
        "nombre": "iPhone 15 Pro",
        "precio": 3500000,
        "imagen": "iphone.jpg",
        "categoria": "celular",
        "descripcion": "Chip A17 Pro, cámara de 48 MP con zoom óptico 5x, pantalla Super Retina XDR de 6.1\", titanio grado aeroespacial y batería de todo el día.",
        "calificacion": 4.8,
        "num_resenas": 2,
        "comentarios": [
            {"usuario": "Juliana R.", "estrellas": 5, "texto": "El mejor iPhone que he tenido. La cámara es increíble y el titanio se siente premium.", "fecha": "2 Abr 2025"},
            {"usuario": "Felipe M.", "estrellas": 5, "texto": "Rapidísimo y la duración de batería mejoró mucho. Vale cada peso.", "fecha": "15 Mar 2025"},
        ]
    },
    {
        "id": 2,
        "nombre": "Samsung S24 Ultra",
        "precio": 3800000,
        "imagen": "samsung.jpg",
        "categoria": "celular",
        "descripcion": "Pantalla Dynamic AMOLED 2X de 6.8\", S Pen integrado, cámara de 200 MP, chip Snapdragon 8 Gen 3 y batería de 5000 mAh con carga de 45W.",
        "calificacion": 4.7,
        "num_resenas": 2,
        "comentarios": [
            {"usuario": "Camila T.", "estrellas": 5, "texto": "El S Pen es una maravilla para tomar notas. La pantalla es simplemente espectacular.", "fecha": "1 Abr 2025"},
            {"usuario": "Andrés B.", "estrellas": 4, "texto": "Excelente teléfono, un poco grande pero la cámara de 200MP no tiene competencia.", "fecha": "20 Mar 2025"},
        ]
    },
    {
        "id": 3,
        "nombre": "Xiaomi Redmi Note 13",
        "precio": 800000,
        "imagen": "xiaomi.jpg",
        "categoria": "celular",
        "descripcion": "Pantalla AMOLED 120Hz de 6.67\", triple cámara de 108 MP, procesador Snapdragon 685, carga rápida de 33W y batería de 5000 mAh. La mejor relación calidad-precio.",
        "calificacion": 4.5,
        "num_resenas": 2,
        "comentarios": [
            {"usuario": "Valentina S.", "estrellas": 5, "texto": "Por este precio no existe nada mejor. La pantalla AMOLED es hermosa y la cámara sorprende.", "fecha": "10 Abr 2025"},
            {"usuario": "Daniel C.", "estrellas": 4, "texto": "Muy bueno para el precio. La carga rápida es una ventaja enorme en el día a día.", "fecha": "28 Mar 2025"},
        ]
    },
    {
        "id": 4,
        "nombre": "NVIDIA RTX 4060 Ti",
        "precio": 2950000,
        "imagen": "rtx4060.jpg",
        "categoria": "hardware",
        "descripcion": "GPU con 8GB GDDR6, arquitectura Ada Lovelace, DLSS 3, Ray Tracing en tiempo real. Ideal para gaming 1080p/1440p y creación de contenido con rendimiento excepcional.",
        "calificacion": 4.6,
        "num_resenas": 2,
        "comentarios": [
            {"usuario": "Santiago G.", "estrellas": 5, "texto": "Juego todos los títulos AAA en Ultra 1440p sin problemas. El DLSS 3 es un game changer.", "fecha": "5 Abr 2025"},
            {"usuario": "Nicolás V.", "estrellas": 4, "texto": "Excelente rendimiento. Solo le quito una estrella porque el precio sigue siendo alto.", "fecha": "18 Mar 2025"},
        ]
    },
    {
        "id": 5,
        "nombre": "RAM 16GB DDR4 RGB",
        "precio": 480000,
        "imagen": "ram.jpg",
        "categoria": "hardware",
        "descripcion": "Kit de 16GB DDR4 a 3200MHz con iluminación RGB personalizable. Compatible con AMD y Intel. Incluye disipador de aluminio de alto rendimiento para temperatura óptima.",
        "calificacion": 4.4,
        "num_resenas": 2,
        "comentarios": [
            {"usuario": "Laura P.", "estrellas": 5, "texto": "El RGB es hermoso y la velocidad mejoró notablemente mi PC. Instalación sencilla.", "fecha": "8 Abr 2025"},
            {"usuario": "Esteban M.", "estrellas": 4, "texto": "Buena memoria, compatible con mi placa Gigabyte sin ningún problema de configuración.", "fecha": "25 Mar 2025"},
        ]
    },
    {
        "id": 6,
        "nombre": "LG Smart TV 55\"",
        "precio": 3800000,
        "imagen": "tv-lg.jpg",
        "categoria": "tv",
        "descripcion": "Smart TV 4K UHD de 55 pulgadas con webOS, HDR10, Dolby Vision, procesador α5 Gen6, ThinQ AI y compatibilidad con Google Assistant y Alexa. 4 puertos HDMI.",
        "calificacion": 4.8,
        "num_resenas": 2,
        "comentarios": [
            {"usuario": "Mariana L.", "estrellas": 5, "texto": "La imagen es impresionante. El webOS es muy fluido y tiene todas las apps que necesito.", "fecha": "3 Abr 2025"},
            {"usuario": "Carlos E.", "estrellas": 5, "texto": "Dolby Vision hace una diferencia enorme al ver películas. El sonido también es muy bueno.", "fecha": "15 Mar 2025"},
        ]
    },
    {
        "id": 7,
        "nombre": "Sony High Power MHC-V83D",
        "precio": 2100000,
        "imagen": "sonido-sony.jpg",
        "categoria": "sonido",
        "descripcion": "Torre de sonido de 1200W con subwoofer integrado, luces LED multicolor, Bluetooth 5.0, karaoke con 2 micrófonos inalámbricos, entrada USB y radio FM. La fiesta perfecta.",
        "calificacion": 4.7,
        "num_resenas": 2,
        "comentarios": [
            {"usuario": "Isabella R.", "estrellas": 5, "texto": "El sonido llena toda la casa y los vecinos lo escuchan. Las luces son espectaculares.", "fecha": "7 Abr 2025"},
            {"usuario": "Mateo A.", "estrellas": 5, "texto": "La usamos en el cumpleaños y fue un éxito total. El karaoke es increíble.", "fecha": "1 Abr 2025"},
        ]
    },
]

@app.route("/")
def index():
    busqueda = request.args.get("q", "").lower()
    categoria = request.args.get("categoria", "todos")
    resultado = productos
    if busqueda:
        resultado = [p for p in resultado if busqueda in p["nombre"].lower() or busqueda in p["descripcion"].lower()]
    if categoria != "todos":
        resultado = [p for p in resultado if p["categoria"] == categoria]
    return render_template("index.html", productos=resultado, categoria_actual=categoria, busqueda=busqueda)

@app.route("/producto/<int:id>")
def producto(id):
    p = next((p for p in productos if p["id"] == id), None)
    if not p:
        return redirect(url_for("index"))
    return render_template("producto.html", producto=p)

@app.route("/comentar/<int:id>", methods=["POST"])
def comentar(id):
    p = next((p for p in productos if p["id"] == id), None)
    if p:
        nuevo = {
            "usuario": request.form.get("usuario", "Anónimo"),
            "estrellas": int(request.form.get("estrellas", 5)),
            "texto": request.form.get("texto", ""),
            "fecha": "Hoy"
        }
        if nuevo["texto"].strip():
            p["comentarios"].insert(0, nuevo)
    return redirect(url_for("producto", id=id))

if __name__ == "__main__":
    app.run(debug=True)
