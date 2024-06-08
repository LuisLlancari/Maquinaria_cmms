document.addEventListener('DOMContentLoaded', function() {
    // Incluye la biblioteca luxon
    const { DateTime } = luxon;

    // MANEJO DE FECHAS

    // Configura la zona horaria de Perú
    const zonaHorariaPeru = 'America/Lima';

    // Obtén la fecha y hora actual en la zona horaria de Perú
    let fechaActual = DateTime.now().setZone(zonaHorariaPeru);
    let fechaMañana = fechaActual.plus({ days: 1 });
    let fechaAyer = fechaActual.plus({ days: -1 });


    //PROGRAMACION LABOR
    // Formatea las fechas en el formato 'yyyy-MM-dd'
    let hoy = fechaActual.toFormat('yyyy-MM-dd');
    let mañana = fechaMañana.toFormat('yyyy-MM-dd');
    
    let hoy_filtro = fechaActual.toFormat('dd-MM-yyyy');
    let mañana_filtro = fechaMañana.toFormat('dd-MM-yyyy');
    let ayer_filtrar = fechaAyer.toFormat('dd-MM-yyyy');

    // Asigna los valores a las opciones del select
    let selectFecha = document.getElementById('id_fechahora');
    let option_1 = document.getElementById('1');
    let option_2 = document.getElementById('2');

    option_1.value = hoy;
    option_1.innerHTML = `HOY - ${hoy}`;
    option_2.value = mañana;
    option_2.innerHTML = `MAÑANA - ${mañana}`;

    let filtro_hoy = document.getElementById('filtro_hoy');
    let filtro_manana = document.getElementById('filtro_manana');
    let filtro_ayer = document.getElementById('filtro_ayer');

    filtro_hoy.value = hoy_filtro;
    filtro_manana.value = mañana_filtro;
    filtro_ayer.value = ayer_filtrar;

    let filtro = document.getElementById('filtro');
    filtro.value = hoy_filtro;

    selectFecha.addEventListener('change', () => {
        let seleccion = selectFecha.value;
    });

    // Funcion para filtrar las filas de la tabla
    filtro.addEventListener('change', function() {
        let selectedDate = filtro.value;
        let filas = document.querySelectorAll('#tabla-labor tbody tr');
        let no_resultado = document.getElementById('no_resultado');
        let resultado = false;

        filas.forEach(fila => {
            let fechaCelda = fila.querySelector('.fecha').textContent.trim();
            if (fechaCelda === selectedDate) {
                fila.style.display = '';
                resultado = true;
            } else {
                fila.style.display = 'none';
            }
        });

        if (!resultado) {
            no_resultado.style.display = 'block';
        } else {
            no_resultado.style.display = 'none';
        }
    });

    // Ejecutar el filtro al cargar la página
    filtro.dispatchEvent(new Event('change'));
});
