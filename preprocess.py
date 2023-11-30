import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Charger le dataset
df = pd.read_csv('dataset.csv')

# Séparer les données en features (X) et labels (y)
X = df['Chiffre_Romain']
y = df['Nombre_Arabe']

# Encoder les chiffres romains en valeurs numériques
label_encoder = LabelEncoder()
X_encoded = label_encoder.fit_transform(X)

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Enregistrez les données prétraitées pour une utilisation ultérieure
processed_data = {
    'X_train': X_train,
    'X_test': X_test,
    'y_train': y_train,
    'y_test': y_test,
    'label_encoder': label_encoder
}

# Sauvegardez les données prétraitées dans un fichier pickle
import pickle

with open('processed_data.pkl', 'wb') as file:
    pickle.dump(processed_data, file)
