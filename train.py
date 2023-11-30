import pickle
from model import create_model, train_model

if __name__ == "__main__":
    # Charger les données prétraitées
    with open('processed_data.pkl', 'rb') as file:
        processed_data = pickle.load(file)

    X_train = processed_data['X_train']
    y_train = processed_data['y_train']

    # Entraîner le modèle
    trained_model = train_model(X_train, y_train, epochs=10)

    # Sauvegarder le modèle entraîné
    trained_model.save('roman_numeral_model.h5')

    print("Entraînement terminé. Modèle sauvegardé sous 'roman_numeral_model.h5'.")
