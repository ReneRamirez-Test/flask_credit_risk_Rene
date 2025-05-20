# Predicción de Riesgo Crediticio

Este proyecto es una aplicación web construida con **Flask** que utiliza un modelo de **XGBoost** para predecir el riesgo crediticio de un usuario, basada en variables financieras personales.

---

##  Enlace a la aplicación en Render

 [https://flask-credit-risk-rene.onrender.com](https://flask-credit-risk-rene.onrender.com)

---

##  Estructura del Repositorio


flask_credit_risk_Rene/
│
├── modelo/
│ └── xgb_model.pkl # Modelo de XGBoost serializado
│
├── templates/
│ └── form.html # Formulario web (HTML)
│
├── app.py # Servidor Flask con lógica de predicción
├── requirements.txt # Dependencias necesarias
├── Procfile # Instrucción de inicio para Render
└── README.md # Documentación del proyecto


---

##  Variables del formulario

- **Revolving Utilization** (uso rotativo del crédito)
- **Edad**
- **Pagos tardíos 30-59 días**
- **Relación deuda/ingreso**
- **Líneas de crédito abiertas**
- **Pagos tardíos +90 días**
- **Propiedades inmobiliarias**
- **Pagos tardíos 60-89 días**
- **Dependientes**
- **Grupo de ingreso** (Muy Bajo, Bajo, Medio, Alto)

---

##  Ejecución local

```bash
# Clona el repositorio
git clone https://github.com/ReneRamirez-Test/flask_credit_risk_Rene.git
cd flask_credit_risk_Rene

# Crea y activa un entorno virtual
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta el servidor
python app.py


Despliegue en Render
Crea una cuenta en Render

Conecta tu cuenta de GitHub

Importa el repositorio flask_credit_risk_Rene

Configura:

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

Python Version: 3.x

Render generará una URL pública

** Detalles técnicos
Backend: Flask

Modelo: XGBoost serializado (joblib)

HTML: formulario con campos numéricos y dropdown

Producción: Render (free tier)

Autor
Rene Ramirez
Proyecto realizado para 4Geeks Academy
** GitHub: @ReneRamirez-Test

