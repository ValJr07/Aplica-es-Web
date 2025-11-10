from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

connector = sqlite3.connect('Hospedagem.db')
with connector as connection:
    cursor = connector.cursor()

    create_table_quarto = '''
    CREATE TABLE Quarto(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco FLOAT,
        descricao TEXT,
        imagem TEXT
    );    
    '''

    insert_quarto = '''
    INSERT INTO Quarto(nome, preco, descricao, imagem)
    VALUES(?, ?, ?, ?);
    '''

    delete_quarto = '''
    DELETE FROM Quarto
    WHERE id = ?;
    '''

    quarto_id = 1


    data_quarto1 = ("Suíte Luxo Vista Mar", 550.00, "Ampla, com varanda e vista panorâmica para o mar.", "https://picsum.photos/seed/quarto1/600/400")
    data_quarto2 = ("Suíte Standard", 320.00, "Aconchegante e moderna, ideal para casais.", "https://picsum.photos/seed/quarto2/600/400")
    data_quarto3 = ("Quarto Econômico", 210.00, "Simplicidade e conforto pelo melhor preço.", "https://picsum.photos/seed/quarto3/600/400")

    select_quarto = "SELECT * FROM Quarto;"

    cursor.execute(select_quarto)

    todos_quartos = cursor.fetchall()


    print("todos os quartos:")
    for quarto in todos_quartos:
        print(quarto)

#BD
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
    return render_template('index.html', quarto=todos_quartos)

@app.route('/quarto/<int:id>')
def quarto(id):
    quarto_escolhido = next((q for q in todos_quartos if q["id"] == id), None)
    if quarto_escolhido:
        return render_template('quarto.html', quarto=quarto_escolhido)
    return "<h2>Quarto não encontrado 😢</h2>", 404

if __name__ == '__main__':
    app.run(debug=True)
