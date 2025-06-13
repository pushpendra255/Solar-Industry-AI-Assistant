import streamlit as st
from PIL import Image
from utils import analyze_image

st.set_page_config(page_title="Solar AI Assistant", layout="centered")
st.title("🔆 Solar Industry AI Assistant")

uploaded_file = st.file_uploader("📤 Upload Rooftop Satellite Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        st.success("✅ Image uploaded successfully")
        image = Image.open(uploaded_file)
        st.image(image, caption="📷 Uploaded Rooftop Image", use_container_width=True)

        st.info("🔍 Running mock analysis...")
        result = analyze_image(image)

        st.success("✅ Analysis Complete!")
        st.markdown("### 📄 Rooftop Solar Report:")
        st.json(result)  # Proper structured output

    except Exception as e:
        st.error("❌ Error while processing")
        st.exception(e)
else:
    st.info("📌 Please upload a JPG or PNG rooftop image to start.")
