import requests

def get_ingredients_list(product_name: str):
    url = f"https://world.openfoodfacts.org/cgi/search.pl"
    params = {
        'search_terms': product_name,
        'search_simple': 1,
        'action': 'process',
        'json': 1,
        "page_size": 1
    }
    res = requests.get(url, params=params)
    products = res.json().get('products',[])
    if not products:
        return None
    return products[0].get('ingredients_text_en') or products[0].get('ingredients_text')

if __name__ == "__main__":
    product = input("Masukkan nama produk: ")
    ingredients = get_ingredients_list(product)
    if ingredients:
        print("Bahan-bahan:", ingredients)
    else:
        print("Produk tidak ditemukan atau tidak ada data bahan.")