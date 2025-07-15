import json
from typing import List, Dict
from rapidfuzz import fuzz

def load_pantangan(filepath: str = "app/prohibition_list.json") -> List[str]:
    with open(filepath, "r") as f:
        return json.load(f)

def analyze_ingredients(ingredients: List[str], prohibition_list: List[str], threshold: int = 90) -> Dict:
    result = {"Aman": True, "Bahan_Tidak_Aman": []}
    lower_prohibition = [p.lower() for p in prohibition_list]

    # Daftar bahan aman
    whitelist = ["rice flour", "corn starch", "cassava flour", "tapioca starch"]

    for ingredient in ingredients:
        ing = ingredient.lower().strip()

        # Lewati kalau masuk whitelist
        if any(white in ing for white in whitelist):
            continue

        # Cek match literal dulu
        if any(proh == ing for proh in lower_prohibition):
            result["Aman"] = False
            result["Bahan_Tidak_Aman"].append(ingredient)
            continue

        # Cek match berdasarkan kata yang berdiri sendiri
        ing_tokens = ing.split()
        if any(proh in ing_tokens for proh in lower_prohibition):
            result["Aman"] = False
            result["Bahan_Tidak_Aman"].append(ingredient)
            continue

        # Cek fuzzy match dengan kontrol ketat
        for prohibition in lower_prohibition:
            score = fuzz.token_sort_ratio(prohibition, ing)
            if score >= threshold and prohibition in ing:
                result["Aman"] = False
                result["Bahan_Tidak_Aman"].append(ingredient)
                break
    return result