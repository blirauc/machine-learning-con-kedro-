import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

# Cargar el modelo previamente entrenado
with open('model/tree_model_best.pkl', 'rb') as f:
    tree_model_best = pickle.load(f)

@app.route('/')
def index():
    return render_template('app.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos del frontend (asegúrate de enviar las características en formato JSON)
        data = request.get_json()
        features = data['features']

        # Convertir las características en un array de numpy
        features = np.array(features).reshape(1, -1)

        # Realizar la predicción
        prediction = tree_model_best.predict(features).tolist()

        # Devolver la predicción
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)