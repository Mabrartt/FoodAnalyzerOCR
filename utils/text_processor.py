import re

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"ingredients\s*[:\-]?", "", text)  # hapus kata 'ingredients' di awal
    text = re.sub(r"[^a-z0-9,\s]", "", text)          # buang karakter selain huruf/angka/koma/spasi
    text = re.sub(r"\s+", " ", text)                  # normalisasi spasi
    return text.strip()

def split_ingredients(text: str) -> list:
    cleaned = clean_text(text)
    ingredients = [item.strip() for item in cleaned.split(",") if item.strip()]
    return ingredients