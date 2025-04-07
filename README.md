# Invisible - AI MCQ Solver

A tool that answer multiple-choice questions, extracts text using OCR, and analyzes the questions using multiple AI models to provide answers.

## Features

- Screenshot capture via keyboard shortcut (Space key)
- Telegram bot integration for sending images directly
- Optical Character Recognition (OCR) using Surya OCR
- Multiple AI model processing:
  - Google Gemini
  - Groq (Llama 3.3)
  - Mistral AI
- Parallel processing:
  - Uses Python's `concurrent.futures` for parallel API calls
  - Implements `asyncio` for asynchronous operations in the Telegram bot

## Setup

### Prerequisites

- Python 3.8+
- API keys for:
  - Groq
  - Google Gemini 
  - Mistral AI
  - Telegram Bot API

### Installation

1. Clone this repository
   ```
   git clone https://github.com/jvishwa06/invisible.git
   cd Invisible
   ```

2. Install dependencies
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key
   TELEGRAM_BOT_API_KEY=your_telegram_bot_api_key
   MIXTRAL_API_KEY=your_mixtral_api_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

## Usage

### Screenshot Mode

Run the screenshot capture utility:
```
python capturescreenshot.py
```

Press the Space key to capture a screenshot, which will:
1. Save the screenshot in the "screenshots" folder
2. Extract text using OCR
3. Process the text with Groq AI
4. Display the answer in the console

### Telegram Bot Mode

Run the Telegram bot:
```
python main.py
```

The bot will start and listen for incoming messages. Send an image through the bot, and it will:
1. Save the image in the "received_images" folder
2. Extract text using OCR
3. Process the text with all three AI models (Gemini, Groq, Mistral)
4. Reply with the question text and answers from each model

## Project Structure

- `main.py` - Main entry point for the Telegram bot application
- `capturescreenshot.py` - Utility for capturing screenshots via keyboard shortcut
- `ocr.py` - Text extraction module using Surya OCR
- `telegrambot.py` - Telegram bot implementation
- `geminillm.py` - Google Gemini API integration
- `groqllm.py` - Groq API integration
- `mixtralllm.py` - Mistral AI integration

## License

[MIT License](LICENSE)