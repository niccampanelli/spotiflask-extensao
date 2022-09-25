const modal = document.getElementById('excluir-usuario-modal');

modal.addEventListener('click', (e) => {
    if (e.target.id === 'excluir-usuario-modal') {
        window.location.href = window.location.href.substring(0, window.location.href.indexOf('/usuario'));
    }
})