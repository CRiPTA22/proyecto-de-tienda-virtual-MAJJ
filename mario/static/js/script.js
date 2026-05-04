let carrito = [];
let totalAcumulado = 0;

// AGREGAR AL CARRITO
document.querySelectorAll('.btn-agregar').forEach((boton) => {
    boton.addEventListener('click', (e) => {
        const btn = e.currentTarget;
        const nombre = btn.dataset.nombre;
        const precio = parseInt(btn.dataset.precio);

        carrito.push({ nombre, precio });
        totalAcumulado += precio;

        // Animación botón
        const textoOriginal = btn.innerText;
        btn.innerText = "¡Añadido! ✓";
        btn.style.backgroundColor = "#28a745";
        btn.disabled = true;

        // Rebote en el ícono del carrito
        const iconoCarrito = document.querySelector('#btn-carrito-nav');
        if (iconoCarrito) {
            iconoCarrito.classList.add('animate__animated', 'animate__rubberBand');
        }

        setTimeout(() => {
            btn.innerText = textoOriginal;
            btn.style.backgroundColor = "";
            btn.disabled = false;
            if (iconoCarrito) iconoCarrito.classList.remove('animate__rubberBand');
        }, 1000);

        actualizarCarritoUI();
        lanzarNotificacion(nombre);
    });
});

// BOTÓN AGREGAR EN PÁGINA DE DETALLE
const btnCarritoProd = document.getElementById('btn-carrito-producto');
if (btnCarritoProd) {
    btnCarritoProd.addEventListener('click', () => {
        const nombre = btnCarritoProd.dataset.nombre;
        const precio = parseInt(btnCarritoProd.dataset.precio);
        carrito.push({ nombre, precio });
        totalAcumulado += precio;
        actualizarCarritoUI();
        lanzarNotificacion(nombre);

        btnCarritoProd.textContent = "¡Añadido! ✓";
        btnCarritoProd.style.background = "#28a745";
        btnCarritoProd.style.color = "white";
        btnCarritoProd.style.borderColor = "#28a745";
        setTimeout(() => {
            btnCarritoProd.textContent = "🛒 Agregar al carrito";
            btnCarritoProd.style.background = "";
            btnCarritoProd.style.color = "";
            btnCarritoProd.style.borderColor = "";
        }, 1200);
    });
}

// ACTUALIZAR UI DEL CARRITO
function actualizarCarritoUI() {
    const contador = document.getElementById('contador');
    if (contador) contador.innerText = carrito.length;

    const contenedor = document.getElementById('items-carrito');
    const totalEl = document.getElementById('total-precio');

    if (!contenedor) return;

    if (carrito.length === 0) {
        contenedor.innerHTML = '<p class="text-center text-white-50 mt-5">Tu carrito está vacío.</p>';
    } else {
        contenedor.innerHTML = carrito.map((item, i) => `
            <div class="item-carrito">
                <div style="font-size:0.85rem; flex:1;">
                    <p class="m-0 fw-bold">${item.nombre}</p>
                    <small class="text-info-custom">$${item.precio.toLocaleString('es-CO')}</small>
                </div>
                <button class="btn btn-sm text-danger p-0 ms-2" onclick="eliminarProducto(${i})" title="Eliminar">✕</button>
            </div>
        `).join('');
    }

    if (totalEl) totalEl.innerText = `$${totalAcumulado.toLocaleString('es-CO')}`;
}

// NOTIFICACIÓN TOAST
function lanzarNotificacion(nombre) {
    const area = document.getElementById('notificacion');
    if (!area) return;
    const aviso = document.createElement('div');
    aviso.className = "toast-item";
    aviso.innerHTML = `✅ <b>${nombre}</b> agregado al carrito`;
    area.appendChild(aviso);
    setTimeout(() => {
        aviso.style.opacity = '0';
        aviso.style.transition = 'opacity 0.4s';
        setTimeout(() => aviso.remove(), 400);
    }, 2500);
}

// BUSCADOR EN TIEMPO REAL
const buscador = document.getElementById('buscador');
if (buscador) {
    buscador.addEventListener('keyup', (e) => {
        const q = e.target.value.toLowerCase();
        document.querySelectorAll('.producto-item').forEach(prod => {
            const nombre = prod.getAttribute('data-nombre').toLowerCase();
            prod.style.display = nombre.includes(q) ? "block" : "none";
        });
    });
}

// FILTROS POR CATEGORÍA
function filtrar(categoria, el) {
    document.querySelectorAll('.btn-filtro').forEach(b => b.classList.remove('active'));
    if (el) el.classList.add('active');

    document.querySelectorAll('.producto-item').forEach(prod => {
        const cat = prod.getAttribute('data-categoria');
        prod.style.display = (categoria === 'todos' || cat === categoria) ? "block" : "none";
    });
}

// TOGGLE CARRITO LATERAL
function toggleCarrito() {
    const panel = document.getElementById('carrito-lateral');
    if (!panel) return;
    const visible = panel.style.display === 'block';
    panel.style.display = visible ? 'none' : 'block';
}

// ELIMINAR PRODUCTO
function eliminarProducto(indice) {
    totalAcumulado -= carrito[indice].precio;
    carrito.splice(indice, 1);
    actualizarCarritoUI();
}
