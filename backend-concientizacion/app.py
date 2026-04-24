from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Permitimos CORS para que Angular (normalmente en el puerto 4200) pueda conectar
CORS(app)

@app.route('/api/registro', methods=['POST'])
def registro():
    data = request.json
    
    # En una campaña real, aquí podrías contar cuántos usuarios 'cayeron'
    # sin necesidad de guardar sus datos privados (DNI, Nombres).
    print(f"Alerta: Intento de registro detectado.")
    print(f"Simulando recepción de datos de: {data.get('email')}")

    # Respondemos con éxito para que Angular haga la redirección
    return jsonify({
        "status": "success",
        "message": "Registro procesado correctamente"
    }), 200

if __name__ == '__main__':
    # Correr en el puerto 5000
    app.run(debug=True, port=5000)