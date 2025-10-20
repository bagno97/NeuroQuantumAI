#!/bin/bash
# QUICK_BUILD.sh
# Szybki build bez pełnej konfiguracji - dla testów

echo "🚀 QUICK BUILD - NeuroQuantumAI"
echo ""

# Sprawdź czy buildozer jest zainstalowany
if ! command -v buildozer &> /dev/null; then
    echo "📦 Instaluję buildozer..."
    pip install buildozer==1.5.0 cython==0.29.36
fi

# Inicjalizuj minimalne pliki
echo "📝 Inicjalizuję pliki danych..."
[ ! -f conversation_history.json ] && echo "[]" > conversation_history.json
[ ! -f editor_log.json ] && echo "[]" > editor_log.json
[ ! -f phone_activity.json ] && echo "[]" > phone_activity.json
[ ! -f knowledge_map.json ] && echo "{}" > knowledge_map.json
[ ! -f network_map.json ] && echo '{"synaptic_connections": {}}' > network_map.json

touch ai_memory.txt emotion_memory.txt evolution_log.txt long_memory.txt 2>/dev/null

echo "🔨 Buduję APK..."
buildozer android debug

if [ -f "bin/neuroquantumai-1.0-debug.apk" ]; then
    echo "✅ SUKCES! APK: bin/neuroquantumai-1.0-debug.apk"
else
    echo "❌ Nie znaleziono APK. Sprawdź logi."
fi
