from flask import Flask, render_template, jsonify
app = Flask(__name__)
# Rota 1: Serve a "casca" da aplicação (o HTML vazio)
@app.route('/')
def pagina_app():
# Envia o "kit de montar" para o navegador
    return render_template('index.html')
# Rota 2: API que fornece os dados em formato JSON (os "ingredientes")
@app.route('/api/alunos')
def api_alunos():
    alunos = [
        {'nome': 'Daniela', 'nota': 10.0},
        {'nome': 'Eduardo', 'nota': 8.0},
        {'nome': 'Fernanda', 'nota': 5.5}
    ]
# Retorna os dados em formato JSON, que o JavaScript entende.
    return jsonify(alunos)
if __name__ == '__main__':
    app.run(debug=True, port=5001)