import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

def create_model(input_dim, output_dim):
    model = Sequential()
    model.add(Embedding(input_dim=input_dim, output_dim=64, input_length=1))
    model.add(LSTM(100))
    model.add(Dense(1, activation='linear'))  # Sortie linéaire pour la régression

    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

def train_model(X_train, y_train, epochs=10):
    input_dim = len(set(X_train)) + 1  # Taille du vocabulaire
    output_dim = 1  # Sortie unique, le nombre arabe

    model = create_model(input_dim, output_dim)
    model.fit(X_train, y_train, epochs=epochs, verbose=1)

    return model

if __name__ == "__main__":
    # Charger les données prétraitées
    import pickle

    with open('processed_data.pkl', 'rb') as file:
        processed_data = pickle.load(file)

    X_train = processed_data['X_train']
    y_train = processed_data['y_train']

    # Entraîner le modèle
    trained_model = train_model(X_train, y_train)

    # Sauvegarder le modèle
    trained_model.save('roman_numeral_model.h5')
