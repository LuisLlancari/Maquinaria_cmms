const hamBurger = document.querySelector(".toggle-btn");


document.querySelector("#sidebar").classList.toggle("expand");
// hamBurger.addEventListener("click", function () {
// });

document.addEventListener("DOMContentLoaded", function() {
  var currentPath = window.location.pathname; // Obtener la ruta actual
  console.log(currentPath)
  var dropdownLinks = document.querySelectorAll(".sidebar-link.has-dropdown");

  if (currentPath === "/") {
      currentPath = "inicio";
      var itemLink = item.querySelector(".sidebar-link");
      var itemPath = itemLink.getAttribute("data-path");
  }
  
  dropdownLinks.forEach(function(link) {
      var dropdown = link.nextElementSibling;
      var dropdownItems = dropdown.querySelectorAll(".sidebar-item");
      
      dropdownItems.forEach(function(item) {
          var itemLink = item.querySelector(".sidebar-link");
          var itemPath = itemLink.getAttribute("data-path"); // Obtener el atributo data-path
          console.log(itemPath)

            // Eliminar la barra diagonal inicial de currentPath si existe
          if (currentPath.charAt(0) === '/') {
              currentPath = currentPath.substring(1);
          }
          
          // Comprobar si la ruta actual coincide con el atributo data-path del ítem del dropdown
          if (currentPath === itemPath) {
              dropdown.classList.add("show"); // Abrir el dropdown
              itemLink.classList.add("active"); // Marcar la opción activa
              itemLink.classList.add("hover"); // Marcar la opción como hover
          }
      });
  });
});
