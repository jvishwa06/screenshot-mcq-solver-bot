from PIL import Image
from surya.recognition import RecognitionPredictor
from surya.detection import DetectionPredictor

def extract_text(image_path):
    """Extract text from the image using Surya OCR"""
    print("Extracting text with OCR...")

    try:
        image = Image.open(image_path)
        langs = ["en"]

        recognition_predictor = RecognitionPredictor()
        detection_predictor = DetectionPredictor()

        result = recognition_predictor([image], [langs], detection_predictor)

        if result and hasattr(result[0], 'text_lines'):
            text_lines = result[0].text_lines  
            text = [line.text for line in text_lines]  
            return "\n".join(text) if text else "No text detected in the image"
        else:
            return "No text detected in the image"

    except Exception as e:
        print(f"Error during OCR: {e}")
        return "Failed to extract text from image"
