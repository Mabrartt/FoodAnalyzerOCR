from PIL import Image
from utils.image_processor import preprocess_image, image_to_text
from utils.text_processor import clean_text, split_ingredients
from app.analyzer import load_pantangan, analyze_ingredients
import cv2

# 1. Buka gambar
img = Image.open("ingredients_en.13.full.jpg")

# 2. Preprocessing
processed_img = preprocess_image(img)
cv2.imwrite("debug_output.jpg", processed_img)

# 3. OCR
extracted_text = image_to_text(processed_img)
print("📄 Hasil OCR:\n", extracted_text)

# 4. Bersihkan & ubah jadi list bahan
cleaned_text = clean_text(extracted_text)
ingredients = split_ingredients(cleaned_text)
print("🍴 Parsed Ingredients:\n", ingredients)

# 5. Load list pantangan
pantangan = load_pantangan()

# 6. Analisis hasil OCR
result = analyze_ingredients(ingredients, pantangan)

# 7. Tampilkan hasil
print("✅ Aman?", result["Aman"])
print("❌ Bahan pantangan yang ditemukan:", result["Bahan_Tidak_Aman"])