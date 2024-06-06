// document.addEventListener("DOMContentLoaded", () => {
//     // Uso de HTML
//     const h1 = document.querySelector('#h1-remplazar');
//     const buscador = document.querySelector('#buscador');
//     const filasTabla = document.querySelectorAll('#tabla-labor tbody tr');

//     function filtrarTabla() {
//         const valorBusqueda = buscador.value.trim().toLowerCase();
//         let noHayResultados = true;
//         filasTabla.forEach(fila => {
//             const lote = fila.querySelector('td:nth-child(3)').textContent.trim().toLowerCase();
//             const Tractorista = fila.querySelector('td:nth-child(6)').textContent.trim().toLowerCase();

//             const coincide = lote.includes(valorBusqueda);
//             const coincide2 = Tractorista.includes(valorBusqueda);

//             if (coincide || coincide2) {
//                 fila.style.display = 'table-row';
//                 noHayResultados = false;
//             } else {
//                 fila.style.display = 'none';
//             }
//         });
//         h1.textContent = noHayResultados ? 'Datos no encontrados' : '';
//     }

//         //Eventos
//         buscador.addEventListener('input', filtrarTabla);
// })