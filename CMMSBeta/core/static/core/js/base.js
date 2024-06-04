document.addEventListener("DOMContentLoaded", function() {
    const hamBurger = document.querySelector(".toggle-btn");
    const sidebar = document.querySelector("#sidebar");
    let activeDropdownId = localStorage.getItem("activeDropdownId"); // Obtener el ID de la lista desplegable activa

    // Check local storage for sidebar state
    if (localStorage.getItem("sidebarState") === "expanded") {
        sidebar.classList.add("expand");
    }

    hamBurger.addEventListener("click", function () {
        sidebar.classList.toggle("expand");
        
        // Save the current state of the sidebar
        if (sidebar.classList.contains("expand")) {
            localStorage.setItem("sidebarState", "expanded");
        } else {
            localStorage.setItem("sidebarState", "collapsed");
        }
    });

    const sidebarItems = document.querySelectorAll(".sidebar-item.has-dropdown");

    sidebarItems.forEach(function(item) {
        const link = item.querySelector(".sidebar-link");
        const dropdown = item.querySelector(".sidebar-dropdown");
        const dropdownId = dropdown.getAttribute("id");

        link.addEventListener("click", function (event) {
            event.preventDefault();

            // Si la lista desplegable actual es diferente de la lista desplegable activa, ábrela
            if (activeDropdownId !== dropdownId) {
                // Cerrar la lista desplegable activa anterior
                if (activeDropdownId) {
                    const prevDropdown = document.getElementById(activeDropdownId);
                    prevDropdown.classList.remove("show");
                    prevDropdown.classList.add("collapse");
                }

                // Abrir la lista desplegable actual
                dropdown.classList.add("show");
                dropdown.classList.remove("collapse");
                
                // Guardar el ID de la lista desplegable activa en localStorage
                activeDropdownId = dropdownId;
                localStorage.setItem("activeDropdownId", activeDropdownId);
            } else {
                // Si se hace clic en la misma lista desplegable, ciérrala
                dropdown.classList.remove("show");
                dropdown.classList.add("collapse");

                // Limpiar el ID de la lista desplegable activa en localStorage
                activeDropdownId = null;
                localStorage.removeItem("activeDropdownId");
            }
        });
    });
});
