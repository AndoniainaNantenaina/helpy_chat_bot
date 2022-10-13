from helpy import speech_engine

def say(text: str):
    """Fonction appelé pour énoncer vocalement un texte.
    
    Parameters
    ------------
    `text` : Une chaine de caractère contenant le texte à enoncer
    """
    speech_engine.say(text=text)
    speech_engine.runAndWait()
    return