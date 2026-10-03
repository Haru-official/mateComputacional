from flask import Flask
from PantallaPrincipal import principal_bp
from Manual import manual_bp
from Aleatorio import aleatorio_bp
from Algoritmo import algoritmo_bp
from Solucion import solucion_bp

app = Flask(__name__)

# Registramos todas las rutas
app.register_blueprint(principal_bp)
app.register_blueprint(manual_bp)
app.register_blueprint(aleatorio_bp)
app.register_blueprint(algoritmo_bp)
app.register_blueprint(solucion_bp)

if __name__ == '__main__':
    print("Iniciando Servidor TSP...")
    app.run(debug=True, port=5000)