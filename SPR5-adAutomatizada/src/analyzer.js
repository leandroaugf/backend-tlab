const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');

function analisarDados() {
    return new Promise((resolve, reject) => {
        const caminhoCsv = path.join(__dirname, '..', 'historico_precos.csv');

        if (!fs.existsSync(caminhoCsv)) {
            return reject('Nenhum dado encontrado - execute o scraper');
        }

        let quantidade = 0;
        let totalPrecos = 0;

        // Cria um fluxo read (readStream) linha por linha
        fs.createReadStream(caminhoCsv)
            .pipe(csv())
            // .on => ligado a => escutador de eventos
            .on('data', (linha) => { //.on('data'): ao ler uma linha do csv, execute isso...
                // executa a cada linha que lê
                const preco = parseFloat(linha.PRECO);
                if (!isNaN(preco)) {
                    totalPrecos += preco;
                    quantidade++;
                }
            })
            .on('end', () => {
                // CÁLCULO DA MÉDIA
                const media = totalPrecos / quantidade;

                console.log('=== RELATÓRIO DE ANÁLISE ===');
                console.log(`Total de produtos analisados: ${quantidade}`)
                console.log(`PREÇO MÉDIO GERAL: R$${media.toFixed(2)}`);
                resolve()
            })
            .on('error', (erro) => {
                reject(erro);
            });
    });
};

module.exports = { analisarDados };
