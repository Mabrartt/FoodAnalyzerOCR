import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from PIL import Image
from utils.image_processor import preprocess_image, image_to_text
from utils.text_processor import clean_text, split_ingredients
from analyzer import load_pantangan, analyze_ingredients

def show_ocr():
    st.markdown(
        "<h1 style='text-align: center;'>🔍 Deteksi Bahan Makanan dari Inputan Gambar</h1>",
        unsafe_allow_html=True
    )
    st.write("Unggah gambar label makanan untuk mendeteksi bahan dan mencocokkannya dengan pantangan.")

    uploaded_file = st.file_uploader("Unggah Gambar Label Makanan", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="📷 Gambar Asli", use_column_width=True)

        with st.spinner("Memproses gambar..."):
            # Preprocessing 
            processed = preprocess_image(image)
            # st.image(processed, caption="🧪 Gambar Setelah Preprocessing", use_column_width=True)

            # ⚠️ Gunakan image asli untuk OCR jika perlu bypass preprocessing
            # extracted_text = image_to_text(image)  # tanpa preprocess
            extracted_text = image_to_text(processed)  # dengan preprocess

            # Cleaning & Splitting
            cleaned = clean_text(extracted_text)
            ingredients = split_ingredients(cleaned)

            # Analisis pantangan
            pantangan = load_pantangan()
            result = analyze_ingredients(ingredients, pantangan)

        # Output hasil OCR
        st.markdown("### 📄 Hasil OCR:")
        st.text(extracted_text if extracted_text else "(tidak terbaca)")

        # Hasil analisis pantangan
        st.markdown("### 🚫 Pantangan Ditemukan:")
        if result["Aman"]:
            st.success("Tidak ditemukan bahan pantangan. Aman dikonsumsi ✅")
        else:
            st.error("Terdapat bahan pantangan berikut:")
            for item in result["Bahan_Tidak_Aman"]:
                st.write(f"- {item}")