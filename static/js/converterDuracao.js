const inputDuracao = document.getElementById('duracao');
const inputDuracaoSegundos = document.getElementById('duracaoEmSegundos');

inputDuracao.addEventListener('input', () => {
    const duracao = inputDuracao.value;
    const duracaoEmSegundos = converterDuracao(duracao);
    inputDuracaoSegundos.value = duracaoEmSegundos;
    console.log(duracaoEmSegundos);
});

function converterDuracao(duracao) {
    const duracaoEmSegundos = duracao.split(':').reduce((acc, time) => {
        return (60 * acc) + +time;
    }, 0);
    return duracaoEmSegundos;
}
