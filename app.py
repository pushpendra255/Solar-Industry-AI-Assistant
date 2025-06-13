
import streamlit as st
from PIL import Image
from utils import analyze_image

st.title('Solar Industry AI Assistant')

uploaded_file = st.file_uploader("Upload Rooftop Satellite Image", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Rooftop Image", use_column_width=True)

    with st.spinner('Analyzing image...'):
        analysis = analyze_image(image)
    st.success('Analysis Complete!')
    st.write(analysis)
