import os
from breast.utils.common import decodeImage
from breast.pipeline.predict import PredictionPipeline

import streamlit as st
from PIL import Image

# Streamlit UI
st.title("Cancer Detection from Image")
st.write("Upload an image to check if it has cancer or not.")

# Upload Image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Save the uploaded file to a temporary location
    temp_file_path = f"temp_{uploaded_file.name}"
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Initialize the prediction pipeline with the file path
    pipeline = PredictionPipeline(temp_file_path)

    # Predict using the pipeline
    result = pipeline.predict()

    # Make the result more prominent
    if result:
        st.markdown(f"<h2 style='text-align: center; color: green;'>{result[0]['image']}</h2>", unsafe_allow_html=True)

    # Clean up the temporary file
    os.remove(temp_file_path)