import os
from helpy import trainer, chat

# Style de sortie console
import colorama 
colorama.init()
from colorama import Fore, Style

# Execution principale
if __name__ == "__main__":
    
    # Vérification si le model est déjà entrainé
    if os.path.exists('model\\chat_model.h5'):
        # Lancer directement le Chat
        print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
        chat.chat()
    else:
        # Faire entrainer le modèle en utilisant les données contenus dans le fichier intents.json
        trainer.loadAndTrainModel(jsonFile='.\\dataset\\bot\\intents.json')
        
        # Lancer le Chat
        print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
        chat.chat()
