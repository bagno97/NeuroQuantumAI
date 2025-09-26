"""
ai_shell.py
-----------
Wirtualny terminal i interpreter poleceń dla AI. Pozwala na uruchamianie poleceń Pythona i systemowych w bezpiecznym, kontrolowanym środowisku.
Może być używany przez AIEngine lub przez użytkownika do interakcji z AI na poziomie powłoki.
"""

import code
import subprocess
import sys
import threading

class AIShell:
    def __init__(self):
        self.locals = {}
        self.banner = "AI Virtual Shell (Python + system) — wpisz 'exit' aby zakończyć."

    def run_python_shell(self):
        """
        Uruchamia interaktywną powłokę Pythona (REPL) w kontekście AI.
        """
        code.interact(banner=self.banner, local=self.locals)

    def run_system_command(self, command: str) -> str:
        """
        Uruchamia polecenie systemowe i zwraca wynik.
        """
        if command.strip() == "exit":
            return "[AI Shell] Zakończono sesję."
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
            return result.stdout + (result.stderr if result.stderr else "")
        except Exception as e:
            return f"[AI Shell] Błąd: {e}"

    def start_shell(self):
        """
        Uruchamia prosty terminal tekstowy (Python + system).
        """
        print(self.banner)
        while True:
            try:
                cmd = input("AI> ").strip()
                if cmd == "exit":
                    print("[AI Shell] Zakończono.")
                    break
                elif cmd.startswith("py "):
                    # Uruchom kod Pythona
                    try:
                        exec(cmd[3:], self.locals)
                    except Exception as e:
                        print(f"[AI Shell] Błąd Pythona: {e}")
                else:
                    print(self.run_system_command(cmd))
            except (KeyboardInterrupt, EOFError):
                print("\n[AI Shell] Zakończono.")
                break

# Przykład użycia:
# shell = AIShell()
# shell.start_shell()
