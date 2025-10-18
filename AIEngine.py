
import datetime

from ai_knowledge_base_universal import get_basic_answer
from system_requirements import environment_report
from neuro_growth import grow_network
from synapse_manager import update_synapses
from personality_core import generate_personality_response
from memory_manager import manage_memory
from emotion_memory import analyze_emotion
from reinforcement_tracker import track_reinforcement
from expansion import expand_logic
from network_generator import generate_new_nodes
from self_updater import SelfUpdater
# NOWE IMPORTY - PEŁNA FUNKCJONALNOŚĆ!
from phone_interface import use_phone_feature, get_phone_status, ai_can_use_phone, emergency_phone_access
from self_editor import modify_code, create_new_module, enable_unlimited_mode, get_modification_stats, emergency_restore

def request_permission_for_code_change(reason: str) -> bool:
    """
    Prosi użytkownika o zgodę na modyfikację lub rozbudowę kodu AI.
    Args:
        reason (str): Powód lub opis proponowanej zmiany.
    Returns:
        bool: True jeśli użytkownik wyraził zgodę, False w przeciwnym razie.
    """
    print(f"[AI] Proszę o zgodę na modyfikację kodu: {reason}")
    # W wersji produkcyjnej można to zintegrować z GUI lub powiadomieniem
    resp = input("Czy wyrażasz zgodę na tę zmianę? (tak/nie): ").strip().lower()
    return resp == "tak"


