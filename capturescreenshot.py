import os
import time
from pynput import keyboard
from PIL import ImageGrab
from ocr import extract_text
from groqllm import process_with_groq
import dotenv

dotenv.load_dotenv()

screenshot_folder = "screenshots"
os.makedirs(screenshot_folder, exist_ok=True)

def take_screenshot():
    screenshot = ImageGrab.grab()
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join(screenshot_folder, f"screenshot_{timestamp}.png")
    screenshot.save(screenshot_path)
    print(f"Screenshot saved as {screenshot_path}")
    return screenshot_path

def on_press(key):
    try:
        if key == keyboard.Key.space:
            screenshot_path = take_screenshot()
            extracted_text = extract_text(screenshot_path)
            api_key = os.getenv("GROQ_API_KEY")
            result = process_with_groq(extracted_text, api_key)
            print(f"Processed Result: {result}")
    except AttributeError:
        pass

def start_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
