const modal = document.getElementById('editar-playlist-modal');

modal.addEventListener('click', (e) => {
    if (e.target.id === 'editar-playlist-modal') {
        window.location.href = window.location.href.substring(0, window.location.href.indexOf('/editar'));
    }
})