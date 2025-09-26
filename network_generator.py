
def generate_new_nodes() -> str:
    """
    Generuje nowe moduły tematyczne na podstawie historii rozmów (jeśli dostępna).
    """
    import os, json
    if os.path.exists("conversation_history.json"):
        with open("conversation_history.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = [{"user": "przykładowy temat"}]
    result = evolve_network_from_data(data)
    return f"[Sieć] {result}"

"""
network_generator.py
Moduł do automatycznego generowania i ewolucji tematycznych modułów AI na podstawie danych użytkownika.
"""

import os
import json
from datetime import datetime

def evolve_network_from_data(data, target_folder="modules", registry_file="modules.json"):
    """
    Generuje lub aktualizuje moduły tematyczne na podstawie słów kluczowych z historii użytkownika.
    Każdy temat otrzymuje osobny plik z funkcją process().
    """
    # Tworzenie folderu docelowego, jeśli nie istnieje
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Wyodrębnianie słów kluczowych z danych użytkownika
    keywords = set()
    for entry in data:
        user_input = entry.get("user", "")
        keywords.update(user_input.lower().split())

    generated = []
    for word in keywords:
        filename = os.path.join(target_folder, f"{word}.py")
        timestamp = datetime.utcnow().isoformat() + "Z"

        if not os.path.exists(filename):
            # Tworzenie nowego modułu
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# Moduł tematyczny: {word}\n\n")
                f.write("def process(input):\n")
                f.write(f"    # Logika dla: {word}\n")
                f.write(f"    return f'Analiza {word}: {{input}}'\n")

            status = "created"
        else:
            # Ewolucja istniejącego modułu
            with open(filename, 'r+', encoding='utf-8') as f:
                content = f.read()
                if "# [ewolucja]" not in content:
                    content += f"\n# [ewolucja] Moduł zaktualizowany {timestamp} na podstawie nowych danych.\n"
                    f.seek(0)
                    f.write(content)
                    f.truncate()
            status = "updated"

        # Rejestracja zmiany
        generated.append({
            "module": f"{word}.py",
            "topic": word,
            "source": "network_generator",
            "status": status,
            "timestamp": timestamp
        })

    # Aktualizacja pliku rejestru
    if generated:
        if os.path.exists(registry_file):
            try:
                with open(registry_file, 'r', encoding='utf-8') as reg:
                    registry = json.load(reg)
            except json.JSONDecodeError:
                registry = []
        else:
            registry = []

        registry.extend(generated)

        with open(registry_file, 'w', encoding='utf-8') as reg:
            json.dump(registry, reg, indent=2, ensure_ascii=False)

    return f"Zaktualizowano {len(generated)} modułów."
