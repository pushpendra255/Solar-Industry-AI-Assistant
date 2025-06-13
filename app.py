import streamlit as st
from PIL import Image
from utils import analyze_image

st.title('Solar Industry AI Assistant')

uploaded_file = st.file_uploader("Upload Rooftop Satellite Image", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Rooftop Image", use_container_width=True)

    with st.spinner('Analyzing image using Gemini...'):
        try:
            # Call analysis
            analysis = analyze_image(image)

            # Show raw result
            st.success("✅ Analysis Complete!")
            st.markdown("**📝 Gemini Output:**")
            st.write(analysis)

        except Exception as e:
            st.error("❌ Error occurred during analysis.")
            st.exception(e)  # This shows full traceback in output
