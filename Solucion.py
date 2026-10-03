from flask import Blueprint, render_template, request
import json
import itertools

solucion_bp = Blueprint('solucion', __name__)

@solucion_bp.route('/solucion', methods=['POST'])
def solucion():
    matriz = json.loads(request.form.get('matriz'))
    letras = json.loads(request.form.get('letras'))
    n = len(letras)

    # MOTOR PYTHON: Ejecución de Fuerza Bruta para encontrar la solución
    nodos_intermedios = list(range(1, n))
    todas_permutaciones = list(itertools.permutations(nodos_intermedios))
    
    ciclos = []
    for perm in todas_permutaciones:
        ruta = [0] + list(perm) + [0]
        costo_total = 0
        es_valido = True
        
        for i in range(len(ruta)-1):
            peso = matriz[ruta[i]][ruta[i+1]]
            if peso == 0:  # Si no hay conexión (en manual)
                es_valido = False
                break
            costo_total += peso
            
        if es_valido:
            # Evitar duplicados inversos (A-B-C-A es igual a A-C-B-A en costo)
            ruta_inversa = ruta[::-1]
            if not any(c['ruta'] == ruta_inversa for c in ciclos):
                ruta_letras = [letras[idx] for idx in ruta]
                ciclos.append({'ruta_indices': ruta, 'ruta': ruta_letras, 'costo': costo_total})

    # Ordenar de menor a mayor costo
    ciclos.sort(key=lambda x: x['costo'])
    
    mejor_ciclo = ciclos[0] if ciclos else None

    return render_template('indexSolucion.html', n=n, letras=letras, matriz=matriz, 
                           ciclos=ciclos, mejor=mejor_ciclo)