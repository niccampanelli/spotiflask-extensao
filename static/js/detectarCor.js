const provedorDeCor = document.getElementsByClassName('provedorDeCor')[0];
const aplicaCorDinamica = document.getElementsByClassName('aplicaCorDinamica')[0];

const detectarCor = () => {
    const cor = provedorDeCor.style.backgroundColor;
    aplicaCorDinamica.style.backgroundColor = cor;
}
window.addEventListener('load', detectarCor);