import streamlit as st
from PIL import Image
from utils import analyze_image

st.set_page_config(page_title="Solar AI Assistant", layout="centered")
st.title("🔆 Solar Industry AI Assistant")

uploaded_file = st.file_uploader("📤 Upload Rooftop Satellite Image", type=['jpg', 'jpeg', 'png'])

if uploaded_file:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="🖼️ Uploaded Rooftop Image", use_container_width=True)

        st.info("⏳ Analyzing... please wait")
        st.write("Image uploaded, processing...")  # Debug line
        analysis = analyze_image(image)

        if analysis:
            st.success("✅ Analysis Complete!")
            st.markdown("### 📝 Output:")
            st.write(analysis)
        else:
            st.warning("⚠️ No output received.")

    except Exception as e:
        st.error("❌ Error during processing.")
        st.exception(e)
else:
    st.caption("Please upload a rooftop image (JPG/PNG).")
