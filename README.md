---

## �️ Wirtualny terminal i interpreter AI

Projekt zawiera moduł `ai_shell.py`, który pozwala uruchomić własny terminal i interpreter Pythona dla AI:

- Uruchomienie: `python ai_shell.py` lub integracja z AIEngine.
- Możesz wpisywać polecenia systemowe (np. `ls`, `dir`, `echo test`) lub kod Pythona (`py print(2+2)`).
- Komenda `exit` kończy sesję.
- Shell działa w osobnym wątku i może być rozbudowany o dodatkowe zabezpieczenia.

To środowisko pozwala AI na eksperymenty, testy i samodzielne wykonywanie poleceń w bezpieczny sposób.

---
---

## �🛠️ Wymagania środowiskowe i ograniczenia samomodyfikacji AI

**Pełna samomodyfikacja AI (np. edycja własnych plików, dynamiczne generowanie kodu, restartowanie modułów) wymaga środowiska z dostępem do systemu plików i interpretera Python:**

- **Termux (Android):** Pozwala na uruchamianie Pythona, modyfikację plików, korzystanie z narzędzi systemowych i terminala. Zalecane do eksperymentów z samomodyfikacją AI.
- **Komputer (Windows/Linux/Mac):** Pełny dostęp do systemu plików, terminala i narzędzi deweloperskich.
- **Standardowa aplikacja Android (APK):** Ograniczony dostęp — AI nie może modyfikować własnych plików po instalacji (sandboxing, bezpieczeństwo systemu).

**Wskazówki:**
- Jeśli chcesz, by AI mogła się rozwijać i modyfikować, uruchamiaj ją w Termux lub na komputerze.
- Wersja APK na Androida pozwala na korzystanie z funkcji telefonu i internetu, ale nie na samomodyfikację kodu.
- Moduły fact-checkingu, detekcji dezinformacji i porównywania źródeł są dostępne w każdej wersji.

---
# 🤖 NeuroQuantumAI App

**PL/ENG below**

---

## 🧠 Opis projektu / Project Overview

NeuroQuantumAI to eksperymentalna aplikacja AI na Androida, łącząca elementy sieci neuronowych, kwantowego myślenia i modularnej architektury. Pozwala na interakcję z AI, która rozwija się, uczy i modyfikuje swoje zachowanie na podstawie rozmów, emocji i wzmocnień.

NeuroQuantumAI is an experimental Android AI app combining neural networks, quantum-inspired thinking, and modular architecture. The AI interacts, learns, and evolves based on conversations, emotions, and reinforcement.

---

## ✨ Główne funkcje / Key Features

- Modularna architektura AI (pamięć, emocje, wzmocnienia, samomodyfikacja)
- Dynamiczne generowanie i rozbudowa sieci neuronowej
- Interfejs Kivy na Androida (kompatybilność z Buildozer)
- Integracja z funkcjami telefonu (kamera, lokalizacja, SMS, połączenia)
- Plikowa persystencja stanu i historii
- Łatwe rozszerzanie o nowe moduły tematyczne

---

## 📦 Wymagania / Requirements

- Python 3.11+ (zalecane)
- pip
- buildozer (do kompilacji APK)
- Android device (for deployment)

---

## 🧪 Instalacja środowiska / Environment Setup

> Środowisko nie jest częścią repozytorium — tworzy się je lokalnie.
> The environment is not included in the repo — create it locally.

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install buildozer cython setuptools==65.5.1
```

---

## 🚀 Uruchomienie / Running

```bash
# (W środowisku venv / In venv)
python main.py
# Lub kompilacja na Androida / Or build for Android:
buildozer -v android debug
```

---

## 🏗️ Struktura projektu / Project Structure

- `main.py` — Główny plik uruchomieniowy / Main entry point
- `AIEngine.py` — Silnik AI / AI Engine
- `memory_manager.py`, `emotion_memory.py`, `reinforcement_tracker.py` — Moduły pamięci, emocji, wzmocnień / Memory, emotion, reinforcement modules
- `network_*` — Pliki sieci neuronowej / Neural network files
- `expansion.py`, `self_editor.py`, `self_updater.py` — Rozwój i samomodyfikacja / Expansion and self-modification
- `chat_gui.kv` — Interfejs Kivy / Kivy UI
- `buildozer.spec` — Konfiguracja Buildozer / Buildozer config

---

## 🧩 Rozszerzanie / Extending

Dodawaj nowe moduły tematyczne przez `neuro_architect.py` lub ręcznie. Każdy plik `module_<temat>.py` może zawierać własną logikę analizy.

Add new topic modules via `neuro_architect.py` or manually. Each `module_<topic>.py` can contain its own analysis logic.

---

## 🤝 Wkład / Contributing

Chętnie przyjmujemy pull requesty i sugestie! / Pull requests and suggestions welcome!

---

## 📄 Licencja / License

MIT
