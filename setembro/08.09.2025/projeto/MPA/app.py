from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/sobre')
def pagina_sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)