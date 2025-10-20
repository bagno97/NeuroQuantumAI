"""
main_android_fixed.py
NAPRAWIONY główny plik dla Androida - rozwiązuje problem minimalizowania
"""

import os
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.logger import Logger
from kivy.utils import platform

# Android-specific imports
if platform == 'android':
    from android.runnable import run_on_ui_thread
    from jnius import autoclass, cast
    from android import activity
    
    # Android classes
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Intent = autoclass('android.content.Intent')
    PendingIntent = autoclass('android.app.PendingIntent')

# Bezpieczny import AIEngine dla Androida
try:
    from AIEngine_android import AIEngine
    Logger.info("MAIN: Używam AIEngine_android - pełna funkcjonalność")
except ImportError:
    try:
        from AIEngine import AIEngine
        Logger.info("MAIN: Używam standardowy AIEngine")
    except ImportError as e:
        Logger.error(f"MAIN: Błąd importu AIEngine: {e}")
        class AIEngine:
            def process_input(self, text):
                return f"🤖 NeuroQuantumAI (tryb awaryjny): {text}"

class ChatBox(BoxLayout):
    """
    Główny widget czatu z Android-specific fixes
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine = AIEngine()
        Logger.info("ChatBox: Inicjalizacja zakończona")
        
        # Android-specific initialization
        if platform == 'android':
            self.setup_android()

    def setup_android(self):
        """
        Konfiguracja specyficzna dla Androida
        """
        try:
            # Zabezpieczenie przed minimalizowaniem
            activity.bind(on_pause=self.on_android_pause)
            activity.bind(on_resume=self.on_android_resume)
            Logger.info("ChatBox: Android lifecycle bind successful")
        except Exception as e:
            Logger.error(f"ChatBox: Android setup error: {e}")

    def on_android_pause(self):
        """
        Obsługa pauzowania aplikacji
        """
        Logger.info("ChatBox: Android app paused")
        return True  # Pozwól na pauzę

    def on_android_resume(self):
        """
        Obsługa wznawiania aplikacji
        """
        Logger.info("ChatBox: Android app resumed")

    def send_message(self):
        """
        Wysyłanie wiadomości z logowaniem
        """
        user_text = self.ids.user_input.text.strip()
        if not user_text:
            return
            
        Logger.info(f"ChatBox: Processing message: {user_text}")
        
        try:
            response = self.engine.process_input(user_text)
            
            # Sprawdź typ komendy
            phone_keywords = ["zrób zdjęcie", "lokalizacja", "sms", "bateria", "wifi"]
            mod_keywords = ["modyfikuj", "utwórz moduł", "dodaj funkcję"]
            
            if any(kw in user_text.lower() for kw in phone_keywords):
                response = "📱 " + response
            elif any(kw in user_text.lower() for kw in mod_keywords):
                response = "🔧 " + response
                
        except Exception as e:
            Logger.error(f"ChatBox: AI processing error: {e}")
            response = f"❌ [Błąd AI] {e}"

        # Aktualizacja interfejsu
        self.ids.chat_log.text += f"\n👤 User: {user_text}\n🤖 AI: {response}\n{'-'*50}"
        self.ids.user_input.text = ""
        Logger.info("ChatBox: Message processed successfully")
    
    def send(self):
        self.send_message()

class NeuroQuantumAIApp(App):
    """
    Klasa aplikacji z Android fixes
    """
    def build(self):
        Logger.info("App: Building interface")
        return ChatBox()

    def on_start(self):
        """
        Callback po starcie aplikacji
        """
        Logger.info("App: Application started")
        if platform == 'android':
            self.setup_android_window()

    def setup_android_window(self):
        """
        Konfiguracja okna dla Androida
        """
        try:
            # Ustaw flagę aby aplikacja pozostała aktywna
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            WindowManager = autoclass('android.view.WindowManager$LayoutParams')
            
            activity = PythonActivity.mActivity
            window = activity.getWindow()
            
            # Dodaj flagi aby zapobiec minimalizowaniu
            window.addFlags(WindowManager.FLAG_KEEP_SCREEN_ON)
            window.addFlags(WindowManager.FLAG_SHOW_WHEN_LOCKED)
            window.addFlags(WindowManager.FLAG_TURN_SCREEN_ON)
            
            Logger.info("App: Android window flags set successfully")
        except Exception as e:
            Logger.error(f"App: Android window setup error: {e}")

    def on_pause(self):
        """
        Obsługa pauzowania aplikacji
        """
        Logger.info("App: Application paused")
        return True

    def on_resume(self):
        """
        Obsługa wznawiania aplikacji
        """
        Logger.info("App: Application resumed")

if __name__ == "__main__":
    Logger.info("Starting NeuroQuantumAI Android App")
    NeuroQuantumAIApp().run()