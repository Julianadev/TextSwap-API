from flask import Flask, jsonify, request
from substituicao import Substituir

app = Flask(__name__)

@app.route('/substituir', methods=['POST'])
def substituir():
    """Endpoint para realizar a substituição de caracteres."""
    data = request.json

    if not data or not all(key in data for key in ('texto', 'localizar', 'caractere_substituto')):
        return jsonify({'error': 'Por favor, forneça texto, localizar e caractere_substituto.'}), 400

    texto = data['texto']
    localizar = data['localizar']
    caractere_substituto = data['caractere_substituto']

    substituicao = Substituir(texto, localizar, caractere_substituto)
    resultado = substituicao.substituicao()

    return jsonify({'resultado': resultado})

@app.route('/')
def index():
    """Endpoint para teste básico."""
    return jsonify({
        "mensagem": "Bem-vindo à API de substituição de caracteres!",
        "exemplo": {
            "texto": "Olá mundo",
            "localizar": "mundo",
            "caractere_substituto": "Python"
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
