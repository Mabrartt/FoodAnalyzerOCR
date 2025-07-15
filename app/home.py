import streamlit as st
from OCR_Deteksi_Bahan import show_ocr
from Daftar_Pantangan import show_pantangan
import base64
from pathlib import Path

st.set_page_config(page_title="FoodAnalyzer", page_icon="🍽️", layout="centered")

# Inisialisasi session state
if "page" not in st.session_state:
    st.session_state.page = "home"

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Encode logo
logo_base64 = get_base64_of_bin_file("assets/Logo.png")

# Sidebar Navigasi
with st.sidebar:
    st.markdown(
        f"""
        <div style="text-align: center; margin-top: -100px; margin-bottom: -50px;">
            <img src="data:image/png;base64,{logo_base64}" width="200" style="margin-bottom: -10px;"/>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("## 🍽️ FoodAnalyzer")
    st.markdown("### Navigasi Menu")
    st.write("Pilih halaman di bawah untuk mulai menggunakan aplikasi.")
    st.markdown("---")

    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "home"
    if st.button("🔍 OCR Deteksi Bahan", use_container_width=True):
        st.session_state.page = "ocr"
    if st.button("📋 Daftar Pantangan", use_container_width=True):
        st.session_state.page = "pantangan"

# Halaman utama session_state.page
if st.session_state.page == "home":
    st.title("🍽️ FoodAnalyzer")
    st.subheader("Solusi Cerdas untuk Deteksi Bahan Makanan dan Pantangan Autoimun")
    st.markdown("""
    Selamat datang di **FoodAnalyzer**, sebuah aplikasi berbasis AI yang dirancang untuk:

    - 🧠 Mengekstrak bahan makanan dari label menggunakan OCR (Optical Character Recognition)
    - 🚫 Menganalisis bahan yang berpotensi menjadi pantangan bagi penderita autoimun
    - 📋 Memberikan daftar bahan yang harus dihindari secara interaktif

    Silakan gunakan menu di sebelah kiri untuk mulai menggunakan aplikasi.
    """)
elif st.session_state.page == "ocr":
    show_ocr()
elif st.session_state.page == "pantangan":
    show_pantangan()