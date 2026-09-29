const { executarColeta } = require('./scraper')
const { analisarDados } = require('./analyzer')

async function iniciarSistema() {
    console.log('=== INICIANDO SISTEMA DE PRECIFICAÇÃO ===')

    // 'await' faz o Node esperar a raspagem/precificação antes de seguir
    await executarColeta();

    try {
        await analisarDados();
    } catch (erro) {
        console.log('Erro durante a análise: ', erro)
    }
    console.log('\n=== PROCESSO FINALIZADO ===')
};

iniciarSistema();
