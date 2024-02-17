# src/search.py
def search(query):
    products = [
        {"name": "Zapatillas Deportivas XYZ", "category": "zapatillas deportivas"},
        {"name": "Camiseta Deportiva ABC", "category": "ropa deportiva"},
    ]
    
    results = [product for product in products if query.lower() in product["category"].lower()]
    return results
