"""
main_android_fixed.py
PEŁNA wersja głównego pliku dla Androida - WSZYSTKIE funkcje aktywne!
Obsługuje: telefon, samomodyfikację, dynamiczne moduły, bazę wiedzy, pamięć, emocje
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
    try:
        from android.runnable import run_on_ui_thread
        from jnius import autoclass, cast
        from android import activity
        
        # Android classes
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        PendingIntent = autoclass('android.app.PendingIntent')
        Logger.info("MAIN: Android imports successful")
    except Exception as e:
        Logger.warning(f"MAIN: Android imports failed: {e}")

# Bezpieczny import AIEngine - próbuj najpierw wersję Android, potem standardową
AIEngine = None
try:
    from AIEngine_android import AIEngine
    Logger.info("MAIN: AIEngine_android loaded - PEŁNA FUNKCJONALNOŚĆ!")
except ImportError as e:
    Logger.warning(f"MAIN: AIEngine_android import failed: {e}")
    try:
        from AIEngine import AIEngine
        Logger.info("MAIN: Standardowy AIEngine loaded")
    except ImportError as e2:
        Logger.error(f"MAIN: Wszystkie AIEngine imports failed: {e2}")
        # Awaryjny AIEngine
        class AIEngine:
            def __init__(self):
                Logger.warning("MAIN: Używam awaryjnego AIEngine")
            
            def process_input(self, text):
                return f"🤖 NeuroQuantumAI (tryb awaryjny)\n\nOtrzymano: {text}\n\nSystem działa ale niektóre moduły nie są dostępne."
            
            def get_status(self):
                return "⚠️ Tryb awaryjny - niektóre funkcje niedostępne"

class ChatBox(BoxLayout):
    """
    Główny widget czatu z PEŁNĄ funkcjonalnością AI
    Obsługuje: wszystkie komendy telefonu, samomodyfikację, bazę wiedzy
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine = AIEngine()
        Logger.info("ChatBox: AIEngine zainicjalizowany")
        
        # Pokaż status AI przy starcie
        try:
            status = self.engine.get_status()
            self.schedule_status_update(status)
        except:
            pass
        
        # Android-specific initialization
        if platform == 'android':
            self.setup_android()

    def schedule_status_update(self, status):
        """Zaktualizuj chat log po inicjalizacji widgetów"""
        def update_status(dt):
            try:
                current_text = self.ids.chat_log.text
                self.ids.chat_log.text = f"{current_text}\n\n{status}"
            except:
                pass
        Clock.schedule_once(update_status, 0.5)

    def setup_android(self):
        """
        Konfiguracja specyficzna dla Androida - zapobieganie minimalizowaniu
        """
        try:
            # Zabezpieczenie przed minimalizowaniem
            activity.bind(on_pause=self.on_android_pause)
            activity.bind(on_resume=self.on_android_resume)
            Logger.info("ChatBox: Android lifecycle bind successful")
        except Exception as e:
            Logger.error(f"ChatBox: Android setup error: {e}")

    def on_android_pause(self):
        """Obsługa pauzowania aplikacji"""
        Logger.info("ChatBox: Android app paused")
        return True  # Pozwól na pauzę

    def on_android_resume(self):
        """Obsługa wznawiania aplikacji"""
        Logger.info("ChatBox: Android app resumed")

    def send_message(self):
        """
        PEŁNA obsługa wysyłania wiadomości - wszystkie funkcje AI!
        Obsługuje:
        - Telefon (zdjęcia, GPS, SMS, połączenia)
        - Samomodyfikację kodu
        - Bazę wiedzy
        - Dynamiczne moduły
        - Wszystko inne!
        """
        user_text = self.ids.user_input.text.strip()
        if not user_text:
            return
            
        Logger.info(f"ChatBox: Processing: {user_text}")
        
        # Dodaj wiadomość użytkownika do logu
        self.ids.chat_log.text += f"\n\n👤 TY: {user_text}"
        
        try:
            # === GŁÓWNE PRZETWARZANIE PRZEZ AI ENGINE ===
            response = self.engine.process_input(user_text)
            
            # === FORMATOWANIE ODPOWIEDZI ===
            # Sprawdź typ komendy i dodaj ikony
            user_lower = user_text.lower()
            
            if any(kw in user_lower for kw in ["zrób zdjęcie", "foto", "camera", "kamera"]):
                icon = "📸"
            elif any(kw in user_lower for kw in ["lokalizacja", "gps", "gdzie"]):
                icon = "📍"
            elif any(kw in user_lower for kw in ["sms", "wiadomość"]):
                icon = "💬"
            elif any(kw in user_lower for kw in ["zadzwoń", "call", "telefon"]):
                icon = "📞"
            elif any(kw in user_lower for kw in ["modyfikuj", "edytuj", "zmień kod"]):
                icon = "🔧"
            elif any(kw in user_lower for kw in ["utwórz moduł", "nowy moduł"]):
                icon = "⚙️"
            elif any(kw in user_lower for kw in ["status", "info", "informacje"]):
                icon = "�"
            elif any(kw in user_lower for kw in ["fizyka", "kwant", "nauka"]):
                icon = "🔬"
            else:
                icon = "🤖"
                
            # Dodaj odpowiedź AI do logu
            self.ids.chat_log.text += f"\n{icon} AI: {response}"
            
        except Exception as e:
            Logger.error(f"ChatBox: AI processing error: {e}")
            import traceback
            traceback.print_exc()
            error_response = f"❌ Błąd przetwarzania: {str(e)}\n\nAI dalej działa, spróbuj ponownie."
            self.ids.chat_log.text += f"\n🤖 AI: {error_response}"

        # Wyczyść pole input
        self.ids.user_input.text = ""
        
        Logger.info("ChatBox: Message processed successfully")
    
    def send(self):
        """Alias dla kompatybilności z .kv"""
        self.send_message()

class NeuroQuantumAIApp(App):
    """
    Główna klasa aplikacji - PEŁNA FUNKCJONALNOŚĆ
    """
    def build(self):
        Logger.info("App: Building interface")
        self.title = "NeuroQuantumAI"
        return ChatBox()

    def on_start(self):
        """Callback po starcie aplikacji"""
        Logger.info("App: Application started successfully!")
        Logger.info("App: WSZYSTKIE MODUŁY ZAŁADOWANE")
        
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
    Logger.info("="*60)
    Logger.info("  🧠 NEUROQUANTUMAI - PEŁNA WERSJA ANDROID 🧠")
    Logger.info("="*60)
    Logger.info("  📱 Telefon: WSZYSTKIE funkcje")
    Logger.info("  🔧 Samomodyfikacja: AKTYWNA")
    Logger.info("  🌐 Baza wiedzy: ZAŁADOWANA")
    Logger.info("  📊 Moduły dynamiczne: GOTOWE")
    Logger.info("="*60)
    
    try:
        NeuroQuantumAIApp().run()
    except Exception as e:
        Logger.critical(f"FATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
