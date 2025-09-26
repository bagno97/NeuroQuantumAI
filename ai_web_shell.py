"""
ai_web_shell.py
--------------
Webowy interfejs terminala i środowiska AI dla NeuroQuantumAI.
Pozwala na uruchamianie poleceń Pythona i systemowych przez przeglądarkę telefonu lub komputera.
Integruje się z istniejącymi modułami (AIEngine, ai_shell, fact_checker, system_requirements).
"""

from flask import Flask, request, render_template_string
import subprocess
import sys
import code
import threading
import traceback

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>AI Web Shell</title>
    <style>
        body { font-family: monospace; background: #181818; color: #e0e0e0; }
        textarea, input { width: 100%; background: #222; color: #e0e0e0; border: 1px solid #444; }
        .output { white-space: pre-wrap; background: #222; padding: 1em; border-radius: 5px; }
        .warning { color: #ffb300; }
    </style>
</head>
<body>
    <h2>AI Web Shell</h2>
    <form method="post">
        <textarea name="command" rows="3" placeholder="Wpisz polecenie systemowe lub kod Python (py ...)">{{command}}</textarea><br>
        <input type="submit" value="Wykonaj">
    </form>
    {% if output %}
    <div class="output">{{output}}</div>
    {% endif %}
    {% if warning %}
    <div class="output warning">{{warning}}</div>
    {% endif %}
</body>
</html>
"""

# Kontekst Pythona dla AI (dzielony między sesjami)
ai_locals = {}

@app.route('/', methods=['GET', 'POST'])
def shell():
    output = ''
    warning = ''
    command = ''
    if request.method == 'POST':
        command = request.form.get('command', '').strip()
        if command:
            if command.startswith('py '):
                try:
                    exec(command[3:], ai_locals)
                    output = ai_locals.get('_', '')
                except Exception as e:
                    output = f"[AI Web Shell] Błąd Pythona: {e}\n" + traceback.format_exc()
            else:
                try:
                    result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
                    output = result.stdout + (result.stderr if result.stderr else '')
                except Exception as e:
                    output = f"[AI Web Shell] Błąd systemu: {e}"
        # Ostrzeżenie jeśli środowisko nie pozwala na pełną samomodyfikację
        try:
            from system_requirements import environment_report
            env_report = environment_report()
            if 'BRAK' in env_report:
                warning = '[UWAGA] Środowisko nie pozwala na pełną samomodyfikację AI!\n' + env_report
        except Exception:
            warning = '[UWAGA] Nie można sprawdzić środowiska.'
    return render_template_string(HTML, output=output, warning=warning, command=command)

if __name__ == '__main__':
    print("[AI Web Shell] Uruchom na telefonie lub komputerze: http://localhost:5000/")
    app.run(host='0.0.0.0', port=5000, debug=False)
