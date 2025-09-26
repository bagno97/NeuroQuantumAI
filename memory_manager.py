
def manage_memory(user_text: str, response: str) -> None:
    """
    Dodaje interakcję użytkownika i AI do pliku ai_memory.txt jako prostą pamięć rozmów.
    """
    try:
        with open("ai_memory.txt", "a", encoding="utf-8") as f:
            f.write(f"[Ty] {user_text}\n[AI] {response}\n")
    except Exception as e:
        print(f"[Memory] Błąd zapisu pamięci: {e}")

"""
memory_manager.py
Moduł zarządzający długoterminową pamięcią AI. Pozwala na aktualizację i przywoływanie wspomnień.
"""

import random

def update_long_memory():
    """
    Przetwarza plik ai_memory.txt i zapisuje kluczowe wspomnienia do long_memory.txt.
    Wspomnienia muszą być odpowiednio długie i oznaczone jako [Ty] lub [AI].
    """
    try:
        lines = open("ai_memory.txt", "r", encoding="utf-8").read().splitlines()
    except FileNotFoundError:
        return
    mem = set()
    for l in lines:
        if l.startswith("[Ty]") or l.startswith("[AI]"):
            text = l.split(']', 1)[1].strip()
            if len(text) > 30:
                mem.add(text)
    if mem:
        with open("long_memory.txt", "w", encoding="utf-8") as f:
            f.write("# Kluczowe wspomnienia:\n")
            for m in mem:
                f.write(f"- {m}\n")

def recall_from_memory() -> str:
    """
    Losowo przywołuje jedno kluczowe wspomnienie z long_memory.txt.
    """
    try:
        lines = [l for l in open("long_memory.txt", "r", encoding="utf-8") if l.startswith("-")]
        return random.choice(lines).lstrip("- ").strip()
    except Exception:
        return "Pamięć pusta."
