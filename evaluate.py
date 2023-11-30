import pickle
from model import create_model
from sklearn.metrics import mean_absolute_error

if __name__ == "__main__":
    # Charger les données prétraitées
    with open('processed_data.pkl', 'rb') as file:
        processed_data = pickle.load(file)

    X_test = processed_data['X_test']
    y_test = processed_data['y_test']

    # Charger le modèle entraîné
    trained_model = create_model(len(set(X_test)) + 1, 1)  # Assurez-vous de créer le même modèle que celui utilisé pour l'entraînement
    trained_model.load_weights('roman_numeral_model.h5')

    # Faire des prédictions sur l'ensemble de test
    y_pred = trained_model.predict(X_test)

    # Calculer et imprimer l'erreur absolue moyenne
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Erreur absolue moyenne sur l'ensemble de test : {mae}")
