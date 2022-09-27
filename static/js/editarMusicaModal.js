const modal = document.getElementById('editar-musica-modal');

modal.addEventListener('click', (e) => {
    if (e.target.id === 'editar-musica-modal') {
        window.location.href = window.location.href.substring(0, window.location.href.indexOf('/musica'));
    }
})