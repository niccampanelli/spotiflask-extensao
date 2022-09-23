const headerContaDropdown = document.getElementById('conta-dropdown');
const headerContaDropdownLista = document.getElementById('conta-dropdown-lista');

headerContaDropdown.addEventListener('click', () => {
    headerContaDropdownLista?.classList.toggle('show');
}, false);

window.addEventListener('click', (e) => {
    if (e.target.id !== 'conta-dropdown') {
        headerContaDropdownLista?.classList.remove('show');
    }
});