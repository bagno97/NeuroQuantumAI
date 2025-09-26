
"""
background_tasks.py
Moduł do uruchamiania cyklicznych zadań w tle (np. aktualizacja pamięci, logów, synchronizacja).
Możesz łatwo dodać kolejne zadania cykliczne do listy TASKS.
"""

from threading import Thread
from time import sleep
from memory_manager import update_long_memory

def periodic_task(func, interval_sec):
    """Uruchamia podaną funkcję cyklicznie co interval_sec sekund w osobnym wątku."""
    def loop():
        while True:
            try:
                func()
            except Exception as e:
                print(f"[background_tasks] Błąd w zadaniu {func.__name__}: {e}")
            sleep(interval_sec)
    Thread(target=loop, daemon=True).start()

# Lista zadań cyklicznych: (funkcja, interwał w sekundach)
TASKS = [
    (update_long_memory, 3600),  # co godzinę aktualizuj długą pamięć
    # Dodaj kolejne zadania tutaj, np. (twoja_funkcja, 600)
]

for func, interval in TASKS:
    periodic_task(func, interval)
