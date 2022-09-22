const modal = document.getElementById('adicionar-musica-modal');
const artistaSelect = document.getElementById('artista');

modal.addEventListener('click', (e) => {
    if (e.target.id === 'adicionar-musica-modal') {
        window.location.href = '/';
    }
})

artistaSelect.addEventListener('change', (e) => {
    const artistaId = e.target.value;
    const albunsDatalist = document.getElementById('albuns');

    albunsDatalist.innerHTML = '';
    fetch(`usuario/artista/${artistaId || 0}/albuns`)
        .then(response => response.json())
        .then(albuns => {
            console.log(albuns);
            albuns.forEach(album => {
                const option = document.createElement('option');
                option.value = album[0];
                option.innerText = album[1];
                albunsDatalist.appendChild(option);
            });
        });
})