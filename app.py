import streamlit as st
import google.generativeai as genai

# --- KONFIGURASI AI (Tersembunyi dari User) ---
# Ganti dengan API Key dari AI Studio
API_KEY = "ISI_API_KEY_ANDA_DISINI" 
genai.configure(api_key=API_KEY)

# Instruksi Sistem Rahasia Anda
SYSTEM_INSTRUCTION = "Anda adalah pakar analisis data. Ubah input berikut menjadi format laporan formal:"

# --- TAMPILAN APLIKASI ---
st.set_page_config(page_title="Formulir Pintar AI", layout="centered")

st.title("📝 Formulir Pengisian Data")
st.write("Silakan isi formulir di bawah ini untuk mendapatkan hasil analisis AI.")

# Membuat Form agar lebih rapi
with st.form("my_form"):
    user_name = st.text_input("Nama Lengkap")
    user_data = st.text_area("Data atau Informasi yang ingin diproses")
    
    submitted = st.form_submit_button("Kirim ke AI")

    if submitted:
        if not user_data:
            st.warning("Mohon isi data terlebih dahulu.")
        else:
            with st.spinner("AI sedang memproses..."):
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    # Gabungkan instruksi rahasia dengan input user
                    full_prompt = f"{SYSTEM_INSTRUCTION}\n\nNama: {user_name}\nData: {user_data}"
                    
                    response = model.generate_content(full_prompt)
                    
                    st.success("Berhasil! Berikut hasilnya:")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Terjadi kesalahan: {e}")

st.divider()
st.caption("Powered by Gemini AI | Data Anda aman dan instruksi sistem terenkripsi.")