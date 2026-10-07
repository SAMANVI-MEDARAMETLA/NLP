import re

products = [
    "Apple iPhone 15",
    "Apple iPhone 16",
    "Samsung Galaxy S24",
    "Samsung Galaxy A55",
    "Dell Laptop",
    "HP Laptop",
    "Apple Watch",
    "Wireless Mouse",
    "Bluetooth Keyboard"
]

def search_products(keyword, search_type):

    if search_type == "exact":
        pattern = r"^" + re.escape(keyword) + r"$"

    elif search_type == "prefix":
        pattern = r"^" + re.escape(keyword)

    elif search_type == "suffix":
        pattern = re.escape(keyword) + r"$"

    else:
        pattern = re.escape(keyword)

    matches = [
        p for p in products
        if re.search(pattern, p, re.IGNORECASE)
    ]

    print("\nSearch Type :", search_type)
    print("Keyword     :", keyword)

    for product in matches:
        print("-", product)

    print("Total Matches:", len(matches))


search_products("Dell Laptop", "exact")
search_products("Apple", "prefix")
search_products("Laptop", "suffix")
search_products("phone", "partial")
search_products("SAMSUNG", "partial")
