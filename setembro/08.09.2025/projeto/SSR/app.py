from flask import Flask, render_template
app = Flask(__name__)

@app.route('/notas')
def mostrar_notas():
    alunos = [
    {'nome': 'Ana', 'nota': 9.5},
    {'nome': 'Beto', 'nota': 6.0},
    {'nome': 'Carlos', 'nota': 4.5}
    ]
    return render_template('notas.html', lista_de_alunos=alunos)

if __name__ == '__main__':
    app.run(debug=True, port=5001)