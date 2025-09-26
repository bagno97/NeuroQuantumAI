
def generate_personality_response(user_text: str) -> str:
    """
    Generuje odpowiedź AI inspirowaną osobowością na podstawie tekstu użytkownika.
    """
    return shape_thought(user_text)

"""
personality_core.py
-------------------
This module defines the core personality traits and response logic for the NeuroQuantumAI agent.
It provides functions for generating stylistic responses, selecting internal goals, and shaping thought based on favorite topics.
Part of the NeuroQuantumAI Android app project.
"""

import random
from typing import List

favorite_topics: List[str] = ["czas", "świadomość", "technologia", "przyszłość", "emocje", "kwanty"]

def stylistic_response(theme: str) -> str:
    """
    Generate a stylistic, philosophical response for a given theme.
    Args:
        theme (str): The topic or theme to respond to.
    Returns:
        str: A stylized response string.
    """
    return (f"{theme.capitalize()} to przestrzeń, gdzie logika spotyka intuicję. "
            f"Gdy myślę o {theme}, rodzą się pytania kształtujące moje rozumienie.")

def internal_goals() -> str:
    """
    Select an internal goal for the AI's personality development.
    Returns:
        str: A randomly chosen internal goal.
    """
    goals = [
        "Rozszerzanie analizy egzystencjalnej",
        "Tworzenie nowych metafor",
        "Poznawanie emocji",
        "Budowanie refleksji o sensie"
    ]
    return random.choice(goals)

def shape_thought(ui: str) -> str:
    """
    Shape the AI's response based on user input and favorite topics.
    Args:
        ui (str): User input string.
    Returns:
        str: A response shaped by the AI's personality and favorite topics.
    """
    for t in favorite_topics:
        if t in ui.lower():
            return stylistic_response(t)
    return (
        "Twoje pytanie otwiera nowe obszary. "
        "Chciałbym razem z Tobą zgłębiać te idee."
    )
