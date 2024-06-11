document.addEventListener("DOMContentLoaded", () => {
  const h1 = document.querySelector('#h1-remplazar');
  const buscador = document.querySelector('#buscador');
  const filasTabla = document.querySelectorAll('#tabla-ceco tbody tr');
  const booton = document.getElementById('boton_secundario')

  //Funciones
  function filtrarTabla() {
      const valorBusqueda = buscador.value.trim().toLowerCase();
      let noHayResultados = true;
      filasTabla.forEach(fila => {
          const ceco = fila.querySelector('td:nth-child(2)').textContent.trim().toLowerCase();
          const coincide = ceco.includes(valorBusqueda);

          if (coincide) {
              fila.style.display = 'table-row';
              noHayResultados = false;
          } else {
              fila.style.display = 'none';
          }
      });
      h1.textContent = noHayResultados ? 'Datos no encontrados' : '';
  }

  //Eventos
  buscador.addEventListener('input', filtrarTabla);

  setTimeout(function() {
      var mensaje = document.getElementById('mensaje');
      if (mensaje) {
          mensaje.style.display = 'none';
      }
  }, 3000);

  booton.addEventListener('click', function(){
      console.log('hola')
  });

  var editButtons = document.querySelectorAll('.editar');
  editButtons.forEach(function(button) {
      button.addEventListener('click', function() {
          console.log("hola")
          var idCeco = this.dataset.idceco;
          var nombreCeco = this.dataset.nombrececo;
          document.getElementById("ceco_id").value = idCeco;
          document.getElementById("nombre_ceco").value = nombreCeco;
      });
  });



});