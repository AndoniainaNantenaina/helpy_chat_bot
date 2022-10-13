import pickle, keras
from colorama import Fore, Style
from keras_preprocessing import sequence as seq
from helpy import data, speech
import numpy as np

def chat():
    """Fonction de chat
    """
    # Charger le modèle entrainé
    model = keras.models.load_model('model\\chat_model.h5')

    # Charger l'objet tokenizer
    with open('model\\tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # Charger l'objet d'encodeur de label
    with open('model\\label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20
    
    while True:
        print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
        
        # Prendre l'entrée utilisateur
        user_input = input()
        
        if user_input.lower() == "quit":
            break

        # Appel de la méthode de prédiction
        result = model.predict(
            seq.pad_sequences(
                tokenizer.texts_to_sequences([user_input]),
                truncating='post', maxlen=max_len))
        
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

        for i in data['intents']:
            if i['tag'] == tag:
                answer = np.random.choice(i['responses'])
                print(Fore.GREEN + "Helpy:" + Style.RESET_ALL , answer)
                speech.say(answer.__str__())
