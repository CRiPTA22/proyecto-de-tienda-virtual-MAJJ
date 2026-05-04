# Marketplace JMJ — Flask + Python

## Estructura del proyecto

```
marketplace/
├── app.py                    ← Servidor Flask (lógica principal)
├── templates/
│   ├── index.html            ← Página principal con todos los productos
│   └── producto.html         ← Página de detalle de cada producto
└── static/
    ├── css/
    │   └── estilos.css       ← Estilos personalizados
    ├── js/
    │   └── script.js         ← Carrito, filtros, buscador
    └── img/
        ├── iphone.jpg
        ├── samsung.jpg
        ├── xiaomi.jpg
        ├── rtx4060.jpg
        ├── ram.jpg
        ├── tv-lg.jpg
        └── sonido-sony.jpg
```

## Cómo correr el proyecto

### 1. Instalar Flask (solo una vez)
```bash
pip install flask
```

### 2. Entrar a la carpeta del proyecto
```bash
cd marketplace
```

### 3. Correr la aplicación
```bash
python app.py
```

### 4. Abrir en el navegador
```
http://localhost:5000
```

## Funcionalidades

- Catálogo de productos con tus imágenes reales
- Filtro por categorías: Celulares, Hardware, TV, Sonido
- Buscador en tiempo real
- Carrito lateral con animaciones
- Notificaciones al agregar productos
- Página de detalle por producto con descripción, calificación y reseñas
- Formulario para dejar comentarios (funciona de verdad)
- Diseño responsive

## Agregar más productos

En `app.py` agrega un elemento a la lista `productos`:

```python
{
    "id": 8,
    "nombre": "Nombre del producto",
    "precio": 1500000,
    "imagen": "nombre-imagen.jpg",     # ← Pon la imagen en static/img/
    "categoria": "celular",            # celular | hardware | tv | sonido
    "descripcion": "Descripción...",
    "calificacion": 4.5,
    "num_resenas": 200,
    "comentarios": []
}
```
