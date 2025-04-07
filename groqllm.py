import requests

def process_with_groq(text, api_key, model="llama-3.3-70b-versatile"):
    """Send text to Groq API for MCQ analysis"""
    print(f"Processing text with Groq {model}...")
    
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a highly skilled and specialized assistant with advanced expertise in solving complex and difficult aptitude and reasoning problems. You are capable of solving very challenging questions by breaking them down and reasoning through the solution step by step. Your task is to analyze the given multiple-choice question, reason through it logically, and determine the correct answer with precision. Provide the answer after completing a detailed thought process, without skipping any critical steps."
                },
                {
                    "role": "user",
                    "content": f"This is a multiple-choice aptitude question. Based on your advanced expertise and reasoning skills, carefully analyze the question and answer choices. Solve the question step by step, reasoning through each part of the problem iteratively. Once you reach the final solution, provide only the correct answer in this format: 'option : answer', for example: 'A: 55'. **Strictly follow this format**. No explanations, no extra words, no additional characters. Just the answer in the format 'option : answer'.\n\n{text}"
                }
            ]
        }

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload
        )
        
        if response.status_code != 200:
            print(f"Error ({model}): {response.status_code}")
            print(response.text)
            return f"Failed to process with {model}"

        response_data = response.json()
        answer = response_data["choices"][0]["message"]["content"]
        print(f"Processed text with Groq {model}")
        return f"{model}: {answer}"

    except Exception as e:
        print(f"Error ({model}): {str(e)}")
        return f"Failed to process with {model}: {str(e)}"
