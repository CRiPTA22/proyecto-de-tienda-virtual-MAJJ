// 1. VARIABLES GLOBALES
let carrito = [];
let totalAcumulado = 0;

// 2. LÓGICA DE AGREGAR PRODUCTOS
document.querySelectorAll('.btn-agregar').forEach((boton) => {
    boton.addEventListener('click', (e) => {
        const btn = e.target;
        const tarjeta = btn.closest('.producto-item');
        const nombre = tarjeta.getAttribute('data-nombre');
        const precioTexto = tarjeta.querySelector('.text-primary').innerText;
        // Limpiamos el texto "$4.500.000" para que sea solo el número 4500000
        const precioNumerico = parseInt(precioTexto.replace(/[^0-9]/g, ""));

        // A. Guardar datos
        carrito.push({ nombre, precio: precioNumerico });
        totalAcumulado += precioNumerico;

        // B. Animación del botón (Interacción)
        const textoOriginal = btn.innerText;
        btn.innerText = "¡Añadido! ✓";
        btn.style.backgroundColor = "#28a745"; // Cambia a verde éxito temporalmente
        btn.disabled = true;

        // C. Animación de rebote en el carrito de la barra superior
        const iconoCarrito = document.querySelector('.btn-dark.position-relative');
        iconoCarrito.classList.add('animate__animated', 'animate__rubberBand');

        // Resetear efectos del botón e icono después de 1 segundo
        setTimeout(() => {
            btn.innerText = textoOriginal;
            btn.style.backgroundColor = ""; // Vuelve al azul oscuro del CSS
            btn.disabled = false;
            iconoCarrito.classList.remove('animate__rubberBand');
        }, 1000);

        // D. Actualizar todo
        actualizarCarritoUI();
        lanzarNotificacion(nombre);
    });
});

// 3. ACTUALIZAR LA INTERFAZ DEL CARRITO
function actualizarCarritoUI() {
    // Actualizar el numerito rojo
    document.getElementById('contador').innerText = carrito.length;

    const contenedorItems = document.getElementById('items-carrito');
    const visualTotal = document.getElementById('total-precio');

    if (carrito.length === 0) {
        contenedorItems.innerHTML = '<p class="text-center text-muted mt-5">Tu carrito está vacío.</p>';
    } else {
        contenedorItems.innerHTML = carrito.map((item, i) => `
            <div class="d-flex justify-content-between align-items-center mb-2 p-2 rounded animate__animated animate__fadeInRight" 
                 style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2)">
                <div style="font-size:0.85rem">
                    <p class="m-0 fw-bold">${item.nombre}</p>
                    <small class="text-info-custom">$${item.precio.toLocaleString()}</small>
                </div>
                <button class="btn btn-sm text-danger" onclick="eliminarProducto(${i})">✕</button>
            </div>
        `).join('');
    }

    visualTotal.innerText = `$${totalAcumulado.toLocaleString()}`;
}

// 4. LANZAR NOTIFICACIÓN (TOAST)
function lanzarNotificacion(nombre) {
    const area = document.getElementById('notificacion');
    const aviso = document.createElement('div');
    aviso.className = "alert alert-dark text-white shadow-lg border-0 mb-2 animate__animated animate__backInUp";
    aviso.style.background = "#003366";
    aviso.innerHTML = `✅ <b>${nombre}</b> agregado al carrito`;
    
    area.appendChild(aviso);

    setTimeout(() => {
        aviso.classList.replace('animate__backInUp', 'animate__backOutDown');
        setTimeout(() => aviso.remove(), 500);
    }, 2500);
}

// 5. BUSCADOR EN TIEMPO REAL
document.getElementById('buscador').addEventListener('keyup', (e) => {
    const busqueda = e.target.value.toLowerCase();
    document.querySelectorAll('.producto-item').forEach(prod => {
        const nombre = prod.getAttribute('data-nombre').toLowerCase();
        prod.style.display = nombre.includes(busqueda) ? "block" : "none";
    });
});

// 6. FILTROS POR CATEGORÍA
function filtrar(categoria) {
    // Actualizar botones de filtro
    document.querySelectorAll('.btn-filtro').forEach(b => b.classList.remove('active'));
    event.target.classList.add('active');

    document.querySelectorAll('.producto-item').forEach(prod => {
        const cat = prod.getAttribute('data-categoria');
        prod.style.display = (categoria === 'todos' || cat === categoria) ? "block" : "none";
    });
}

// 7. MOSTRAR/OCULTAR CARRITO LATERAL
function toggleCarrito() {
    const panel = document.getElementById('carrito-lateral');
    panel.style.display = (panel.style.display === 'none' || panel.style.display === '') ? 'block' : 'none';
}

// 8. ELIMINAR PRODUCTO
function eliminarProducto(indice) {
    totalAcumulado -= carrito[indice].precio;
    carrito.splice(indice, 1);
    actualizarCarritoUI();
}