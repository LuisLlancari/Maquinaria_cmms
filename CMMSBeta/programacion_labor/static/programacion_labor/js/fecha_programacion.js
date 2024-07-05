document.addEventListener('DOMContentLoaded', function() {
    // Incluye la biblioteca luxon
    const { DateTime } = luxon;

    // MANEJO DE FECHAS

    // Configura la zona horaria de Perú
    const zonaHorariaPeru = 'America/Lima';

    // Obtén la fecha y hora actual en la zona horaria de Perú
    let fechaActual = DateTime.now().setZone(zonaHorariaPeru);
    let fechaMañana = fechaActual.plus({ days: 1 });


    //PROGRAMACION LABOR
    // Formatea las fechas en el formato 'yyyy-MM-dd'
    let hoy = fechaActual.toFormat('yyyy-MM-dd');
    let mañana = fechaMañana.toFormat('yyyy-MM-dd');

    // Asigna los valores a las opciones del select
    let option_1 = document.getElementById('1');
    let option_2 = document.getElementById('2');

    option_1.value = hoy;
    option_1.innerHTML = `HOY - ${hoy}`;
    option_2.value = mañana;
    option_2.innerHTML = `MAÑANA - ${mañana}`;

    let filtro = document.getElementById('filtro');
    filtro.value = hoy;

    // Funcion para filtrar las filas de la tabla
    filtro.addEventListener('change', function() {
        let selectedDate = filtro.value; // 'yyyy-MM-dd'
        let filas = document.querySelectorAll('#tabla-labor tbody tr');
        let no_resultado = document.getElementById('no_resultado');
        let resultado = false;

        filas.forEach(fila => {
            let fechaCelda = DateTime.fromFormat(fila.querySelector('.fecha').textContent.trim(), 'dd-MM-yyyy').toFormat('yyyy-MM-dd');
            if (fechaCelda === selectedDate) {
                fila.style.display = '';
                resultado = true;
            } else {
                fila.style.display = 'none';
            }
        });

        no_resultado.style.display = resultado ? 'none' : 'block';
    });

    // Ejecutar el filtro al cargar la página
    filtro.dispatchEvent(new Event('change'));
});
