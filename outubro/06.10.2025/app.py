from flask import Flask, render_template,request,abort,jsonify
from flask_sqlalchemy import SQLAlchemy
import math

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///produtos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "preco": self.preco}
    
def criar_bd():
    db.create_all()

    if Produto.query.count() == 0:
        lista = [
            ("Notebook", 1500), ("PS5", 3000), ("Jogo", 200), ("Placa de video", 1200),
            ("Processador", 1000), ("Monitor", 800), ("Teclado Mecânico", 400),
            ("Mouse Gamer", 250), ("Fone de Ouvido", 350), ("SSD 1TB", 600),
            ("Webcam", 300), ("Microfone", 500), ("Caixa de Som", 450),
            ("Carregador Portátil", 200), ("Tablet", 1200), ("Smartphone", 2500),
            ("Drone", 2200), ("Câmera DSLR", 3500), ("Impressora", 700),
            ("Gamer Chair", 900), ("HD Externo 2TB", 500), ("Placa Mãe", 800),
            ("Memória RAM 16GB", 400), ("Fonte de Alimentação", 300),
            ("Cooling Pad", 150), ("Gamepad", 300), ("Roteador", 250),
            ("Cabo HDMI", 80), ("Consoles Antigos", 1500), ("Luminária LED", 100)
        ]

        for nome, preco in lista:
            db.session.add(Produto(nome=nome, preco=preco))
        db.session.commit()

@app.route('/produtos')
def listar_produtos():
    produtos = Produto.query.all()
    return render_template('produtos.html',produtos=produtos)

@app.route('/produtos/pagina/<int:page>')
def listar_produtos_paginados(page=1):
    per_page = 5
    paginacao = Produto.query.paginate(page=page, per_page=per_page)
    produtos_da_pagina = paginacao.items

    return render_template(
        "produtos_paginados.html",
        produtos=produtos_da_pagina,
        page=page,
        total_pages=paginacao.pages
    )

@app.route('/produto/<int:produto_id>')
def detalhe_produto(produto_id):
    produto = Produto.query.get(produto_id)
    return render_template('detalhe_produto.html', produto=produto)


@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template('404.html'),404

def buscar_produtos():
    dados = request.get_json()
    nome_produto = dados.get("nome", "").lower()
    resultado = Produto.query.filter(Produto.nome.ilike(f"%{nome_produto}%")).all()
    return jsonify({
        "produtos_encontrados": [p.to_dict() for p in resultado]
    })

if __name__ == '__main__':
    with app.app_context():
        criar_bd()
    app.run(debug=True)

