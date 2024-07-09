function bienvenida(mensaje){
  const Toast = Swal.mixin({
    toast: true,
    position: 'top-end',
    showConfirmButton: false,
    timer: 2000,
    timerProgressBar: true,
    didOpen: (toast) => {
      toast.addEventListener('mouseenter', Swal.stopTimer)
      toast.addEventListener('mouseleave', Swal.resumeTimer)
    }
  })

  Toast.fire({
    icon: 'success',
    title: mensaje
  })
}

function notificar(icon,titulo, mensaje, tiempo){
  const nom_emp = "COMPUSERVIC TECNOLOGIA PERU";
  Swal.fire({
    icon: icon,
    title: titulo,
    text: mensaje,
    confirmButtonColor: '#2E86C1',
    confirmButtonText: 'Aceptar',
    footer: nom_emp,
    timerProgressBar: true,
    timer: (tiempo * 1000)
  })
}


function PreguntarGuardar(callback) {
  return Swal.fire({
    title: '¿Estás seguro de guardar el registro?',
    icon: 'question',
    showCancelButton: true,
    confirmButtonText: 'Aceptar',
    cancelButtonText: 'Cancelar',
    confirmButtonColor: '#2E86C1',
    cancelButtonColor: '#797D7F',
    }).then((result) => {
        if (result.isConfirmed) {
            callback()
        }
    });
}

function PreguntarEliminar(registro,callback) {
  return Swal.fire({
    title: `¿Estás seguro de eliminar ${registro} del registro?`,
    text: "Este procedimiento no se podrá revertir",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    cancelButtonText: "Cancelar",
    confirmButtonText: "Eliminarlo"
    }).then((result) => {
        if (result.isConfirmed) {
            callback()
        }
});
}

function PreguntarRegistrar(titulo, mensaje) {
  return Swal.fire({
    title: titulo,
    text: mensaje,
    icon: 'question',
    showCancelButton: true,
    confirmButtonText: 'Aceptar',
    cancelButtonText: 'Cancelar',
    confirmButtonColor: '#2E86C1',
    cancelButtonColor: '#797D7F',
    footer: 'Sistema'
  });
}

function PreguntarConfirmarLlegadss(titulo, mensaje) {
  return Swal.fire({
    title: titulo,
    text: mensaje,
    icon: 'question',
    showCancelButton: true,
    confirmButtonText: 'Aceptar',
    cancelButtonText: 'Cancelar',
    confirmButtonColor: '#2E86C1',
    cancelButtonColor: '#797D7F',
    footer: 'Sistema'
  });
}

function PreguntarConfirmarLlegada(callback) {
  return Swal.fire({
    title: '¿Estás seguro de eceptar el implemento?',
    icon: 'question',
    showCancelButton: true,
    confirmButtonText: 'Aceptar',
    cancelButtonText: 'Cancelar',
    confirmButtonColor: '#2E86C1',
    cancelButtonColor: '#797D7F',
    }).then((result) => {
        if (result.isConfirmed) {
            callback()
        }
    });
}