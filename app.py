from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route("/factorial/<int:n>", methods=["GET"])
def factorial(n: int):
    # Validaciones sencillas
    if n < 0:
        return jsonify({
            "error": "El número debe ser entero no negativo"
        }), 400

    # Cálculo del factorial (math.factorial maneja enteros grandes)
    f = math.factorial(n)
    etiqueta = "par" if (f % 2 == 0) else "impar"

    return jsonify({
        "numero_recibido": n,
        "factorial": f,
        "etiqueta": etiqueta
    }), 200

@app.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "uso": "GET /factorial/<n>  (n entero no negativo)"
    }), 200

if __name__ == "__main__":
    # Para correr local: python app.py
    app.run(host="0.0.0.0", port=5000)
