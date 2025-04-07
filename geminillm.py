from google import genai
from google.genai import types

def process_with_gemini(text, api_key, model="gemini-2.0-flash"):
    """Process text using Google Gemini API with Google Search grounding"""
    print(f"Processing text with Gemini {model}")
    
    try:
        client = genai.Client(api_key=api_key)
        
        prompt = f"""You are an assistant and aptitude expert that analyzes multiple choice questions and determines the correct answer.
        
        Tell me which answer is correct. Only tell me the correct answer letter (A, B, C, D, etc.) and answer, strictly no explanation needed, no more extra characters in the response.
        
        Question: {text}"""
        
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.1,  
                tools=[types.Tool(
                    google_search=types.GoogleSearchRetrieval()
                )]
            )
        )
        
        answer = response.text.strip() if hasattr(response, 'text') else response.candidates[0].content.parts[0].text
        print(f"Processed text with Gemini {model}")
        return f"{model}: {answer}"
    
    except Exception as e:
        print(f"Error ({model}): {str(e)}")
        return f"Failed to process with {model}: {str(e)}"