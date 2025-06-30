from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from datetime import datetime
import pandas as pd
import os

class KeyboardApp(App):
    def build(self):
        self.last_time = None
        self.log = []
        self.layout = GridLayout(cols=10, padding=10, spacing=10)
        keys = list("QWERTYUIOPASDFGHJKLZXCVBNM")
        
        for key in keys:
            btn = Button(text=key, font_size=24)
            btn.bind(on_press=self.key_pressed)
            self.layout.add_widget(btn)
        
        self.status = Label(text="Start typing...", font_size=18, size_hint_y=0.2)
        self.layout.add_widget(self.status)
        return self.layout

    def key_pressed(self, instance):
        current_time = datetime.now()
        key = instance.text

        if self.last_time:
            delay = (current_time - self.last_time).total_seconds()
        else:
            delay = 0.0

        self.last_time = current_time
        self.status.text = f"Pressed: {key} | Delay: {round(delay, 2)}s"

        self.log.append({
            "key": key,
            "timestamp": current_time,
            "delay": delay
        })

        self.save_logs()

    def save_logs(self):
        df = pd.DataFrame(self.log)
        df.to_csv("keystroke_log.csv", index=False)

if __name__ == "__main__":
    KeyboardApp().run()
