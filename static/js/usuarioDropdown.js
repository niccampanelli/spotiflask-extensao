const usuarioOpcoes = document.getElementById('usuario-opcoes');
const usuarioOpcoesLista = document.getElementById('usuario-opcoes-lista');

usuarioOpcoes.addEventListener('click', () => {
    usuarioOpcoesLista?.classList.toggle('show');
}, false);

window.addEventListener('click', (e) => {
    if (e.target.id !== 'usuario-opcoes') {
        usuarioOpcoesLista?.classList.remove('show');
    }
});