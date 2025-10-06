from flask import Flask, render_template,request,abort,jsonify
import math

app = Flask(__name__)

produtos = [
    {"id": 1,"nome": "Notebook", "preco": 1500},
    {"id": 2,"nome": "PS5", "preco": 3000},
    {"id": 3,"nome": "Jogo", "preco": 200},
    {"id": 4,"nome": "Placa de video", "preco": 1200},
    {"id": 5,"nome": "Processador", "preco": 1000},
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
    for produto in produtos:
        if produto["id"] == produto_id:
            produto_encontrado = produto
            break
        if produto_encontrado is None:
            abort(404)
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

