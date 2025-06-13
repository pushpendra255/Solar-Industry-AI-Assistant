
import openai
import base64
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def call_ai_model(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    image_bytes = base64.b64encode(buffered.getvalue()).decode('utf-8')

    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "system", "content": "Provide detailed analysis of rooftop solar potential, including recommended panel type, estimated ROI, and possible obstructions."},
            {"role": "user", "content": [
                {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64," + image_bytes}}
            ]}
        ],
        max_tokens=500
    )

    return response.choices[0].message.content
