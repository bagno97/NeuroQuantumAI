"""
chat_web.py
-----------
Graficzny webowy czat dla NeuroQuantumAI z podglądem stanu pracy AI, spinnerem, powiadomieniami i obsługą wszystkich funkcji (fact-checking, samomodyfikacja, pobieranie danych, zgody).
"""

import importlib
try:
    _flask = importlib.import_module('flask')
    Flask = _flask.Flask
    request = _flask.request
    render_template_string = _flask.render_template_string
    jsonify = _flask.jsonify
except Exception:
    Flask = None
    request = None
    def render_template_string(*args, **kwargs):
        return "Flask nie jest zainstalowany. Zainstaluj pakiet 'flask' aby uruchomić czat webowy."
    def jsonify(obj):
        import json
        return json.dumps(obj)
import threading
import time

# Import AIEngine (przykład — dostosuj do swojej implementacji)
from AIEngine import AIEngine

app = Flask(__name__) if Flask else None
ai = AIEngine()

# Prosty status pracy AI (współdzielony między wątkami)
ai_status = {"stage": "czeka na polecenie", "busy": False}

HTML = """
<!DOCTYPE html>
<html lang=\"pl\">
<head>
    <meta charset=\"UTF-8\">
    <title>NeuroQuantumAI — Czat</title>
    <style>
        body { font-family: Arial, sans-serif; background: #181818; color: #e0e0e0; }
        #chatbox { width: 100%; height: 60vh; background: #222; border-radius: 8px; padding: 1em; overflow-y: auto; }
        .msg { margin: 0.5em 0; }
        .user { color: #8ecae6; }
        .ai { color: #ffd166; }
        #status { margin: 1em 0; font-weight: bold; }
        #spinner { display: none; }
        .spinner { border: 4px solid #444; border-top: 4px solid #ffd166; border-radius: 50%; width: 24px; height: 24px; animation: spin 1s linear infinite; display: inline-block; }
        @keyframes spin { 100% { transform: rotate(360deg); } }
        #notify { background: #073b4c; color: #fff; padding: 0.5em 1em; border-radius: 5px; margin: 1em 0; display: none; }
    </style>
    <script>
        function scrollChat() {
            var chatbox = document.getElementById('chatbox');
            chatbox.scrollTop = chatbox.scrollHeight;
        }
        function showSpinner(show) {
            document.getElementById('spinner').style.display = show ? 'inline-block' : 'none';
        }
        function showNotify(msg) {
            var n = document.getElementById('notify');
            n.innerText = msg;
            n.style.display = 'block';
            setTimeout(function(){ n.style.display = 'none'; }, 4000);
        }
        function sendMsg() {
            var input = document.getElementById('msg');
            var msg = input.value.trim();
            if (!msg) return;
            input.value = '';
            showSpinner(true);
            fetch('/send', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({msg: msg})
            })
            .then(r => r.json())
            .then(data => {
                document.getElementById('chatbox').innerHTML = data.chat_html;
                document.getElementById('status').innerText = data.status;
                showSpinner(false);
                if (data.notify) showNotify(data.notify);
                scrollChat();
            });
        }
        function pollStatus() {
            fetch('/status').then(r => r.json()).then(data => {
                document.getElementById('status').innerText = data.status;
                if (data.notify) showNotify(data.notify);
            });
            setTimeout(pollStatus, 2000);
        }
        window.onload = function() { scrollChat(); pollStatus(); }
    </script>
</head>
<body>
    <h2>NeuroQuantumAI — Czat</h2>
    <div id="chatbox">{{chat_html|safe}}</div>
    <div id="status">{{status}}</div>
    <div id="spinner"><span class="spinner"></span> AI pracuje...</div>
    <div id="notify"></div>
    <form onsubmit="sendMsg(); return false;">
        <input id="msg" type="text" autocomplete="off" placeholder="Wpisz wiadomość..." style="width:80%;">
        <button type="submit">Wyślij</button>
    </form>
</body>
</html>
"""

# Prosta historia czatu (w RAM, można rozbudować o plik/DB)
chat_history = []

if app:
    @app.route('/', methods=['GET'])
    def index():
        return render_template_string(HTML, chat_html=render_chat(), status=ai_status["stage"])

def render_chat():
    html = ''
    for who, msg in chat_history:
        cls = 'user' if who == 'user' else 'ai'
        html += f'<div class="msg {cls}"><b>{who.upper()}:</b> {msg}</div>'
    return html

if app:
    @app.route('/send', methods=['POST'])
    def send():
        data = request.get_json()
        user_msg = data.get('msg', '')
        chat_history.append(('user', user_msg))
        ai_status["stage"] = "AI analizuje dane..."
        ai_status["busy"] = True
        notify = None
        def ai_task():
            try:
                # Etap 1: Analiza wejścia
                ai_status["stage"] = "AI analizuje dane..."
                time.sleep(0.5)
                # Etap 2: Fact-checking
                if 'sprawdź' in user_msg.lower() or 'fact' in user_msg.lower():
                    ai_status["stage"] = "AI sprawdza fakty..."
                    time.sleep(0.7)
                # Etap 3: Czekanie na zgodę (symulacja)
                if 'zgoda' in user_msg.lower():
                    ai_status["stage"] = "AI czeka na zgodę użytkownika..."
                    time.sleep(0.7)
                # Odpowiedź AI
                ai_reply = ai.process_input(user_msg)
                chat_history.append(('ai', ai_reply))
                ai_status["stage"] = "czeka na polecenie"
                ai_status["busy"] = False
            except Exception as e:
                chat_history.append(('ai', f"[Błąd AI] {e}"))
                ai_status["stage"] = "Błąd AI"
                ai_status["busy"] = False
        threading.Thread(target=ai_task, daemon=True).start()
        return jsonify({
            'chat_html': render_chat(),
            'status': ai_status["stage"],
            'notify': notify
        })

if app:
    @app.route('/status', methods=['GET'])
    def status():
        # Możesz dodać powiadomienia o zakończeniu zadań w tle
        notify = None
        if not ai_status["busy"] and chat_history and chat_history[-1][0] == 'ai':
            if 'INTERNET' in chat_history[-1][1]:
                notify = 'AI zakończyła pobieranie danych z internetu.'
        return jsonify({'status': ai_status["stage"], 'notify': notify})

if __name__ == '__main__':
    if app:
        print("[AI Chat] Uruchom na telefonie lub komputerze: http://localhost:5000/")
        app.run(host='0.0.0.0', port=5000, debug=False)
    else:
        print("[AI Chat] Flask nie jest zainstalowany. Uruchom: pip install flask")
