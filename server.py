from flask import Flask, request, jsonify
import onnxruntime as ort
import numpy as np
from PIL import Image
from flask_cors import CORS

# Charger le modèle ONNX
session = ort.InferenceSession("improved_net.onnx")

# Classes disponibles
classes = ['avion', 'automobile', 'oiseau', 'chat', 'cerf', 'chien', 'grenouille', 'cheval', 'bateau', 'camion']

app = Flask(__name__)
CORS(app)

def preprocess_image(image):
    # Redimensionner et normaliser l'image (32x32 pour CIFAR-10)
    image = image.resize((32, 32))
    image_array = np.array(image).astype('float32') / 255.0
    image_array = (image_array - 0.5) / 0.5  # Normalisation comme à l'entraînement
    image_array = np.transpose(image_array, (2, 0, 1))  # Changer l'ordre des dimensions (C, H, W)
    image_array = np.expand_dims(image_array, axis=0)  # Ajouter une dimension pour le batch
    return image_array

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    image = Image.open(file).convert('RGB')
    input_tensor = preprocess_image(image)

    # Faire la prédiction
    outputs = session.run(None, {'input': input_tensor})
    predicted_class = np.argmax(outputs[0])

    return jsonify({'predicted_class': classes[predicted_class]})

if __name__ == '__main__':
    app.run(debug=True)
