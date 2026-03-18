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