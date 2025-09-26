
"""
main.py
Główny plik uruchamiający aplikację neuronowo-kwantowej AI z interfejsem Kivy.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from AIEngine import AIEngine  # Centralny mózg AI

class ChatBox(BoxLayout):
    """
    Główny widget czatu. Integruje interfejs z silnikiem AI.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine = AIEngine()  # Inicjalizacja silnika AI

    def send_message(self):
        """
        Obsługuje wysyłanie wiadomości przez użytkownika i aktualizuje interfejs.
        """
        user_text = self.ids.user_input.text.strip()
        if not user_text:
            return
        try:
            # === Przetwarzanie wiadomości przez AIEngine ===
            response = self.engine.process_input(user_text)
        except Exception as e:
            response = f"[Błąd AI] {e}"

        # === Aktualizacja interfejsu ===
        self.ids.chat_log.text += f"\nUser: {user_text}\nAI:   {response}\n"
        self.ids.user_input.text = ""

class NeuroQuantumAIApp(App):
    """
    Klasa aplikacji Kivy. Buduje główny interfejs.
    """
    def build(self):
        return ChatBox()

if __name__ == "__main__":
    NeuroQuantumAIApp().run()
