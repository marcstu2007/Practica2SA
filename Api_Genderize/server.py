import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Add CORS to the application

@app.route('/live', methods=['GET'])
def obtener_usuario_contrasena():
    try:
        return jsonify({'Mensaje': "Hola mundo"})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/genderize', methods=['GET'])
def consultar_agify():
    try:
        # Obtain the name parameter from the request
        name = request.args.get('name')

        # Make a request to the agify API
        response = requests.get(f"https://api.genderize.io?name={name}")

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({'error': 'Error al consultar la API genderize'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001, debug=True)