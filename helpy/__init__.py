import pyttsx3, json

# Engine utilisé pour le transformation de texte en vocal
speech_engine = pyttsx3.init()

# Prendre les propriétés de voix
voices = speech_engine.getProperty('voices')

# Mettre en langue anglaise
speech_engine.setProperty("voice", voices[1].id)

# Charger le dataset
with open("intents.json") as file:
    data = json.load(file)
    