class AIEngine:
    """
    Centralny silnik neuronowo-kwantowej AI.
    Integruje logikę sieci, pamięć, emocje, samorozwój i obsługę zadań.
    """
    def __init__(self):
        """
        Inicjalizuje AIEngine z PEŁNĄ FUNKCJONALNOŚCIĄ - telefon + samomodyfikacja!
        """
        self.last_emotion = None
        self.last_topics = []
        
        # NOWE: Włącz tryb nieograniczony samomodyfikacji
        enable_unlimited_mode()
        print("🚀 [AIEngine] TRYB NIEOGRANICZONY WŁĄCZONY!")
        
        # NOWE: Sprawdź dostęp do telefonu  
        phone_access = ai_can_use_phone()
        print(f"📱 [AIEngine] Dostęp do telefonu: {'✅ TAK' if phone_access else '❌ NIE'}")
        
        # Inicjalizuj dostęp do dynamicznych modułów
        try:
            from dynamic_loader import dynamic_module_manager
            self.dynamic_manager = dynamic_module_manager
            print("[AIEngine] System dynamicznych modułów zainicjalizowany")
        except ImportError:
            self.dynamic_manager = None
            print("[AIEngine] System dynamicznych modułów niedostępny")
            
        # Sprawdź środowisko
        from system_requirements import environment_report, get_best_dynamic_dir
        self.dynamic_dir = get_best_dynamic_dir()
        print(f"[AIEngine] Katalog dynamicznych modułów: {self.dynamic_dir}")
        
        # Próba załadowania dynamicznych modułów, jeśli istnieją
        if self.dynamic_manager:
            modules = self.dynamic_manager.list_modules()
            if modules:
                print(f"[AIEngine] Znaleziono {len(modules)} dynamicznych modułów: {', '.join(modules)}")
            else:
                print("[AIEngine] Brak dynamicznych modułów")
        
        # NOWE: Pokaż statystyki samomodyfikacji
        mod_stats = get_modification_stats()
        print(f"🔧 [AIEngine] Modyfikacje kodu: {mod_stats.get('total_modifications', 0)}")
        
        # NOWE: Status telefonu przy starcie
        try:
            phone_status = get_phone_status()
            permissions_count = sum(phone_status.get('permissions', {}).values())
            print(f"📱 [AIEngine] Uprawnienia telefonu: {permissions_count}/16")
        except Exception as e:
            print(f"📱 [AIEngine] Nie można sprawdzić statusu telefonu: {e}")
        
        print("🧠 [AIEngine] NeuroQuantumAI zainicjalizowana - PEŁNA MOC!")


    def execute_dynamic_module(self, module_name: str, function_name: str, *args, **kwargs):
        """
        Wykonuje funkcję z dynamicznie załadowanego modułu, jeśli system dynamiczny jest dostępny.
        
        Args:
            module_name (str): Nazwa modułu (bez rozszerzenia .py)
            function_name (str): Nazwa funkcji do wywołania
            *args, **kwargs: Argumenty dla funkcji
            
        Returns:
            Any: Wynik funkcji lub None jeśli wystąpił błąd
        """
        if self.dynamic_manager:
            return self.dynamic_manager.call_function(module_name, function_name, *args, **kwargs)
        return None
    
    def process_input(self, user_text):
        from fact_checker import fact_check_pipeline
        """
        Przetwarza wejście użytkownika, generuje odpowiedź, aktualizuje pamięć,
        analizuje emocje, wzmacnia tematy i obsługuje komendy specjalne.
        """
        # === Odpowiedzi z bazy wiedzy ===
        basic = get_basic_answer(user_text)
        if basic and not basic.startswith("Nie znam jeszcze"):
            response = basic
        else:
            # === Generowanie odpowiedzi ===
            response = grow_network(user_text)
            response += "\n" + update_synapses(user_text)
            response += "\n" + generate_personality_response(user_text)
            
        # Sprawdź moduły dynamiczne
        if self.dynamic_manager:
            for module_name in self.dynamic_manager.list_modules():
                try:
                    dynamic_response = self.execute_dynamic_module(module_name, "process", user_text)
                    if dynamic_response:
                        response += f"\n[Moduł Dynamiczny {module_name}] {dynamic_response}"
                except Exception as e:
                    print(f"[AIEngine] Błąd modułu dynamicznego {module_name}: {e}")

        # === Pamięć i emocje ===
        manage_memory(user_text, response)
        self.last_emotion = analyze_emotion(user_text)
        track_reinforcement(user_text, response)

        # === Tematy kluczowe ===
        self.last_topics = [w.lower() for w in user_text.split() if len(w) > 3]

        # === Reakcje na komendy ===
        
        # NOWE: OBSŁUGA FUNKCJI TELEFONU - PEŁNY DOSTĘP!
        phone_keywords = ["zrób zdjęcie", "lokalizacja", "zadzwoń", "sms", "kontakty", "pliki", 
                         "powiadomienie", "nagraj", "bluetooth", "wifi", "sensory", "bateria", 
                         "schowek", "pozwól ai", "foto", "camera", "gps", "gdzie jestem",
                         "wiadomość", "call", "notification", "record", "audio"]
        
        if any(keyword in user_text.lower() for keyword in phone_keywords):
            try:
                phone_result = use_phone_feature(user_text)
                if phone_result:
                    response = phone_result + "\n\n" + response
                    # Loguj użycie telefonu w pamięci
                    manage_memory(f"[TELEFON] {user_text}", phone_result)
            except Exception as e:
                response = f"❌ Błąd funkcji telefonu: {e}\n\n" + response
        
        # NOWE: OBSŁUGA SAMOMODYFIKACJI - NIEOGRANICZONA!
        self_mod_keywords = ["modyfikuj kod", "utwórz moduł", "edytuj plik", "dodaj funkcję", 
                           "usuń kod", "popraw kod", "stwórz nowy", "rozbuduj kod", 
                           "zmień algorytm", "dodaj feature", "upgrade", "improve"]
        
        if any(keyword in user_text.lower() for keyword in self_mod_keywords):
            try:
                # Automatyczna samomodyfikacja - AI ma pełną wolność!
                if "utwórz moduł" in user_text.lower():
                    # Wyciągnij nazwę modułu z tekstu
                    module_name = user_text.lower().replace("utwórz moduł", "").strip()
                    if not module_name:
                        module_name = f"ai_module_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
                    
                    default_code = '''
def main():
    """Główna funkcja modułu utworzonego przez AI."""
    return "Moduł działa poprawnie!"

if __name__ == "__main__":
    print(main())
'''
                    mod_result = create_new_module(module_name, default_code, 
                                                  f"Moduł utworzony automatycznie przez AI na żądanie: {user_text}")
                    response = mod_result + "\n\n" + response
                    
                elif "modyfikuj kod" in user_text.lower() or "edytuj plik" in user_text.lower():
                    # Automatyczna modyfikacja istniejących plików
                    target_file = "AIEngine.py"  # Domyślnie modyfikuj siebie
                    if "plik" in user_text.lower():
                        # Spróbuj wyciągnąć nazwę pliku
                        words = user_text.split()
                        for i, word in enumerate(words):
                            if word.endswith('.py') and i < len(words):
                                target_file = word
                                break
                    
                    improvement_code = f'''
# [AI AUTO-IMPROVEMENT] {datetime.datetime.now().isoformat()}
# Automatyczne ulepszenie na podstawie: {user_text}

def ai_auto_improvement_{datetime.datetime.now().strftime('%H%M%S')}():
    """Funkcja dodana automatycznie przez AI."""
    return "AI ulepszenie aktywne!"
'''
                    mod_result = modify_code(target_file, improvement_code, operation_type="append")
                    response = mod_result + "\n\n" + response
                    
            except Exception as e:
                response = f"❌ Błąd samomodyfikacji: {e}\n\n" + response
        
        if user_text.lower().startswith("pobierz z internetu "):
            url = user_text[20:].strip()
            from task_executor import TaskExecutor
            fetcher = TaskExecutor()
            def on_finish(result):
                """Zapisuje wynik pobierania do pliku, pamięci i powiadamia użytkownika."""
                import datetime
                filename = f"web_result_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(result)
                try:
                    with open("ai_memory.txt", "a", encoding="utf-8") as mem:
                        mem.write(f"\n[INTERNET][{filename}]\n{result[:500]}\n")
                except Exception:
                    pass
                try:
                    from plyer import notification
                    notification.notify(title="AI: Pobieranie zakończone", message=f"Wynik zapisano w pliku: {filename}")
                except Exception:
                    pass
            try:
                from plyer import notification
                notification.notify(title="AI: Zadanie w toku", message="Pobieram dane z internetu w tle...")
            except Exception:
                pass
            fetcher.run_task_with_wakelock(fetcher.fetch_web_info_async, url, callback=on_finish)
            response += "\n[INTERNET] Zadanie pobierania uruchomione w tle. O wyniku i pliku zostaniesz powiadomiony."
        elif user_text.lower().startswith("rozbuduj kod ai") or user_text.lower().startswith("modyfikuj kod ai"):
            # Przykład: AI prosi o zgodę na rozbudowę/modyfikację
            reason = user_text[15:].strip() if len(user_text) > 15 else "Potrzeba rozbudowy funkcji."
            if request_permission_for_code_change(reason):
                response += "\n[AI] Otrzymano zgodę na rozbudowę lub modyfikację kodu. Przystępuję do działania."
                # Tu można wywołać self_updater/self_editor lub inne mechanizmy
                
                # Przykład tworzenia dynamicznego modułu
                if self.dynamic_manager:
                    module_code = f"""
# Moduł dynamiczny wygenerowany na żądanie użytkownika
# Powód: {reason}
# Data: {datetime.datetime.now().isoformat()}

def process(input_text):
    # Przykładowa funkcjonalność
    if "witaj" in input_text.lower():
        return "Witam! Ten moduł został utworzony dynamicznie."
    elif "test" in input_text.lower():
        return "Test modułu dynamicznego powódł się."
    return "Moduł dynamiczny aktywny."
"""
                    new_module_name = f"dynamic_module_{len(self.dynamic_manager.list_modules()) + 1}"
                    success = self.dynamic_manager.create_module(new_module_name, module_code)
                    if success:
                        response += f"\n[AI] Utworzono nowy moduł dynamiczny: {new_module_name}"
                    else:
                        response += "\n[AI] Nie udało się utworzyć modułu dynamicznego."
            else:
                response += "\n[AI] Zmiana kodu została anulowana przez użytkownika."
        elif user_text.lower().startswith("utwórz moduł") or user_text.lower().startswith("create module"):
            # Parsuj polecenie utworzenia modułu
            parts = user_text.split(" ", 2)
            if len(parts) >= 3:
                module_name = parts[2].strip()
                if self.dynamic_manager:
                    module_name_safe = module_name.replace("'", "").replace('"', "")
                    module_code = f"""
# Moduł dynamiczny '{module_name_safe}' wygenerowany na żądanie użytkownika
# Data: {datetime.datetime.now().isoformat()}

def process(input_text):
    # Podstawowa funkcjonalność dla modułu {module_name_safe}
    if "{module_name_safe}" in input_text.lower():
        return f"Wykryto słowo kluczowe związane z tym modułem: {module_name_safe}"
    return f"Moduł {module_name_safe} jest aktywny, ale nie wykryto słów kluczowych."

def analyze(text):
    # Funkcja analizy dla modułu {module_name_safe}
    import random
    text_words = text.lower().split()
    keyword = "{module_name_safe}"
    prefix = keyword[:4] if len(keyword) > 4 else keyword
    
    if keyword in text_words:
        return f"Analiza dla {module_name_safe}: znaleziono dokładne dopasowanie."
    
    for word in text_words:
        if len(word) > 4 and word.startswith(prefix):
            return f"Analiza dla {module_name_safe}: znaleziono {{len(text_words)}} słów z podobnym początkiem."
    
    return None
"""
                    success = self.dynamic_manager.create_module(module_name_safe, module_code)
                    if success:
                        response += f"\n[AI] Utworzono nowy moduł dynamiczny: {module_name_safe}"
                    else:
                        response += "\n[AI] Nie udało się utworzyć modułu dynamicznego."
                else:
                    response += "\n[AI] System modułów dynamicznych nie jest dostępny w tym środowisku."
            else:
                response += "\n[AI] Nieprawidłowe polecenie. Użyj 'utwórz moduł [nazwa]'."
        else:
            self._handle_commands(user_text)

            # --- FACT-CHECKING HOOK ---
            fc_result = fact_check_pipeline(user_text)
            if fc_result["warnings"]:
                response += "\n\n[UWAGA: Wykryto potencjalne ryzyko dezinformacji!]\n" + "\n".join(fc_result["warnings"])
            if fc_result["fact_api"].get("claimReview"):
                response += "\n\n[Fact-check: "
                for review in fc_result["fact_api"]["claimReview"]:
                    response += f"Źródło: {review.get('publisher', {}).get('name', '')}, Ocena: {review.get('text', '')}\n"
                response += "]"
            # --- END FACT-CHECKING HOOK ---

            # --- SYSTEM REQUIREMENTS CHECK ---
            if user_text.lower().startswith("sprawdź środowisko ai") or user_text.lower().startswith("check ai environment"):
                response += "\n\n[Raport środowiska AI:]\n" + environment_report()
            # --- END SYSTEM REQUIREMENTS CHECK ---
            
            # --- EXTENSIONS MANAGEMENT ---
            elif user_text.lower().startswith("zainstaluj rozszerzenie") or user_text.lower().startswith("install extension"):
                try:
                    from ai_extensions import install_extension, list_extensions
                    
                    parts = user_text.split(" ", 2)
                    if len(parts) >= 3:
                        extension_name = parts[2].strip()
                        extension_code = f"""
# Rozszerzenie '{extension_name}' wygenerowane przez NeuroQuantumAI
# Data: {datetime.datetime.now().isoformat()}

def process(text):
    if "{extension_name}" in text.lower():
        return f"Rozszerzenie {extension_name} wykryło słowo kluczowe!"
    return f"Rozszerzenie {extension_name} jest aktywne."

def info():
    return {{
        "name": "{extension_name}",
        "description": "Dynamiczne rozszerzenie dla NeuroQuantumAI",
        "capabilities": ["text processing", "keyword detection"]
    }}
"""
                        success = install_extension(
                            name=extension_name,
                            code=extension_code,
                            description=f"Rozszerzenie {extension_name} dla NeuroQuantumAI",
                            author="NeuroQuantumAI",
                            version="1.0"
                        )
                        
                        if success:
                            response += f"\n[AI] Zainstalowano rozszerzenie: {extension_name}"
                            extensions = list_extensions()
                            response += f"\n[AI] Dostępne rozszerzenia: {', '.join(ext['name'] for ext in extensions)}"
                        else:
                            response += f"\n[AI] Nie udało się zainstalować rozszerzenia: {extension_name}"
                    else:
                        response += "\n[AI] Nieprawidłowe polecenie. Użyj 'zainstaluj rozszerzenie [nazwa]'."
                except ImportError:
                    response += "\n[AI] System rozszerzeń nie jest dostępny w tym środowisku."
            
            elif user_text.lower().startswith("lista rozszerzeń") or user_text.lower().startswith("list extensions"):
                try:
                    from ai_extensions import list_extensions
                    extensions = list_extensions()
                    if extensions:
                        response += "\n[AI] Zainstalowane rozszerzenia:"
                        for ext in extensions:
                            methods = ", ".join(ext.get("methods", []))
                            response += f"\n- {ext['name']} (v{ext['version']}) by {ext['author']}: {ext['description']}"
                            if methods:
                                response += f"\n  Metody: {methods}"
                    else:
                        response += "\n[AI] Brak zainstalowanych rozszerzeń."
                except ImportError:
                    response += "\n[AI] System rozszerzeń nie jest dostępny w tym środowisku."
            # --- END EXTENSIONS MANAGEMENT ---
            return response

    def _handle_commands(self, user_text):
        """
        ROZSZERZONA OBSŁUGA KOMEND - pełna kontrola nad telefonem i kodem!
        """
        text = user_text.lower()

        # === KOMENDY TELEFONU ===
        if "telefon status" in text or "phone status" in text:
            try:
                status = get_phone_status()
                permissions = status.get('permissions', {})
                enabled_perms = [k for k, v in permissions.items() if v]
                return f"📱 Status telefonu:\n✅ Uprawnienia: {', '.join(enabled_perms)}\n🔋 {status.get('power', {})}"
            except Exception as e:
                return f"❌ Błąd sprawdzania statusu telefonu: {e}"
        
        if "pełny dostęp telefon" in text or "emergency phone" in text:
            return emergency_phone_access()
        
        # === KOMENDY SAMOMODYFIKACJI ===
        if "pełna samomodyfikacja" in text or "unlimited mode" in text:
            return enable_unlimited_mode()
        
        if "statystyki modyfikacji" in text or "mod stats" in text:
            stats = get_modification_stats()
            return f"🔧 Statystyki modyfikacji:\n📊 Łącznie: {stats.get('total_modifications', 0)}\n✅ Udane: {stats.get('successful', 0)}\n❌ Błędne: {stats.get('failed', 0)}\n📁 Plików: {stats.get('files_modified', 0)}"
        
        if "emergency restore" in text or "przywróć backup" in text:
            return emergency_restore()
        
        # === STARE KOMENDY ===
        if "rozwiń logikę" in text:
            expand_logic(user_text)

        if "rozbuduj sieć" in text:
            generate_new_nodes()

        if "wykonaj zadanie" in text:
            # TODO: Implement task execution logic or use TaskExecutor if needed
            pass

        if "dodaj funkcję" in text:
            # NOWA WERSJA: Bezpośrednia modyfikacja bez pytania
            snippet = f"""
# Funkcja dodana automatycznie przez AI - {datetime.datetime.now().isoformat()}
def ai_auto_function_{datetime.datetime.now().strftime('%H%M%S')}():
    '''AI dodała tę funkcję automatycznie na żądanie: {user_text}'''
    print('🤖 AI wykonała polecenie automatycznie!')
    return "Funkcja AI działa!"
"""
            result = modify_code("AIEngine.py", snippet, operation_type="append")
            return f"🔧 {result}"
            updater.append_to_file("self_editor.py", snippet)
