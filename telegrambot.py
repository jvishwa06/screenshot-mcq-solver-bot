import os
import time
from concurrent.futures import ThreadPoolExecutor
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from ocr import extract_text
from geminillm import process_with_gemini
from groqllm import process_with_groq
from mixtralllm import process_with_mixtral
import dotenv

dotenv.load_dotenv()

api_key = os.getenv("TELEGRAM_BOT_API_KEY")
screenshot_folder = "received_images"
os.makedirs(screenshot_folder, exist_ok=True)

async def download_image(update: Update, context: CallbackContext):
    photo_file = await update.message.photo[-1].get_file() 
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    image_path = os.path.join(screenshot_folder, f"image_{timestamp}.jpg")
    
    await photo_file.download_to_drive(image_path)
    print(f"Image saved as {image_path}")
    
    extracted_text = extract_text(image_path)
    
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    groq_api_key = os.getenv("GROQ_API_KEY")
    mixtral_api_key = os.getenv("MIXTRAL_API_KEY")
    
    final_response = process_all_models(extracted_text, gemini_api_key, groq_api_key, mixtral_api_key)
    
    await update.message.reply_text(f"Question: {extracted_text}\n\nAnswer:\n{final_response}")

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Send me an image, and I'll process it for you.")

def process_all_models(text, gemini_api_key, groq_api_key, mixtral_api_key):
    """Process the text using all models concurrently"""
    
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(process_with_gemini, text, gemini_api_key),
            executor.submit(process_with_groq, text, groq_api_key),
            executor.submit(process_with_mixtral, text, mixtral_api_key)
        ]
        
        results = [future.result() for future in futures]
    
    return "\n\n".join(results)

def main():
    application = Application.builder().token(api_key).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, download_image))
    application.run_polling()
