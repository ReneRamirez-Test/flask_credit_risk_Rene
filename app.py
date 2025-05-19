# App.py — API básica Flask para predicción de riesgo crediticio

from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Cargar modelo entrenado
modelo_path = os.path.join("modelo", "xgb_model.pkl")
modelo = joblib.load(modelo_path)

@app.route('/')
def home():
    return render_template("form.html")

@app.route('/predecir', methods=["POST"])
def predecir():
    try:
        # Obtener datos del formulario
        datos = [
            float(request.form["rev_util"]),
            float(request.form["age"]),
            float(request.form["late_30_59"]),
            float(request.form["debt_ratio"]),
            float(request.form["open_credit"]),
            float(request.form["late_90"]),
            float(request.form["real_estate"]),
            float(request.form["late_60_89"]),
            float(request.form["dependents"]),
            request.form["ingreso_grupo"]
        ]

        # Codificación one-hot manual de ingreso_grupo
        ingreso_labels = ["Muy Bajo", "Bajo", "Medio", "Alto", "Muy Alto", "Extremo"]
        ingreso_dummies = [1 if datos[9] == label else 0 for label in ingreso_labels]

        # Concatenar las variables numéricas + las dummies
        entrada = np.array(datos[:9] + ingreso_dummies).reshape(1, -1)

        # Predecir
        prediccion = modelo.predict(entrada)[0]
        resultado = "⚠️ Riesgo Crediticio" if prediccion == 1 else "✅ Cliente Confiable"

    except Exception as e:
        resultado = f"❌ Error al procesar los datos: {str(e)}"

    return render_template("form.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
