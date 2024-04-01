# api.py
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/usuario/<int:usuario_id>', methods=['GET'])
def obter_usuario(usuario_id):
    usuarios = {
        1: {'nome': 'Alice', 'idade': 30},
        2: {'nome': 'Bob', 'idade': 25},
    }
    usuario = usuarios.get(usuario_id)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404
if __name__ == '__main__':
    app.run()