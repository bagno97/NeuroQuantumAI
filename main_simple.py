"""
main_simple.py
Uproszczony plik uruchamiający dla testów na Androidzie.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SimpleApp(App):
    def build(self):
        # Główny layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Chat log
        self.chat_log = Label(
            text="🚀 NeuroQuantumAI - DZIAŁAM! 🚀\nWpisz wiadomość poniżej:",
            size_hint_y=0.7,
            text_size=(None, None),
            halign='left',
            valign='top'
        )
        
        # Input
        self.text_input = TextInput(
            hint_text="Napisz coś...",
            size_hint_y=0.2,
            multiline=False
        )
        
        # Button
        send_button = Button(
            text="Wyślij",
            size_hint_y=0.1
        )
        send_button.bind(on_press=self.send_message)
        
        # Dodaj do layoutu
        layout.add_widget(self.chat_log)
        layout.add_widget(self.text_input)
        layout.add_widget(send_button)
        
        return layout
    
    def send_message(self, instance):
        user_text = self.text_input.text.strip()
        if user_text:
            # Prosty odpowiedź bot
            response = f"Echo: {user_text}"
            self.chat_log.text += f"\n👤: {user_text}\n🤖: {response}\n"
            self.text_input.text = ""

if __name__ == "__main__":
    SimpleApp().run()