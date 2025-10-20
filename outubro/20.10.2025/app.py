from flask import Flask, render_template,request,abort,jsonify

app = Flask(__name__)

usuarios = [
    {"id": 1, "nomeC" : "Valter", "email":"aaa@gmail.com", "senha_hash" : "abc123", "perfil_id": 1},
]

perfis = [
    {"id":usuarios[0]["perfil_id"], "nome_perfil": "Administrador"}
]

tipos_quarto = [
    {"id_tipo" : 1, "nome_tipo": "Luxo", "capacidade_max": "3", "preco_diariaB" : 90, "descricao": "Tem cama e privada"}
]

retorno = {
    "Simples" : 1,
    "Luxo" : 2,
    "Suite presidencial" : 3,
}

def retornoTipos(indice):
    valor = tipos_quarto[indice].get("nome_tipo")
    if valor in retorno:
        return retorno[valor]
    return None



quartos = [
    {"num_quartos" : 1, "id_tipo" : retornoTipos(0), "statusLimp" : "Limpando", "localizacao" : "Térreo"}
]

hospedes = [
    {"id_hospede":1, "NomeC" : "Valter", "documento": 52775210806, "telefone": 11940028922, "email" : "aaa@gmail.com", "id_usuario" :  id_usuarios}
]

reservas = [
    {"id_reserva" : 1, "id_hospede" : '''id_hospede''', "num_quartos" : '''num_quartos FK''', "data_chekin": "11.02.2003", "data_checkout" : "11.02.2025", "status_reserva" : "Confirmada", "valor_total" : 1000000 }
]

servicos = [
    {"id":1, "nome_servico": "Minibar", "preco": 100}
]

faturas = [
    {"id_fatura": 1, "id_reserva" : "id_reserva", "data_emissao" : "11.02.2003", "valor_servicos": 120, "valor_diarias": 120, "status_pagamento": "Parcialmente Pago"}
]

itens_fatura = [
    {"id_item" : 1, "id_fatura" : '''id_fatura''', "id_servico": '''id_servico''', "quantidade":20, "preco_unitario": 123, "data_consumo": "11.02.2003"}
]
