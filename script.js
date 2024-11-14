// Función para desplegar/plegar el menú lateral
function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const menuOptions = document.querySelector('.menu-options');

    // Expandir la barra lateral
    sidebar.classList.toggle('expanded');

    // Mostrar/ocultar las opciones de navegación
    if (sidebar.classList.contains('expanded')) {
        menuOptions.style.display = 'block';
    } else {
        menuOptions.style.display = 'none';
    }
}

// Función para mostrar el contenido basado en la opción seleccionada
function showContent(section) {
    const sections = document.querySelectorAll('.section');
    sections.forEach(s => s.style.display = 'none');
    document.getElementById(section).style.display = 'block';
}

// Función para desplegar/plegar el dropdown de servicios
// Función para desplegar/plegar el dropdown de servicios
function toggleDropdown(dropdownId) {
    const dropdown = document.getElementById(dropdownId);
    dropdown.classList.toggle('active'); // Añadimos o quitamos la clase active
}
