from flask import Flask, render_template

app = Flask(__name__)

#BD 
quartos = [
    {
        "id": 1,
        "nome": "Suíte Luxo Vista Mar",
        "preco": 550,
        "descricao": "Ampla, com varanda e vista panorâmica para o mar.",
        "imagem": "https://picsum.photos/seed/quarto1/600/400"
    },
    {
        "id": 2,
        "nome": "Suíte Standard",
        "preco": 320,
        "descricao": "Aconchegante e moderna, ideal para casais.",
        "imagem": "https://picsum.photos/seed/quarto2/600/400"
    },
    {
        "id": 3,
        "nome": "Quarto Econômico",
        "preco": 210,
        "descricao": "Simplicidade e conforto pelo melhor preço.",
        "imagem": "https://picsum.photos/seed/quarto3/600/400"
    }
]

@app.route('/')
def index():
    return render_template('index.html', quartos=quartos)

@app.route('/quarto/<int:id>')
def quarto(id):
    quarto_escolhido = next((q for q in quartos if q["id"] == id), None)
    if quarto_escolhido:
        return render_template('quarto.html', quarto=quarto_escolhido)
    return "<h2>Quarto não encontrado 😢</h2>", 404

if __name__ == '__main__':
    app.run(debug=True)
