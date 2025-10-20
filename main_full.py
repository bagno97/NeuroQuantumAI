
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
        ROZSZERZONA obsługa wysyłania wiadomości - teraz z pełną funkcjonalnością!
        """
        user_text = self.ids.user_input.text.strip()
        if not user_text:
            return
        try:
            # === Przetwarzanie wiadomości przez AIEngine ===
            response = self.engine.process_input(user_text)
            
            # === Sprawdź czy to komenda telefonu/samomodyfikacji ===
            phone_keywords = ["zrób zdjęcie", "lokalizacja", "sms", "bateria", "wifi"]
            mod_keywords = ["modyfikuj", "utwórz moduł", "dodaj funkcję"]
            
            if any(kw in user_text.lower() for kw in phone_keywords):
                response = "📱 " + response
            elif any(kw in user_text.lower() for kw in mod_keywords):
                response = "🔧 " + response
                
        except Exception as e:
            response = f"❌ [Błąd AI] {e}"

        # === Aktualizacja interfejsu z kolorami ===
        self.ids.chat_log.text += f"\n👤 User: {user_text}\n🤖 AI: {response}\n{'-'*50}"
        self.ids.user_input.text = ""
    
    # Alias dla kompatybilności z .kv
    def send(self):
        self.send_message()

class NeuroQuantumAIApp(App):
    """
    Klasa aplikacji Kivy. Buduje główny interfejs.
    """
    def build(self):
        return ChatBox()

if __name__ == "__main__":
    NeuroQuantumAIApp().run()
