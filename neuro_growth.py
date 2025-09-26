
"""
neuro_growth.py
---------------
This module provides functionality for growing the neural network by generating new synaptic connections and updating the network map.
Part of the NeuroQuantumAI Android app project.
"""

import json
import random
import os
from typing import List, Union

MAP_FILE = "network_map.json"
def grow_network(user_text: str) -> str:
    """
    Rozbudowuje sieć neuronową na podstawie tekstu użytkownika.
    Tworzy nowe połączenie synaptyczne i zwraca komunikat.
    """
    # Prosta logika: każde słowo >3 znaki traktuj jako sygnał
    words = [w for w in user_text.split() if len(w) > 3]
    if not words:
        return "[Sieć] Brak wystarczających danych do rozbudowy sieci."
    target = words[0]
    sources = words[1:] if len(words) > 1 else ["AI"]
    msg = generate_synaptic_connection(sources, target)
    return f"[Sieć] {msg}"

def generate_synaptic_connection(source_signals: Union[str, List[str]], target: str) -> str:
    """
    Generate a synaptic connection from source signals to a target neuron and update the network map.
    Args:
        source_signals (Union[str, List[str]]): Source neuron(s) or signal(s).
        target (str): Target neuron or signal.
    Returns:
        str: Status message indicating success or error.
    """
    if not isinstance(source_signals, list):
        source_signals = [str(source_signals)]
    weight = round(random.uniform(0.75, 0.98), 2)
    try:
        if os.path.exists(MAP_FILE):
            with open(MAP_FILE, "r", encoding="utf-8") as f:
                map_data = json.load(f)
        else:
            map_data = {}
        for src in source_signals:
            key = f"{src}→{target}"
            map_data[key] = weight
        with open(MAP_FILE, "w", encoding="utf-8") as f:
            json.dump(map_data, f, indent=2)
        return f"🧠 Połączenie utworzone: {', '.join(source_signals)} → {target}, waga: {weight}"
    except Exception as e:
        return f"⚠️ Błąd synapsy: {e}"
