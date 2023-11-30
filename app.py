import tkinter as tk
from tkinter import ttk
from model import create_model
import pickle


class RomanNumeralApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reconnaissance des Chiffres Romains")

        # Charger le modèle entraîné
        with open('processed_data.pkl', 'rb') as file:
            processed_data = pickle.load(file)

        self.label_encoder = processed_data['label_encoder']
        self.trained_model = create_model(len(self.label_encoder.classes_) + 1, 1)
        self.trained_model.load_weights('roman_numeral_model.h5')

        # Interface utilisateur
        self.create_widgets()

    def create_widgets(self):
        # Libellé d'instruction
        self.label_instruction = ttk.Label(self.root, text="Entrez un chiffre romain :")
        self.label_instruction.grid(row=0, column=0, padx=10, pady=10)

        # Champ de saisie
        self.entry_roman_numeral = ttk.Entry(self.root)
        self.entry_roman_numeral.grid(row=0, column=1, padx=10, pady=10)

        # Bouton de prédiction
        self.btn_predict = ttk.Button(self.root, text="Prédire", command=self.predict_numeral)
        self.btn_predict.grid(row=1, column=0, columnspan=2, pady=10)

        # Résultat de la prédiction
        self.label_result = ttk.Label(self.root, text="")
        self.label_result.grid(row=2, column=0, columnspan=2, pady=10)

    def predict_numeral(self):
        # Récupérer la saisie de l'utilisateur
        input_roman_numeral = self.entry_roman_numeral.get()

        # Encoder le chiffre romain
        input_encoded = self.label_encoder.transform([input_roman_numeral])[0]

        # Faire une prédiction avec le modèle
        prediction = self.trained_model.predict([input_encoded])[0][0]

        # Afficher le résultat de la prédiction
        self.label_result.config(text=f"La prédiction en chiffres arabes est : {round(prediction)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = RomanNumeralApp(root)
    root.mainloop()
