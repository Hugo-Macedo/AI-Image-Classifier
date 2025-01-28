# CIFAR-10 Image Classifier using ONNX & Flask

## 📌 Description
Ce projet est une application de classification d'images basée sur un modèle de deep learning entraîné sur le dataset **CIFAR-10**. Le modèle a été entraîné avec **PyTorch**, exporté en **ONNX**, et est utilisé dans une API Flask pour faire des prédictions en temps réel.

## 🏗️ Structure du projet
```
/project
│
├── /data                  # Dossier contenant les données CIFAR-10 téléchargées
├── /frontend              # Dossier contenant l'interface utilisateur
│   └── index.html         # Interface web pour charger une image et obtenir la prédiction
├── improved_net.onnx      # Modèle exporté au format ONNX
├── server.py              # Code backend Flask
├── requirements.txt       # Dépendances Python
├── .gitignore             # Fichiers à ignorer dans Git
└── README.md              # Documentation du projet
```

## 📦 Installation
1️⃣ **Cloner le dépôt**
```bash
git clone <URL_DU_REPO>
cd project
```

2️⃣ **Créer un environnement virtuel et installer les dépendances**
```bash
python -m venv venv
source venv/bin/activate  # Sur Linux/Mac
venv\Scripts\activate  # Sur Windows
pip install -r requirements.txt
```

## 🚀 Utilisation
### 1️⃣ Lancer le serveur Flask
```bash
python server.py
```
Le serveur démarrera sur `http://127.0.0.1:5000/`

### 2️⃣ Ouvrir l'interface utilisateur
Si vous utilisez Python, démarrez un serveur HTTP local dans `/frontend` :
```bash
cd frontend
python -m http.server 8000
```
Puis ouvrez **http://127.0.0.1:8000/index.html** dans votre navigateur.

## 🧠 Fonctionnalités
- 🎯 **Classification d'images en 10 catégories** (avion, voiture, oiseau, etc.)
- ⚡ **Modèle optimisé avec ONNX Runtime** pour des prédictions rapides
- 🌐 **Interface web** permettant d'uploader une image et d'afficher la prédiction
- 🔥 **Support des images PNG, JPG** avec conversion automatique

---
🚀 **Développeur** : Hugo-Macedo

