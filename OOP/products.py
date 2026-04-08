class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, category):
        product = {
            "name":name,
            "price":price,
            "category":category
        }
        self.products.append(product)
        print(f"added product: {name}")

    def list_products(self):
        if self.products:
            print("current products:")
            for product in self.products:
                print(f"- {product.get('name')} (${product.get('price')}) in category {product.get('category')}")
        else:
            print("no product available.")
    def find_product_by_name(self, name):
        result = []
        for product in self.products:
            if product.get("name") == name:
                result.append(product)
        return result
        
# my_product = ProductManager()
# my_product.add_product("Bata shoes", 1500, "footwear")
# print(my_product.products)
if __name__ == "__main__":
    manager = ProductManager()
    manager.add_product("Bata shoes", 1500, "footwear")
    manager.add_product
    print(manager.products)
manager.list_products()
manager.find_product_by_name("Bata shoes")