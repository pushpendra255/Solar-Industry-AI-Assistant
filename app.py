import streamlit as st
from PIL import Image
from utils import analyze_image

st.set_page_config(page_title="Solar AI Assistant", layout="centered")
st.title("🔆 Solar Industry AI Assistant (Gemini-based)")

# Image upload
uploaded_file = st.file_uploader("📤 Upload Rooftop Satellite Image", type=['jpg', 'jpeg', 'png'])

if uploaded_file:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="🖼️ Uploaded Rooftop Image", use_container_width=True)

        st.info("⏳ Analyzing... please wait")
        analysis = analyze_image(image)

        if analysis:
            st.success("✅ Analysis Complete!")
            st.markdown("### 📝 Output from Gemini:")
            st.write(analysis)
        else:
            st.warning("⚠️ No output received from Gemini API.")

    except Exception as e:
        st.error("❌ An error occurred.")
        st.exception(e)

else:
    st.caption("Please upload a valid satellite image of a rooftop.")
