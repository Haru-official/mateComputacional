from flask import Blueprint, render_template, request
import json

algoritmo_bp = Blueprint('algoritmo', __name__)

@algoritmo_bp.route('/algoritmo', methods=['POST'])
def algoritmo():
    matriz = json.loads(request.form.get('matriz'))
    letras = json.loads(request.form.get('letras'))
    n = len(letras)
    return render_template('indexAlgoritmo.html', n=n, letras=letras, matriz=matriz)