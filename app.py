import streamlit as st
from PIL import Image
from utils import analyze_image

st.set_page_config(page_title="Solar Industry AI Assistant", layout="centered")
st.title("🔆 Solar Industry AI Assistant")

st.markdown("Upload a satellite rooftop image and get a solar panel recommendation, ROI estimate, and obstruction analysis.")

uploaded_file = st.file_uploader("📤 Upload Rooftop Satellite Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="🖼️ Uploaded Rooftop Image", use_container_width=True)

        with st.spinner("🔍 Analyzing rooftop image..."):
            analysis = analyze_image(image)

        st.success("✅ Analysis Complete!")
        st.markdown("### 🔎 Results:")
        st.write(analysis)

    except Exception as e:
        st.error("❌ An error occurred during analysis.")
        st.exception(e)
else:
    st.info("📸 Please upload a rooftop satellite image.")
