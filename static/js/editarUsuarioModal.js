const modal = document.getElementById('editar-usuario-modal');

modal.addEventListener('click', (e) => {
    if (e.target.id === 'editar-usuario-modal') {
        window.location.href = window.location.href.substring(0, window.location.href.indexOf('/editar'));
    }
})