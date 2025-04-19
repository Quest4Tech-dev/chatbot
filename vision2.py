from dotenv import load_dotenv
load_dotenv() #loading all environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import io

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Using the correct, current vision model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def get_gemini_response(input_prompt, image_data):
/*************  ✨ Windsurf Command ⭐  *************/
    """
    Queries the Gemini LLM model with the given input prompt and image data.

    Args:
        input_prompt (str): The text prompt to query the model with.
        image_data (bytes): The image data to query the model with.

    Returns:
        str: The response from the Gemini model.

    Raises:
        Exception: If the request to the Gemini model failed.
    """
    
/*******  72798776-c68a-4d00-82be-0a041a207ac3  *******/
    contents = []
    if input_prompt:
        contents.append(input_prompt)
    if image_data:
        contents.append(image_data)

    if not contents:
        return "Please provide an input prompt or upload an image."

    try:
        response = model.generate_content(contents)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

st.set_page_config(page_title="Gemini Image Interaction")
st.header("Gemini LLM Application with Vision")
input_prompt = st.text_input("Input Prompt: ", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image_data = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)
    image_bytes = uploaded_file.getvalue()
    image_data = {
        "mime_type": uploaded_file.type,
        "data": image_bytes
    }

submit = st.button("Tell me something about this image")

if submit:
    with st.spinner("Generating response..."):
        response = get_gemini_response(input_prompt, image_data)
        st.subheader("Response:")
        st.write(response)