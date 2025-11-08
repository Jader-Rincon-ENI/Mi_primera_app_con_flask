from flask import Flask, jsonify, request, render_template
import os

app = Flask(__name__)

# --- RUTA PRINCIPAL ---
@app.route('/')
def home():
    return render_template('index.html')  # Carga una página HTML desde /templates

# --- EJEMPLO DE API REST ---
@app.route('/api/saludo', methods=['GET'])
def saludo():
    nombre = request.args.get('nombre', 'Mundo')
    return jsonify({'mensaje': f'Hola, {nombre}!'}), 200

# --- EJEMPLO POST ---
@app.route('/api/registrar', methods=['POST'])
def registrar():
    datos = request.get_json()
    if not datos or 'usuario' not in datos:
        return jsonify({'error': 'Falta el campo "usuario"'}), 400
    usuario = datos['usuario']
    return jsonify({'mensaje': f'Usuario {usuario} registrado correctamente!'}), 201

# --- MANEJO DE ERRORES ---
@app.errorhandler(404)
def error_404(e):
    return jsonify({'error': 'Ruta no encontrada'}), 404

@app.errorhandler(500)
def error_500(e):
    return jsonify({'error': 'Error interno del servidor'}), 500

# --- EJECUCIÓN EN RENDER ---
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render asigna automáticamente el puerto
    app.run(host='0.0.0.0', port=port)
