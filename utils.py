
from ai_model import call_ai_model

def analyze_image(image):
    response = call_ai_model(image)
    return response
