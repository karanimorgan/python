store_inventory = {
    "laptop": {
        "category": "Electronics",
        "brand": "Dell",
        "variants": [
            {
                "model": "Inspiron 15",
                "price": 750,
                "stock": 10,
                "specs": {
                    "RAM": "8GB",
                    "Storage": "512GB SSD",
                    "Processor":"Intel i5"
                }
            },
            {
                "model": "XPS 13",
                "price": 1100,
                "stock": 5,
                "specs": {
                    "RAM": "16GB",
                    "Storage": "1TB SSD",
                    "Processor": "Intel i7",
                }
            }
        ],
        "ratings": [4, 5, 5, 3, 4],
        "suppliers": ["Dell kenya", "TechWorld"],
        "on_sale": True
    },
    "Coffee Maker": {
        "category": "Appliances",
        "brand": "Philips",
        "price_tiers": {
            "basic": 80,
            "premium": 120
        },
        "stock": {
            "basic": 5,
            "premium": 3
        },
        "ratings": [5, 4, 4, 4],
        "suppliers": ["KitchenPlus"],
        "on_sale": False
    },
    "Desk Chair": {
        "category": "Funiture",
        "brand": "ErgoPro",
        "models": {
            "Standard": {
                "price":150,
                "stock": 12,
                "features": ["Adjustable height", "Mesh back"]
            },
            "Deluxe": {
                "price": 200,
                "stock": 8,
                "features": ["Adjustable arms", "Lumbar support", "Wheels"]
            }
        },
        "ratings":[3, 4, 5, 5, 4],
        "suppliers": ["OfficeFurnish"],
        "on_sale": True
    },
    "Smartphone": {
        "category": "Electronics",
        "brand": "Samsung",
        "models": [
            {
                "price": 400,
                "stock":6,
                "name": "Galaxy A54", 
            },
            {
                "price": 850,
                "stock":4,
                "name": "Galaxy S23"
            }
        ],
        "ratings": [4, 5, 4, 4, 5],
        "suppliers": ["Samsung Official", "Mobitech"],
        "on_sale": False
    }
}


# 1. create a function that returns the total stock of all items in the store inventory
def total_stock(inventory):
    total = 0
    for item in inventory.values():
        if "variants" in item:
            for variant in item["variants"]:
                total += variant.get("stock", 0)
        elif "stock" in item and isinstance(item["stock"], dict):
            total += sum(item["stock"].values())
        elif "models" in item and isinstance(item["models"], dict):
            for model in item ["models"].values():
                total += model.get("stock", 0)
        elif "models" in item and isinstance(item["models"], list):
            for model in item["models"]:
                total += model.get("stock", 0)
    return total
# print("Total stock in inventory:", total_stock(store_inventory))

# 2. return average rating of all products
def average_rating(inventory):
    total_ratings = 0
    count = 0
    for item in inventory.values():
        if "ratings" in item:
            total_ratings += sum(item["ratings"])
            count += len(item["ratings"])
    if count == 0:
        return 0
    return total_ratings/ count
# print("Average rating of products:", average_rating(store_inventory))

# 3. create a function that returns the total revenue from all products in the store inventory.
def total_revenue(inventory):
    total = 0
    for item in inventory.values():
        if "variants" in item:
            for variant in item["variants"]:
                total += variant.get("price", 0) * variant.get("stock",0)
        elif "stock" in item and isinstance(item["stock"], dict):
            for tier, stock in item["stock"].items():
                price = item ["price_tiers"].get(tier, 0)
                total += price*stock
        elif "models" in item and isinstance(item["models"], dict):
            for model in item ["models"].values():
                total += model.get("price", 0) * model.get("stock", 0)
        elif "models" in item and isinstance(item["models"], list):
            for model in item["models"]:
                total += model.get("price", 0) * model.get("stock", 0)
    return total

# print("Total revenue from products: ", total_revenue(store_inventory)) 
# 4. create a function that returns the total number of suppliers in the store inventory.
def total_suppliers(inventory):
    suppliers = set()
    for item in inventory.values():
        if "suppliers" in item:
            suppliers.update(item["suppliers"])
    return len(suppliers)
# print("Total number of suppliers:", total_suppliers(store_inventory))

# 5. create a function that returns total number of items on sale in the store inventory
def total_items_on_sale(inventory):
    count = 0
    for item in inventory.values():
        if isinstance(item, dict) and item.get("on_sale", False):
            count += 1
    return count
# print("Total number of items on sale:", total_items_on_sale(store_inventory))

# 6. create a function that returns the total number of products in a specific category
def total_products_in_category(inventory, category_name):
    count = 0
    for item in inventory.values():
        if item.get("category") == category_name:
            count+= 1
    return count
print(total_products_in_category(store_inventory, "Electronics"))


# 7. create a function that returns the total number of models in a specific product

def total_models(inventory, product_name):
    product = inventory.get(product_name)
    if not product:
        return "product not found"
    if isinstance(product, dict) and "models" in product:
        if isinstance(product["models"], dict):
            return len(product["models"])
        elif isinstance(product["models"], list):
            return len(product["models"])
    if isinstance(product, dict) and "variants" in product:
        return len(product["variants"])
    return "No models found for this product"
# print("Total models for Desk Chair:", total_models(store_inventory, "Desk Chair"))