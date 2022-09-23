const modal = document.getElementById('excluir-musica-modal');

modal.addEventListener('click', (e) => {
    if (e.target.id === 'excluir-musica-modal') {
        window.location.href = window.location.href.substring(0, window.location.href.indexOf('/musica'));
    }
})