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

@app.route('/consulta', methods=['GET'])
def consultar_agify():
    try:
        # Obtain the name parameter from the request
        name = request.args.get('name')

        # Make a request to the agify API
        responseAgify = requests.get(f"http://localhost:3000/agify?name={name}")
        responseGen = requests.get(f"http://localhost:3001/genderize?name={name}")

        # Check if the request was successful
        if responseAgify.status_code == 200 and responseGen.status_code == 200:
            dataAgify = responseAgify.json()
            dataGen = responseGen.json()
            # You may want to combine the data from both APIs before returning it.
            combined_data = {
                "agify_data": dataAgify,
                "genderize_data": dataGen
            }
            return jsonify(combined_data)
        else:
            return jsonify({'error': 'Error al consultar la API Agify o Genderize'})
        
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3002, debug=True)
