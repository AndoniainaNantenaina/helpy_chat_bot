# Importation des packages nécéssaires

import json 
import numpy as np 
import pickle
from keras.models import Sequential
from keras.layers import Dense, Embedding, GlobalAveragePooling1D
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder

def loadAndTrainModel(jsonFile : str):
    
    # Charger les données dans le fichier JSON dans data
    with open(jsonFile) as file:
        data = json.load(file)
        
    # Variables
    training_sentences = []     # Contenant les données de formation
    training_labels = []        # Contenant toutes les étiquettes cibles correspondant à chaque donnée de formation.
    labels = []                 # Contenant les étiquettes
    responses = []              # Contenant les réponses dans le fichier

    # Itération sur les intents
    for intent in data['intents']:
        
        # Ajouter les données dans les variables
        for pattern in intent['patterns']:
            training_sentences.append(pattern)
            training_labels.append(intent['tag'])
        
        responses.append(intent['responses'])
        
        if intent['tag'] not in labels:
            labels.append(intent['tag'])
            
    # Variables contenant le nombre de classe trouvés dans le fichier Json
    num_classes = len(labels)

    # Conversion des étiquettes cibles en une forme compréhensible de modèle.
    lbl_encoder = LabelEncoder()                                # Déclarer l'encodeur
    lbl_encoder.fit(training_labels)                            # Adapter les données
    training_labels = lbl_encoder.transform(training_labels)    # Transformation

    # Ensuite, nous vectorisons notre corpus de données textuelles en utilisant la classe "Tokenizer" 
    # et cela nous permet de limiter la taille de notre vocabulaire jusqu'à un certain nombre défini. 
    # Lorsque nous utilisons cette classe pour la tâche de prétraitement du texte, par défaut, toutes les ponctuations 
    # seront supprimées, transformant les textes en séquences de mots séparés par des espaces, et ces séquences 
    # sont ensuite divisées en listes de jetons. Ils seront ensuite indexés ou vectorisés. 
    # Nous pouvons également ajouter "oov_token" qui est une valeur pour "out of token" pour 
    # traiter les mots hors vocabulaire (tokens) au moment de l'inférence.

    vocab_size = 1000
    embedding_dim = 16
    max_len = 20
    oov_token = "<OOV>"

    tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
    tokenizer.fit_on_texts(training_sentences)
    word_index = tokenizer.word_index
    sequences = tokenizer.texts_to_sequences(training_sentences)

    # Mettre les séquences de texte d'apprentissage en même taille.
    padded_sequences = pad_sequences(sequences, truncating='post', maxlen=max_len) 


    # Entrainement du model

    # Architecture de réseau de neurones pour le modèle proposé
    model = Sequential()

    model.add(
        Embedding(
            vocab_size, 
            embedding_dim, 
            input_length=max_len))
    model.add(GlobalAveragePooling1D())
    model.add(Dense(16, activation='relu'))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))

    model.compile(
        loss='sparse_categorical_crossentropy', 
        optimizer='adam', metrics=['accuracy'])

    model.summary()

    # Passage à l'entrainement du model
    epochs = 500
    history = model.fit(
        padded_sequences, 
        np.array(training_labels), 
        epochs=epochs)

    # Sauvegarde du model déjà entrainé
    model.save("chat_model")

    # Enregistrement du tokenizer adapté/ajusté
    with open('tokenizer.pickle', 'wb') as handle:
        pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
    # Enregistrement de l'encodeur d'étiquette adapté/ajusté
    with open('label_encoder.pickle', 'wb') as ecn_file:
        pickle.dump(lbl_encoder, ecn_file, protocol=pickle.HIGHEST_PROTOCOL)    
        
    return
