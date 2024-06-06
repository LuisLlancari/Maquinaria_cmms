document.addEventListener("DOMContentLoaded", () => {
    //Funcion para que el mensaje tenga un tiempo de espera de 3 segundos
    setTimeout(function() {
        var errorMessage = document.getElementById('message');

        if (errorMessage ) {
            errorMessage.style.display = 'none';
        }
    },5000);

    setTimeout(function() {
        var span_error = document.getElementById('10');

        if (span_error) {
            span_error.style.display = 'none';
        }
    },5000);
})