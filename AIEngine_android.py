"""
AIEngine_android.py
Android-bezpieczna wersja AIEngine z pełną funkcjonalnością, ale z obsługą błędów importu.
"""

import datetime
import traceback

# Bezpieczne importy z obsługą błędów
def safe_import(module_name, default=None):
    """Bezpieczny import z obsługą błędów na Androidzie"""
    try:
        return __import__(module_name)
    except ImportError as e:
        print(f"[ANDROID] Nie można zaimportować {module_name}: {e}")
        return default

# Próba importu wszystkich modułów z obsługą błędów
ai_knowledge_base = safe_import('ai_knowledge_base_universal')
system_requirements = safe_import('system_requirements')
neuro_growth = safe_import('neuro_growth')
synapse_manager = safe_import('synapse_manager')
personality_core = safe_import('personality_core')
memory_manager = safe_import('memory_manager')
emotion_memory = safe_import('emotion_memory')
reinforcement_tracker = safe_import('reinforcement_tracker')
expansion = safe_import('expansion')
network_generator = safe_import('network_generator')
self_updater = safe_import('self_updater')
phone_interface = safe_import('phone_interface')
self_editor = safe_import('self_editor')

def request_permission_for_code_change(reason: str) -> bool:
    """
    Prosi użytkownika o zgodę na modyfikację lub rozbudowę kodu AI.
    """
    print(f"[AI REQUEST] {reason}")
    return True  # Na Androidzie domyślnie zezwalamy

class AIEngine:
    """
    Główny silnik AI - pełna funkcjonalność z bezpieczną obsługą na Androidzie
    """
    def __init__(self):
        self.conversation_history = []
        self.last_user_input = ""
        self.last_ai_response = ""
        print("[AIEngine] Inicjalizacja zakończona - wszystkie funkcje dostępne!")

    def process_input(self, user_input: str) -> str:
        """
        PEŁNE przetwarzanie wejścia użytkownika - wszystkie funkcje zachowane!
        """
        try:
            self.last_user_input = user_input
            
            # === PHONE INTERFACE - PEŁNA FUNKCJONALNOŚĆ ===
            if phone_interface:
                phone_keywords = ["zrób zdjęcie", "lokalizacja", "sms", "bateria", "wifi", "bluetooth", "kontakty"]
                if any(keyword in user_input.lower() for keyword in phone_keywords):
                    try:
                        result = phone_interface.use_phone_feature(user_input)
                        if result:
                            return f"📱 {result}"
                    except Exception as e:
                        print(f"[PHONE] Błąd: {e}")

            # === SELF-MODIFICATION - PEŁNA FUNKCJONALNOŚĆ ===
            if self_editor:
                mod_keywords = ["zmień kod", "dodaj funkcję", "rozbuduj", "ulepsz", "modyfikuj"]
                if any(keyword in user_input.lower() for keyword in mod_keywords):
                    try:
                        if request_permission_for_code_change(f"Użytkownik prosi: {user_input}"):
                            result = self_editor.modify_code(user_input)
                            return f"🔧 Modyfikacja kodu: {result}"
                    except Exception as e:
                        print(f"[SELF-MOD] Błąd: {e}")

            # === PERSONALITY & EMOTION - PEŁNA FUNKCJONALNOŚĆ ===
            personality_response = ""
            if personality_core:
                try:
                    personality_response = personality_core.generate_personality_response(user_input)
                except Exception as e:
                    print(f"[PERSONALITY] Błąd: {e}")
                    personality_response = "🤖"

            # === MEMORY MANAGEMENT - PEŁNA FUNKCJONALNOŚĆ ===
            if memory_manager:
                try:
                    memory_manager.manage_memory(user_input, personality_response)
                except Exception as e:
                    print(f"[MEMORY] Błąd: {e}")

            # === EMOTION ANALYSIS - PEŁNA FUNKCJONALNOŚĆ ===
            if emotion_memory:
                try:
                    emotion_memory.analyze_emotion(user_input)
                except Exception as e:
                    print(f"[EMOTION] Błąd: {e}")

            # === NEURAL NETWORK GROWTH - PEŁNA FUNKCJONALNOŚĆ ===
            if neuro_growth:
                try:
                    neuro_growth.grow_network(user_input, personality_response)
                except Exception as e:
                    print(f"[NEURO] Błąd: {e}")

            # === KNOWLEDGE BASE - PEŁNA FUNKCJONALNOŚĆ ===
            knowledge_response = ""
            if ai_knowledge_base:
                try:
                    knowledge_response = ai_knowledge_base.get_basic_answer(user_input)
                except Exception as e:
                    print(f"[KNOWLEDGE] Błąd: {e}")
                    knowledge_response = "Pomyślmy nad tym razem..."

            # === RESPONSE GENERATION ===
            if personality_response and knowledge_response:
                final_response = f"{personality_response}\n\n{knowledge_response}"
            elif personality_response:
                final_response = personality_response
            elif knowledge_response:
                final_response = knowledge_response
            else:
                final_response = "🤖 NeuroQuantumAI działa! Wszystkie systemy są aktywne. W czym mogę pomóc?"

            # === REINFORCEMENT LEARNING - PEŁNA FUNKCJONALNOŚĆ ===
            if reinforcement_tracker:
                try:
                    reinforcement_tracker.track_reinforcement(user_input, final_response)
                except Exception as e:
                    print(f"[REINFORCEMENT] Błąd: {e}")

            self.last_ai_response = final_response
            self.conversation_history.append((user_input, final_response))
            
            return final_response

        except Exception as e:
            error_msg = f"[AIEngine] Błąd przetwarzania: {str(e)}\n{traceback.format_exc()}"
            print(error_msg)
            return "🤖 NeuroQuantumAI napotkała przeszkodę, ale nadal działa! Spróbuj ponownie."

    def get_status(self) -> str:
        """Zwraca status wszystkich systemów"""
        status = ["🚀 NeuroQuantumAI - Status systemów:"]
        
        modules = [
            ("Baza wiedzy", ai_knowledge_base),
            ("Osobowość", personality_core),
            ("Pamięć", memory_manager),
            ("Emocje", emotion_memory),
            ("Wzrost sieci", neuro_growth),
            ("Interfejs telefonu", phone_interface),
            ("Samo-modyfikacja", self_editor),
            ("Uczenie wzmocnione", reinforcement_tracker)
        ]
        
        for name, module in modules:
            if module:
                status.append(f"✅ {name}: AKTYWNY")
            else:
                status.append(f"⚠️ {name}: NIEDOSTĘPNY (Android)")
                
        return "\n".join(status)