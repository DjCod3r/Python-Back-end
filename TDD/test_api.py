# test_api.py
import requests
from api import app

def test_obter_usuario_existente():
    resposta = requests.get('http://127.0.0.1:5000/usuario/1')
    dados = resposta.json()
    assert resposta.status_code == 200
    assert dados['nome'] == 'Alice'
def test_obter_usuario_inexistente():
    resposta = requests.get('http://127.0.0.1:5000/usuario/3')
    dados = resposta.json()
    assert resposta.status_code == 404
    assert dados['mensagem'] == 'Usuário não encontrado'