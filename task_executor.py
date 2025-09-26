

# task_executor.py
from plyer import gps, camera, notification, filechooser, tts
import datetime
import requests
import threading
from typing import Any, Callable, Optional

class TaskExecutor:
    """
    Provides methods for running background tasks, notifications, camera, GPS, TTS, and file selection.
    """
    def run_in_background(self, func: Callable, *args: Any, **kwargs: Any) -> threading.Thread:
        """Uruchamia funkcję w osobnym wątku (zadanie w tle)."""
        thread = threading.Thread(target=func, args=args, kwargs=kwargs, daemon=True)
        thread.start()
        return thread

    def fetch_web_info_async(self, url: str, params: Optional[dict] = None, headers: Optional[dict] = None, callback: Optional[Callable] = None) -> None:
        """Pobiera dane z internetu asynchronicznie i wywołuje callback z wynikiem."""
        def task():
            result = self.fetch_web_info(url, params, headers)
            if callback:
                callback(result)
        self.run_in_background(task)

    def keep_screen_awake(self, enable: bool = True) -> None:
        """(Android) Włącza/wyłącza blokadę wygaszania ekranu. Na desktopie nieaktywne."""
        pass

    def run_task_with_wakelock(self, func: Callable, *args: Any, **kwargs: Any) -> threading.Thread:
        """Uruchamia zadanie w tle z blokadą wygaszania ekranu (jeśli dostępne)."""
        def wrapper():
            self.keep_screen_awake(True)
            try:
                func(*args, **kwargs)
            finally:
                self.keep_screen_awake(False)
        return self.run_in_background(wrapper)

    def fetch_web_info(self, url: str, params: Optional[dict] = None, headers: Optional[dict] = None) -> str:
        """Pobiera dane z internetu (GET). Zwraca tekst lub błąd."""
        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text[:1000] + ("..." if len(response.text) > 1000 else "")
        except Exception as e:
            return f"Błąd pobierania: {e}"

    def show_notification(self, title: str = "Powiadomienie AI", message: str = "Zadanie wykonane.") -> None:
        """Wyświetla powiadomienie na urządzeniu."""
        try:
            notification.notify(title=title, message=message)
        except Exception as e:
            print("Błąd powiadomienia:", e)

    def take_photo(self, filename: Optional[str] = None) -> None:
        """Wykonuje zdjęcie aparatem urządzenia."""
        try:
            if not filename:
                filename = f"photo_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            camera.take_picture(filename=filename, on_complete=lambda x: print(f"Zapisano zdjęcie: {x}"))
        except Exception as e:
            print("Błąd fotografowania:", e)

    def get_location(self) -> None:
        """Pobiera lokalizację urządzenia (GPS)."""
        try:
            gps.configure(on_location=lambda **kwargs: print("Lokalizacja:", kwargs))
            gps.start()
        except Exception as e:
            print("Błąd GPS:", e)

    def speak_text(self, text: str = "Cześć! Tu Twoja AI.") -> None:
        """Odczytuje tekst głosem (TTS)."""
        try:
            tts.speak(text)
        except Exception as e:
            print("Błąd syntezatora mowy:", e)

    def choose_file(self) -> None:
        """Otwiera okno wyboru pliku."""
        try:
            filechooser.open_file(on_selection=lambda x: print("Wybrano plik:", x))
        except Exception as e:
            print("Błąd wyboru pliku:", e)
