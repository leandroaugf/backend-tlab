// [ABRE O NAVEGADOR -> COLETA DADOS -> LÊ O HTML(DOM) -> SALVA NO .csv]
const puppeteer = require('puppeteer');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;
const fs = require('fs') // filesystem
const path = require('path')

const pathCsv = path.join(__dirname, '..', 'historico_precos.csv')

async function executarColeta() {
    console.log('1. ABRINDO O NAVEGADOR...')
    const browser = await puppeteer.launch({ headless: "new" })
    const page = await browser.newPage();

    console.log('2. ACESSANDO O SITE...')
    // site educacional para scraping
    await page.goto('http://books.toscrape.com/', {waitUntil: 'domcontentloaded'})

    // LENDO A PÁGINA HTML: page.evaluate roda um cod dentro do navegador, como se fosse o console do chrome
    console.log('3. LENDO A PÁGINA HTML...')
    const produtos = await page.evaluate(() => {
        // pega todos os blocos de livros na tela
        const blocos = document.querySelectorAll('.product_pod')
        const lista = []

        // para cada bloco, extrai o título e preço
        blocos.forEach(bloco => {
            const titulo = bloco.querySelector('h3 a');
            const preco  =  bloco.querySelector('.price_color');

            const tituloValue = titulo ? titulo.innerText : "Sem título"
            // Transforma o 'R$50' no número '50'
            const precoValue = parseFloat(preco.innerText.replace(/[^\d.]/g, ''));

            lista.push({ titulo: tituloValue, preco: precoValue });
        });
        return lista;
    });
    console.log(`Foram encontrados ${produtos.length} produtos`)

    console.log('4. SALVANDO DADOS NO ARQUIVO .csv ...')
    const csvWriter = createCsvWriter({
        path: pathCsv,
        header: [
            { id: 'data', title: 'DATA_COLETA' },
            { id: 'loja', title: 'LOJA' },
            { id: 'produto', title: 'PRODUTO' },
            { id: 'preco', title: 'PRECO' }
        ],
        // cria o caminho ou adiciona no final caso já exista
        append: fs.existsSync(pathCsv)
    });

    // Data de hoje no formato YYYY-MM-DD [truque]
    const hoje = new Date().toISOString().substring(0, 10);

    // Formata os dados para o .csv
    const registros = produtos.map(item => {
        return {
            data: hoje,
            loja: 'BooksToScrape',
            produto: item.titulo,
            preco: item.preco
        };
    });

    await csvWriter.writeRecords(registros);
    console.log('Precificação concluída!')

    await browser.close()
};

module.exports = { executarColeta } ;
