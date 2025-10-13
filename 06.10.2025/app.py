from flask import Flask, render_template,request,abort,jsonify
import math

app = Flask(__name__)

produtos = [
    {"id": 1,"nome": "Notebook", "preco": 1500},
    {"id": 2,"nome": "PS5", "preco": 3000},
    {"id": 3,"nome": "Jogo", "preco": 200},
    {"id": 4,"nome": "Placa de video", "preco": 1200},
    {"id": 5,"nome": "Processador", "preco": 1000},
    {"id": 6, "nome": "Monitor", "preco": 800},
    {"id": 7, "nome": "Teclado Mecânico", "preco": 400},
    {"id": 8, "nome": "Mouse Gamer", "preco": 250},
    {"id": 9, "nome": "Fone de Ouvido", "preco": 350},
    {"id": 10, "nome": "SSD 1TB", "preco": 600},
    {"id": 11, "nome": "Webcam", "preco": 300},
    {"id": 12, "nome": "Microfone", "preco": 500},
    {"id": 13, "nome": "Caixa de Som", "preco": 450},
    {"id": 14, "nome": "Carregador Portátil", "preco": 200},
    {"id": 15, "nome": "Tablet", "preco": 1200},
    {"id": 16, "nome": "Smartphone", "preco": 2500},
    {"id": 17, "nome": "Drone", "preco": 2200},
    {"id": 18, "nome": "Câmera DSLR", "preco": 3500},
    {"id": 19, "nome": "Impressora", "preco": 700},
    {"id": 20, "nome": "Gamer Chair", "preco": 900},
    {"id": 21, "nome": "HD Externo 2TB", "preco": 500},
    {"id": 22, "nome": "Placa Mãe", "preco": 800},
    {"id": 23, "nome": "Memória RAM 16GB", "preco": 400},
    {"id": 24, "nome": "Fonte de Alimentação", "preco": 300},
    {"id": 25, "nome": "Cooling Pad", "preco": 150},
    {"id": 26, "nome": "Gamepad", "preco": 300},
    {"id": 27, "nome": "Roteador", "preco": 250},
    {"id": 28, "nome": "Cabo HDMI", "preco": 80},
    {"id": 29, "nome": "Consoles Antigos", "preco": 1500},
    {"id": 30, "nome": "Luminária LED", "preco": 100},
]

@app.route('/produtos')
def listar_produtos():
    return render_template('produtos.html',produtos=produtos)

@app.route('/produtos-paginados')
def listar_produtos_paginados():
    page = request.args.get('page',1,type=int)
    per_page = 5
    start = (page-1)*per_page
    end = start+per_page
    total_pages = math.ceil(len(produtos)/per_page)
    produtos_da_pagina = produtos[start:end]
    return render_template('produtos_paginados.html',produtos=produtos_da_pagina, page=page, total_pages=total_pages)

@app.route('/produto/<int:produto_id>')
def detalhe_produto(produto_id):
    produto_encontrado = None
    try:
        produto_encontrado = produtos[produto_id-1]
    except:
        pass
    #for produto in produtos:
    #    if produto["id"] == produto_id:
     #       produto_encontrado = produto
      #      break
    return render_template('detalhe_produto.html', produto=produto_encontrado)


@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template('404.html'),404

@app.route('/api/busca-produto', methods=['POST'])
def buscar_produtos():
    dados = request.get_json()
    nome_produto = dados.get('nome').lower()
    resultado = [p for p in produtos if nome_produto in p['nome'].lower()]
    return jsonify({'produtos_encontrados':resultado})

if __name__ == '__main__':
    app.run(debug=True)

