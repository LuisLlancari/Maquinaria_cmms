document.addEventListener("DOMContentLoaded", () => {    
    
    const form = document.getElementById('form_programacion');
    // HACEMOS EL TRUCO NAZHEE
    function obtener_data_select(fecha, turno) {
        const usu_login = document.getElementById('usu_login').value;
        
        //CAMBIA EL VALOR POR QUE SE ENCUENTRA LOGUEADO
        const usuario_id = document.getElementById('usuario_id');

        usuario_id.value = usu_login;
        
        usuario_id_2.value = usu_login;
        usuario_id_3.value = usu_login;
        //id_turno.value = 'M';
        // Referencia al select de limpiamos y creamos
        id_idtractorista.innerHTML = '';
        id_idtractorista.innerHTML = '<option value="">---------</option>';
        id_idtractor.innerHTML = '';
        id_idtractor.innerHTML = '<option value="">---------</option>';
        id_idimplemento.innerHTML = '';
        id_idimplemento.innerHTML = '<option value="">---------</option>';


        fetch(`./obtener_select/${fecha}/${turno}`)
        .then(res => res.json())
        .then(dataRecibida => {
            
            // Referencia al select de tractoristas
            const selectTractorista = document.getElementById('id_idtractorista');
            const selectTractor = document.getElementById('id_idtractor');
            const selectImplemento = document.getElementById('id_idimplemento');

            // Verificar si hay tractoristas disponibles y agregarlos al select
            if (dataRecibida.tractoristas && dataRecibida.tractoristas.length > 0) {
                dataRecibida.tractoristas.forEach(tractorista => {
                    let option = document.createElement('option');
                    option.value = tractorista.idtractorista;
                    option.dataset.idusuario = tractorista.idusuario_id;
                    option.textContent = `${tractorista.idpersona_id__nombres} ${tractorista.idpersona_id__apellidos}`;
                    selectTractorista.appendChild(option);
                });
            } else {
                let option = document.createElement('option');
                option.textContent = "No hay tractoristas disponibles";
                selectTractorista.appendChild(option);
            }

            // Verificar si hay tractores disponibles y agregarlos al select
            if (dataRecibida.tractores && dataRecibida.tractores.length > 0) {
                dataRecibida.tractores.forEach(tractor => {
                    let option = document.createElement('option');
                    option.value = tractor.idtractor;
                    option.dataset.idusuario = tractor.idusuario_id;
                    option.textContent = tractor.nrotractor;
                    selectTractor.appendChild(option);
                });
            } else {
                let option = document.createElement('option');
                option.textContent = "No hay tractores disponibles";
                selectTractor.appendChild(option);
            }

            if (dataRecibida.implementos && dataRecibida.implementos.length > 0) {
            dataRecibida.implementos.forEach(implemento => {
                let option = document.createElement('option');
                option.value = implemento.idimplemento;
                option.dataset.idusuario = implemento.idusuario_id;
                option.textContent = implemento.implemento;
                selectImplemento.appendChild(option);
            });
            } else {
                let option = document.createElement('option');
                option.textContent = "No hay implementos disponibles";
                selectImplemento.appendChild(option);
            }



            // Disparar eventos de cambio en los selects
            selectUsuario.dispatchEvent(new Event('change'));
            selectUsuario2.dispatchEvent(new Event('change'));
            selectUsuario3.dispatchEvent(new Event('change'));
        })
        .catch(error => console.log(error));
    }

    agregar.addEventListener('click', () => {
        const fecha = document.getElementById('id_fechahora').value;
        const turno = document.getElementById('id_turno').value;
        document.querySelector('.implementos').innerHTML = '';
        form.reset();
        obtener_data_select(fecha, turno);
    });
    
    id_fechahora.addEventListener('change', () => {
        const fecha = document.getElementById('id_fechahora').value;
        const turno = document.getElementById('id_turno').value;
        document.querySelector('.implementos').innerHTML = '';
        obtener_data_select(fecha, turno);
    })
    id_turno.addEventListener('change', () => {
        const fecha = document.getElementById('id_fechahora').value;
        const turno = document.getElementById('id_turno').value;
        document.querySelector('.implementos').innerHTML = '';
        obtener_data_select(fecha, turno);
    })

    // FIN DEL TRUCO




    let selectUsuario = document.getElementById('usuario_id');
    let selectedUserId = document.getElementById('usuario_id').value;

    let selectUsuario2 = document.getElementById('usuario_id_2');
    let selectTractor = document.getElementById('id_idtractor');

    let selectUsuario3 = document.getElementById('usuario_id_3');
    let selectTractorista = document.getElementById('id_idtractorista');

    let fundo = document.getElementById('idfundo');
    let lote = document.getElementById('id_idlote').value;

    function filtrarTractoresPorUsuario(userId) {
        id_idtractor.value = '';
        let tractorOptions = document.querySelectorAll('#id_idtractor option');
        tractorOptions.forEach(option => {
            if (option.dataset.idusuario !== userId && option.value !== '') {
                option.style.display = 'none';
            } else {
                option.style.display = 'block';
            }
        });
    }     
    
    function filtrarImplementosPorUsuario(userId) {
        let implementoOptions = document.querySelectorAll('#id_idimplemento option');
        implementoOptions.forEach(option => {
            if (option.dataset.idusuario !== userId && option.value !== '') {
                option.style.display = 'none';
            } else {
                option.style.display = 'block';
            }
        });

        let implementoOptions1 = document.querySelectorAll('#id_idimplemento_1 option');
        implementoOptions1.forEach(option => {
            if (option.dataset.idusuario !== userId && option.value !== '') {
                option.style.display = 'none';
            } else {
                option.style.display = 'block';
            }
        });

        let implementoOptions2 = document.querySelectorAll('#id_idimplemento_2 option');
        implementoOptions2.forEach(option => {
            if (option.dataset.idusuario !== userId && option.value !== '') {
                option.style.display = 'none';
            } else {
                option.style.display = 'block';
            }
        });

    }

    function filtrarTractoristasPorUsuario(userId) {
        id_idtractorista.value = '';
        let tractoristaOptions = document.querySelectorAll('#id_idtractorista option');
        tractoristaOptions.forEach(option => {
            if (option.dataset.idusuario !== userId && option.value !== '') {
                option.style.display = 'none';
            } else {
                option.style.display = 'block';
            }
        });
    }

    function filtrarLotesPorFundo(fundoId) {
        id_idlote.value = '';
        let loteOptions = document.querySelectorAll('#id_idlote option');
        loteOptions.forEach(option => {
            if (option.dataset.idfundo !== fundoId && option.value !== '') {
                option.style.display = 'none';
            } else {
                option.style.display = 'block';
            }
        });
    }

    selectUsuario.addEventListener('change', function() {
        let selectedUserId = this.value;
        filtrarImplementosPorUsuario(selectedUserId);
    });

    selectUsuario2.addEventListener('change', function() {
        let selectedUserId = this.value;
        filtrarTractoresPorUsuario(selectedUserId);
    });

    selectUsuario3.addEventListener('change', function() {
        let selectedUserId = this.value;
        filtrarTractoristasPorUsuario(selectedUserId);
    });

    fundo.addEventListener('change', function() {
        let selectedTractorId = this.value;
        filtrarLotesPorFundo(selectedTractorId);
    });
    
    let maxImplementos = 2;
    document.getElementById('btn-agregar').addEventListener('click', () => {
        let implementosAgregados = document.querySelectorAll('.implementos .implemento-item').length;
        if (implementosAgregados < maxImplementos) {
            // Clonar el select
            var selectClonado = document.getElementById('id_idimplemento').cloneNode(true);
            selectClonado.id = `id_idimplemento_${implementosAgregados + 1}`;

            // Crear un contenedor para el select y el botón de eliminar
            var contenedor = document.createElement('div');
            contenedor.classList.add('implemento-item');

            // Crear el botón de eliminar
            var botonEliminar = document.createElement('button');
            botonEliminar.textContent = 'Eliminar';
            botonEliminar.classList.add('btn', 'btn-danger', 'ms-2');
            botonEliminar.addEventListener('click', () => {
                contenedor.remove();
            });

            // Añadir el select clonado y el botón al contenedor
            contenedor.appendChild(selectClonado);
            contenedor.appendChild(botonEliminar);

            // Añadir el contenedor a la lista de implementos
            document.querySelector('.implementos').appendChild(contenedor);
        } else {
            // Mostrar mensaje de límite alcanzado si no existe ya
            if (!document.querySelector('.implementos .text-danger')) {
                var mensaje = document.createElement('span');
                mensaje.id = 10;
                mensaje.textContent = '¡Llegaste al máximo de implementos permitidos!';
                mensaje.classList.add('text-danger', 'ms-2');
                document.querySelector('.implementos').insertBefore(mensaje, document.querySelector('.implementos').firstChild);
            }
        }
    });
    
    document.querySelectorAll('.btn-ver').forEach(button => {
        button.addEventListener('click', function() {
            let idProgramacion = this.getAttribute('data-idprogramacion');
            fetch(`./obtener_data/${idProgramacion}`)
            .then(response => response.json())
            .then(data => {
                if (data.mensaje === "Success") {
                    var modalBody = document.querySelector('#modalListImplemento .modal-body');
                    modalBody.innerHTML = '';
                    var ul = document.createElement('ul');
                    data.nombres_implementos.forEach(nombre => {
                        var li = document.createElement('li');
                        li.textContent = nombre;
                        ul.appendChild(li);
                    });
                    modalBody.appendChild(ul);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });

    $(document).ready(function(){
        $('[data-toggle="tooltip"]').tooltip(); 
    });
    
    //Llamado de funciones
    filtrarImplementosPorUsuario(selectedUserId);
    filtrarTractoresPorUsuario(selectTractor);
    filtrarTractoristasPorUsuario(selectTractorista);
    filtrarLotesPorFundo(lote);

});