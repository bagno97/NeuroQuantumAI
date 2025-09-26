
"""
network_one.py
Moduł tematyczny: rozpoznawanie kluczowych pojęć w tekście użytkownika.
"""

KEYS = ['czas', 'świadomość', 'technologia', 'emocje', 'lokalizacja']

def process_input_one(text: str):
    """
    Zwraca listę kluczowych pojęć znalezionych w tekście użytkownika.
    Jeśli nie znaleziono, zwraca ['ogólne'].
    """
    found = [k for k in KEYS if k in text.lower()]
    return found or ['ogólne']
