from flask import Blueprint, render_template, request
import random
import math

aleatorio_bp = Blueprint("aleatorio", __name__)


@aleatorio_bp.route("/aleatorio", methods=["POST"])
def aleatorio():
    try:
        n = int(request.form.get("nodos"))
    except (TypeError, ValueError):
        n = 5

    # Validación estricta según rúbrica para Agente Viajero
    if not (5 <= n <= 10):
        return render_template(
            "error.html",
            mensaje="El número de nodos debe estar entre 5 y 10 para el Agente Viajero.",
        )

    letras = [chr(65 + i) for i in range(n)]  # Genera A, B, C, D...

    # Matriz simétrica aleatoria para un grafo completo (garantiza ciclos hamiltonianos)
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            peso = random.randint(10, 100)
            matriz[i][j] = peso
            matriz[j][i] = peso

    aristas = (n * (n - 1)) // 2
    permutaciones = math.factorial(n - 1)
    ciclos_posibles = permutaciones // 2
    complejidad = f"O({n}!)"

    return render_template(
        "indexAleatorio.html",
        n=n,
        letras=letras,
        matriz=matriz,
        aristas=aristas,
        permutaciones=permutaciones,
        ciclos_posibles=ciclos_posibles,
        complejidad=complejidad,
    )
