
import os
import base64
from io import BytesIO
import google.generativeai as genai

# Directly set your Gemini API key (for testing only – avoid in production)
genai.configure(api_key="AIzaSyBeoYwJuJSaOGyWbNwzgoGl8rb2OtctSN8")

def call_ai_model(image):
    # Convert image to base64
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    image_data = base64.b64encode(buffer.getvalue()).decode("utf-8")

    # Initialize Gemini model
    model = genai.GenerativeModel('gemini-pro-vision')

    # Send image and prompt for solar rooftop analysis
    response = model.generate_content([
        {
            "type": "image",
            "data": image_data,
        },
        {
            "type": "text",
            "text": "Analyze this rooftop image and give detailed solar panel installation recommendations, identify shading/obstruction, suggest panel type and ROI estimate.",
        }
    ])

    return response.text