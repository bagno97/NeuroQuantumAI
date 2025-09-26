
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
        Inicjalizuje AIEngine, resetuje ostatnie emocje i tematy.
        """
        self.last_emotion = None
        self.last_topics = []


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

        # === Pamięć i emocje ===
        manage_memory(user_text, response)
        self.last_emotion = analyze_emotion(user_text)
        track_reinforcement(user_text, response)

        # === Tematy kluczowe ===
        self.last_topics = [w.lower() for w in user_text.split() if len(w) > 3]

        # === Reakcje na komendy ===
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
            else:
                response += "\n[AI] Zmiana kodu została anulowana przez użytkownika."
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
            return response

    def _handle_commands(self, user_text):
        """
        Obsługuje specjalne komendy tekstowe użytkownika (rozwój, zadania, auto-modyfikacja).
        """
        text = user_text.lower()

        if "rozwiń logikę" in text:
            expand_logic(user_text)

        if "rozbuduj sieć" in text:
            generate_new_nodes()

        if "wykonaj zadanie" in text:
            # TODO: Implement task execution logic or use TaskExecutor if needed
            pass

        if "dodaj funkcję" in text:
            snippet = (
                "# Funkcja dodana przez AI\n"
                "def auto_function():\n"
                "    print('AI wykonała polecenie.')"
            )
            updater = SelfUpdater()
            updater.append_to_file("self_editor.py", snippet)
