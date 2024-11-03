from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import datetime

app = Flask(__name__)

# Configuración de la clave secreta para JWT
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

# Ruta para autenticar y obtener el token JWT
@app.route('/api/login', methods=['POST'])
def login():
    if request.json.get("username") == "user" and request.json.get("password") == "pass":
        expires = datetime.timedelta(hours=1)
        access_token = create_access_token(identity={"username": "user"}, expires_delta=expires)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid credentials"}), 401

# Ruta protegida por JWT
@app.route('/api/data', methods=['GET'])
@jwt_required()
def get_data():
    data = {"message": "Hello from the server!"}
    return jsonify(data)

# / 
@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=('certs/server.crt', 'certs/server.key'))
