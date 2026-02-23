import streamlit as st
from google import genai

# Memanggil API Key dari Secrets Streamlit
api_key_saya = st.secrets["GEMINI_API_KEY"]

# Inisialisasi Client
client = genai.Client(api_key=api_key_saya)

st.title("Aplikasi AI Saya")
user_input = st.text_input("Masukkan pertanyaan:")

if user_input:
    response = client.models.generate_content(
        model="gemini-2.0-flash", # Gunakan model terbaru
        contents=user_input
    )
    st.write(response.text)
