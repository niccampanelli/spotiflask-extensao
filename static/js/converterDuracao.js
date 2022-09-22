const inputDuracao = document.getElementById('duracao');
const inputDuracaoSegundos = document.getElementById('duracaoEmSegundos');

inputDuracao.addEventListener('input', () => {
    const duracao = inputDuracao.value;
    const duracaoEmSegundos = converterParaSegundos(duracao);
    inputDuracaoSegundos.value = duracaoEmSegundos;
});

function converterParaSegundos(duracao) {
    const duracaoEmSegundos = duracao.split(':').reduce((acc, time) => {
        return (60 * acc) + +time;
    }, 0);
    return duracaoEmSegundos;
}