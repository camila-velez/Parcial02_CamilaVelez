from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route("/factorial/<int:n>", methods=["GET"])
def factorial(n: int):
    if n < 0:
        return jsonify({"error": "El número debe ser entero no negativo"}), 400

    f = math.factorial(n)
    etiqueta = "par" if (n % 2 == 0) else "impar"  # 👈 ahora verifica el número recibido, no el factorial

    return jsonify({
        "numero_recibido": n,
        "factorial": f,
        "etiqueta": etiqueta
    }), 200

if __name__ == "__main__":
    # Para correr local: python app.py
    app.run(host="0.0.0.0", port=5000)
