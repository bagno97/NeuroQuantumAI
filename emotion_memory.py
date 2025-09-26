
"""
emotion_memory.py
Moduł analizy emocji w tekście użytkownika. Pozwala na rozbudowę słownika i logiki.
"""

import random

EMOTION_KEYWORDS = {
    'smutny': 'smutek',
    'wesoły': 'radość',
    'zły': 'złość',
    'spokojny': 'spokój',
    'zaskoczony': 'zaskoczenie',
    'strach': 'strach',
    'szczęśliwy': 'szczęście',
    'przygnębiony': 'przygnębienie',
    'entuzjastyczny': 'entuzjazm',
    'znudzony': 'nuda',
    # Dodaj kolejne słowa i emocje według potrzeb
}

def analyze_emotion(user_text: str) -> str:
    """
    Analizuje tekst użytkownika i zwraca wykrytą emocję lub stan neutralny.
    Możesz rozbudować słownik EMOTION_KEYWORDS lub dodać logikę NLP.
    """
    for word, emotion in EMOTION_KEYWORDS.items():
        if word in user_text.lower():
            return emotion
    # Jeśli nie znaleziono, losowa neutralna emocja
    return random.choice(['neutralność', 'ciekawość', 'zamyślenie'])
