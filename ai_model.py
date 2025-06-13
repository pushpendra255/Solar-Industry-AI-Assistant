import os
from io import BytesIO
import google.generativeai as genai
from PIL import Image

# Gemini API key directly (for quick testing)
genai.configure(api_key="AIzaSyBeoYwJuJSaOGyWbNwzgoGl8rb2OtctSN8")

def call_ai_model(image):
    # Convert image to bytes
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    byte_data = buffer.getvalue()

    # Load Gemini model
    model = genai.GenerativeModel("gemini-pro-vision")

    # Gemini expects proper format using Part.from_data
    response = model.generate_content(
        contents=[
            genai.types.content_types.Part.from_data(
                data=byte_data, mime_type="image/jpeg"
            ),
            "Analyze this rooftop image and give detailed solar panel installation recommendations, identify shading/obstruction, suggest panel type and ROI estimate."
        ]
    )

    return response.text