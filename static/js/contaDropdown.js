const dropdown = document.getElementById('conta-dropdown');
const lista = document.getElementById('conta-dropdown-lista');

dropdown.addEventListener('click', () => {
    lista.classList.toggle('show');
}, false);

window.addEventListener('click', (e) => {
    if (e.target.id !== 'conta-dropdown') {
        lista.classList.remove('show');
    }
});