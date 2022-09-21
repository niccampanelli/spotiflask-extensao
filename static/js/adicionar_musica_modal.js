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

    fetch(`usuario/${artistaId}/playlists`)
        .then(response => response.json())
        .then(albuns => {
            albunsDatalist.innerHTML = '';
            albuns.forEach(album => {
                console.log(album);
                const option = document.createElement('option');
                option.value = album[0];
                option.innerText = album[1];
                albunsDatalist.appendChild(option);
            });
        });
})