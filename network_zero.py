
"""
network_zero.py
Moduł tematyczny: analiza podstawowych cech tekstu użytkownika.
"""

def process_input_zero(text: str):
    """
    Zwraca słownik z długością tekstu i informacją, czy to pytanie.
    """
    return {
        'length': len(text),
        'is_question': text.strip().endswith('?')
    }
