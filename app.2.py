from dotenv import load_dotenv
load_dotenv() #loading all environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini model and get response
# Switching to the recommended model: gemini-1.5-flash
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def get_gemini_response(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit app
st.set_page_config(page_title="Chat with Gemini Pro") #, page_icon=":robot_face:"
st.header("Gemini LLM application")
input_text = st.text_input("input: ", key="input")
submit = st.button("Ask the question")

if submit and input_text:
    with st.spinner("Generating response..."):
        response = get_gemini_response(input_text)
        st.subheader("Response:")
        st.write(response)
elif submit and not input_text:
    st.warning("Please enter a question.")