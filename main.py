import json 
import numpy as np
from tensorflow import keras
import os
import pyttsx3

# Engine utilisé pour le transformation de texte en vocal
speech_engine = pyttsx3.init()
voices = speech_engine.getProperty('voices')
speech_engine.setProperty("voice", voices[1].id)

from train_model import loadAndTrainModel

import colorama 
colorama.init()
from colorama import Fore, Style

import pickle

with open("intents.json") as file:
    data = json.load(file)


def chat():
    # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20
    
    while True:
        print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
        inp = input()
        if inp.lower() == "quit":
            break

        # Appel de la méthode de prédiction
        result = model.predict(
            keras.preprocessing.sequence.pad_sequences(
                tokenizer.texts_to_sequences([inp]),
                truncating='post', maxlen=max_len))
        
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

        for i in data['intents']:
            if i['tag'] == tag:
                answer = np.random.choice(i['responses'])
                print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL , answer)
                say(answer.__str__())

def say(text: str):
    speech_engine.say(text=text)
    speech_engine.runAndWait()
    return

# Execution principale
if __name__ == "__main__":
    
    # Vérification si le model est déjà entrainé
    if os.path.exists('chat_model'):
        print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
        chat()
    else:
        loadAndTrainModel('intents.json')
        print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
        chat()
