function definirCorAleatoria(elemento) {
    console.log(elemento);
    elemento.style.backgroundColor = gerarCorAleatoria();
}

function gerarCorAleatoria() {
    return '#' + Math.floor(Math.random() * 16777215).toString(16);
}