from flask import Flask, render_template, request, redirect, url_for
from models import UsuarioModel

app = Flask(__name__)
Usuario_model = UsuarioModel()

@app.route('/usuarios')
def listar_usuarios():
    usuarios = Usuario_model.get_todos()
    return render_template('usuarios.html', listar_de_usuarios=usuarios)

@app.route('/usuarios/novo', methods=['POST'])
def adicionar_usuario():
    nome = request.form['nome']
    email = request.form['email']
    Usuario_model.salvar(nome,email)
    return redirect(url_for('listar_usuarios'))

if __name__ == '__main__':
    app.run(debug=True)