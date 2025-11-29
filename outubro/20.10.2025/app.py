from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('Hospedagem.db')
    conn.row_factory = sqlite3.Row  
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Quarto(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco FLOAT,
            descricao TEXT,
            imagem TEXT
        );
    ''')

    cursor.execute("SELECT COUNT(*) FROM Quarto")
    if cursor.fetchone()[0] == 0:
        dados = [
            ("Suíte Luxo Vista Mar", 550.00, "Ampla, com varanda e vista panorâmica para o mar.", "https://picsum.photos/seed/quarto1/600/400"),
            ("Suíte Standard", 320.00, "Aconchegante e moderna, ideal para casais.", "https://picsum.photos/seed/quarto2/600/400"),
            ("Quarto Econômico", 210.00, "Simplicidade e conforto pelo melhor preço.", "https://picsum.photos/seed/quarto3/600/400")
        ]

        cursor.executemany(
            "INSERT INTO Quarto(nome, preco, descricao, imagem) VALUES (?, ?, ?, ?)",
            dados
        )

    conn.commit()
    conn.close()

init_db()

#BD antigo
'''
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
'''

@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Quarto")
    quartos = cursor.fetchall()
    conn.close()

    return render_template('index.html', quartos=quartos)

@app.route('/quarto/<int:id>')
def quarto(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Quarto WHERE id = ?", (id,))
    quarto_escolhido = cursor.fetchone()
    conn.close()

    if quarto_escolhido:
        return render_template('quarto.html', quarto=quarto_escolhido)

    return "<h2>Quarto não encontrado</h2>", 404

if __name__ == '__main__':
    app.run(debug=True)
