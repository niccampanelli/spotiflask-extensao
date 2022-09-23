const playlistOpcoes = document.getElementById('playlist-opcoes');
const playlistOpcoesLista = document.getElementById('playlist-opcoes-lista');

playlistOpcoes.addEventListener('click', () => {
    playlistOpcoesLista?.classList.toggle('show');
}, false);

window.addEventListener('click', (e) => {
    if (e.target.id !== 'playlist-opcoes') {
        playlistOpcoesLista?.classList.remove('show');
    }
});