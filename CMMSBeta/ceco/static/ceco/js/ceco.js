document.addEventListener("DOMContentLoaded", () => {
  const h1 = document.querySelector('#h1-remplazar');
  const filasTabla = document.querySelectorAll('#tabla-ceco tbody tr');
  const booton = document.getElementById('boton_secundario')
  const btnGuardarCambios = document.getElementById("guardar-cambios");
  const btnGuardarRegistro = document.getElementById("guardar-datos");
  const formEditar = document.getElementById("form-editar-ceco")
  const formRegistrar = document.getElementById("form-ceco")
  const btnEliminar = document.querySelectorAll('.eliminar');


  //Eventos

  setTimeout(function() {
      var mensaje = document.getElementById('mensaje');
      if (mensaje) {
          mensaje.style.display = 'none';
      }
  }, 3000);


  var editButtons = document.querySelectorAll('.editar');
  editButtons.forEach(function(button) {
      button.addEventListener('click', function() {
          var idCeco = this.dataset.idceco;
          var nombreCeco = this.dataset.nombrececo;
          document.getElementById("ceco_id").value = idCeco;
          document.getElementById("nombre_ceco").value = nombreCeco;
      });
  });

  btnEliminar.forEach(function(boton) {
    boton.addEventListener("click", function(event) {
      event.preventDefault();
      console.log("fgo,da")
      let cultivo = event.currentTarget.dataset.registro;
      let formId = event.currentTarget.dataset.id;
    console.log(cultivo, formId)
      PreguntarEliminar(cultivo, function() {
          document.getElementById('form-' + formId).submit();
      });
    });
  });

  btnGuardarRegistro.addEventListener("click", function(event){
    console.log("holsda")
    if (!formRegistrar.checkValidity()) {
      return;
    }
    event.preventDefault();
    PreguntarGuardar(function(){formRegistrar.submit();});

  });

  btnGuardarCambios.addEventListener("click", function(event){
    console.log("holsda")
    if (!formEditar.checkValidity()) {
      return;
    }
    event.preventDefault();
    PreguntarGuardar(function(){formEditar.submit();});

  });



});