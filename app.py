from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Choose the model HERE
model = genai.GenerativeModel("gemini-2.5-flash")

def get_gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text

st.set_page_config(page_title="Q & A Demo")
st.header("Gemini LLM Application")

user_input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit and user_input:
    response = get_gemini_response(user_input)
    st.subheader("Response from Gemini LLM")
    st.write(response)
