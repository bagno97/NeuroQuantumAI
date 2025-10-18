````markdown
# Instrukcja budowania aplikacji NeuroQuantumAI na Androida

> **WAŻNA AKTUALIZACJA:** Dodano specjalne instrukcje dla urządzeń Samsung Galaxy A35 5G w sekcji "Specjalne instrukcje dla Samsung Galaxy A35 5G" na końcu dokumentu.

## Wymagania systemowe

Aby zbudować aplikację NeuroQuantumAI na Androida, potrzebujesz:

- Python 3.7+ (zalecane 3.9 lub 3.10)
- Buildozer
- Java JDK 11
- Android SDK i NDK

## Kroki instalacji na Linux (Ubuntu/Debian)

1. **Instalacja zależności systemowych**

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-dev git zip unzip openjdk-11-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
```

2. **Instalacja zależności Python**

```bash
pip install --user buildozer==1.4.0 cython==0.29.33 setuptools==65.5.1
```

3. **Sklonuj repozytorium (jeśli jeszcze nie masz)**

```bash
git clone https://github.com/bagno97/NeuroQuantumAI.git
cd NeuroQuantumAI
```

4. **Instalacja wymagań projektu**

```bash
pip install -r requirements.txt
```

5. **Przygotowanie aplikacji do budowania**

```bash
buildozer init
```

(Zauważ: w Twoim przypadku plik buildozer.spec już istnieje, więc ten krok nie jest konieczny)

6. **Zbudowanie APK**

```bash
buildozer -v android debug
```

Gdy proces budowania zakończy się pomyślnie, plik APK będzie dostępny w katalogu `bin/`.

## Kroki instalacji na Windows

1. **Zainstaluj WSL2 (Windows Subsystem for Linux)**
   - Uruchom PowerShell jako administrator i wykonaj:
   ```
   wsl --install
   ```
   
2. **Zainstaluj Ubuntu z Microsoft Store**

3. **Uruchom Ubuntu i wykonaj kroki instalacji dla Linux**

## Kroki instalacji na macOS

1. **Instalacja zależności za pomocą brew**

```bash
brew install autoconf automake libtool pkg-config
brew install python3 git
```

2. **Instalacja Java**

```bash
brew install --cask adoptopenjdk/openjdk/adoptopenjdk11
```

3. **Instalacja Buildozer i innych zależności Python**

```bash
pip3 install --user buildozer==1.4.0 cython==0.29.33 setuptools==65.5.1
```

4. **Wykonaj kroki 3-6 z instrukcji dla Linux**

## Instalacja APK na urządzeniu Android

1. Włącz "Instalację z nieznanych źródeł" w ustawieniach bezpieczeństwa urządzenia Android
2. Przenieś plik APK na urządzenie (przez USB, email, cloud storage, itp.)
3. Otwórz plik APK na urządzeniu i zainstaluj aplikację

## Rozwiązywanie problemów

Jeśli napotkasz problemy podczas budowania:

1. Sprawdź logi Buildozer (zwykle w `~/.buildozer/`)
2. Upewnij się, że masz odpowiednie wersje Android SDK i NDK
3. W przypadku błędów związanych z Java, upewnij się, że używasz JDK 8 lub JDK 11
4. Jeśli wystąpi błąd z distutils w Pythonie 3.12, użyj Python 3.10 lub 3.11

## Uwagi do budowania

Plik buildozer.spec jest już skonfigurowany dla tej aplikacji, ale możesz go dostosować:

- Zmień `package.domain` na swoją własną domenę
- Dostosuj `android.permissions` jeśli potrzebujesz innych uprawnień
- Jeśli aplikacja wymaga dodatkowych bibliotek Python, dodaj je do `requirements`

Powodzenia w budowaniu i korzystaniu z aplikacji NeuroQuantumAI!

## Specjalne instrukcje dla Samsung Galaxy A35 5G

Aby zoptymalizować aplikację dla Samsung Galaxy A35 5G, zastosuj następujące modyfikacje w pliku `buildozer.spec`:

1. **Zaktualizuj minimalną wersję API Androida**:
```
# Minimalna wersja Androida - dostosowana do Samsung Galaxy A35 5G
android.minapi = 26
android.api = 34
android.sdk = 34
android.ndk = 25b
android.archs = arm64-v8a
```

2. **Dodaj specjalne konfiguracje dla Samsung Galaxy A35 5G**:
```
[app.android]

# Konfiguracja pod Samsung Galaxy A35 5G
android.allow_backup = True
android.presplash_color = #ffffff
android.presplash.resize = False
android.entrypoint = org.kivy.android.PythonActivity
android.accept_sdk_license = True

# Optymalizacje dla Galaxy A35 5G
android.gradle_dependencies = androidx.work:work-runtime:2.7.1
android.add_jars = androidx.work:work-runtime:2.7.1
```

3. **Specjalne instrukcje instalacji na Samsung Galaxy A35 5G**:

   - Przenieś plik APK na urządzenie (przez USB, email lub chmurę)
   - Przejdź do Ustawienia > Biometria i zabezpieczenia > Zainstaluj nieznane aplikacje
   - Wybierz aplikację, którą użyjesz do instalacji (np. Menedżer plików)
   - Włącz przełącznik 'Zezwalaj z tego źródła'
   - Otwórz plik APK i postępuj zgodnie z instrukcjami instalacji

Pamiętaj, że Samsung Galaxy A35 5G ma zabezpieczenia Knox, które mogą wymagać dodatkowych uprawnień przy pierwszym uruchomieniu aplikacji.
````