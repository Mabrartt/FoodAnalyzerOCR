from PIL import Image
from utils.image_processor import preprocess_image, image_to_text
from utils.text_processor import clean_text
from jiwer import wer, cer

image_path = "yvr-ingredient-allergen-labelling-700x467_1024x1024.jpg"
ground_truth = "whole grain oat, whole grain wheat, sugar, golden syrup, salt, cinnamon, calcium carbonate"

# Load & OCR
img = Image.open(image_path)
processed = preprocess_image(img)
ocr_result = image_to_text(processed)

# Cleaning teks
cleaned_ocr = clean_text(ocr_result)
cleaned_gt = clean_text(ground_truth)

# Evaluasi
wer_score = wer(cleaned_gt, cleaned_ocr) * 100
cer_score = cer(cleaned_gt, cleaned_ocr) * 100

# Tampilkan
print("📄 Ground Truth   :", cleaned_gt)
print("🧠 OCR Output     :", cleaned_ocr)
print(f"📊 WER: {wer_score:.2f}%")
print(f"📊 CER: {cer_score:.2f}%")