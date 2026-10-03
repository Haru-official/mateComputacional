from flask import Blueprint, render_template, request
import json

manual_bp = Blueprint("manual", __name__)


def verificar_ciclo_hamiltoniano(matriz, n):
    for i in range(n):
        # Contar conexiones válidas (pesos > 0) para cada nodo
        conexiones = sum(1 for j in range(n) if matriz[i][j] > 0 and i != j)
        if conexiones < 2:
            return (
                False,
                f"El nodo {chr(65 + i)} tiene menos de 2 conexiones. Se requieren al menos 2 para formar un ciclo hamiltoniano.",
            )
    return True, "Estructura válida para ciclos hamiltonianos."


# Ruta para mostrar el formulario inicial del tamaño manual (Validando el rango [5, 10])
@manual_bp.route("/manual", methods=["POST"])
def manual():
    try:
        n = int(request.form.get("nodos"))
    except (TypeError, ValueError):
        n = 5

    if not (5 <= n <= 10):
        return render_template(
            "error.html",
            mensaje="El número de nodos debe estar entre 5 y 10 para el Agente Viajero.",
        )

    letras = [chr(65 + i) for i in range(n)]
    return render_template("indexManual.html", n=n, letras=letras)


@manual_bp.route("/procesar_manual", methods=["POST"])
def procesar_manual():
    matriz = json.loads(request.form.get("matriz"))
    letras = json.loads(request.form.get("letras"))
    n = len(letras)

    es_valido, mensaje = verificar_ciclo_hamiltoniano(matriz, n)

    if not es_valido:
        # Si no es válido, regresamos
        return render_template(
            "indexManual.html", n=n, letras=letras, error=mensaje, matriz=matriz
        )

    # Si es válido -> solución por fuerza bruta
    return render_template("indexAlgoritmo.html", n=n, letras=letras, matriz=matriz)
