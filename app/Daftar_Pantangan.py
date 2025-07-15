import streamlit as st
import json
from app.analyzer import load_pantangan

def show_pantangan():
    st.title("📋 Daftar Bahan Pantangan Autoimun")
    pantangan = load_pantangan()
    st.write("Berikut adalah bahan makanan yang umum menjadi pantangan bagi penderita autoimun:")
    st.markdown("---")
    for i, bahan in enumerate(pantangan, 1):
        st.write(f"{i}. {bahan}")