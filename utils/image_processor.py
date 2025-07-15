import json
from typing import List, Dict, Union
from rapidfuzz import fuzz
import pytesseract
import numpy as np
from PIL import Image, ImageOps, ImageEnhance
import cv2

import pytesseract

def image_to_text(image: Union[Image.Image, np.ndarray], preprocess=False) -> str:
    if preprocess:
        if isinstance(image, Image.Image):
            image = preprocess_image(image)
        elif isinstance(image, np.ndarray):
            image = preprocess_image(Image.fromarray(image))

    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)

    text = pytesseract.image_to_string(image, lang="eng+ind")
    return text.strip()


def deskew_image(image: np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    coords = np.column_stack(np.where(binary > 0))
    angle = cv2.minAreaRect(coords)[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

def preprocess_image(pil_image: Image.Image) -> np.ndarray:
    image = np.array(pil_image)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return gray
