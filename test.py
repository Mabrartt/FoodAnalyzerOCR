from PIL import Image
import pytesseract

# Set path ke tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load gambar langsung dari file
image = Image.open("sample1.jpg")  # Ganti dengan path gambar kamu
text = pytesseract.image_to_string(image, lang="eng+ind")

print("Hasil OCR:\n")
print(text)
