class Inventory:
    def __init__(self,):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item} to inventory")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed {item} from inventory.")
        else:
            print(f"item {item} not found in inventory")

    def list_items(self):
        if self.items:
            print("Current inventory:")
            for item in self.items:
                print(f"- {item}")
        else:
            print("inventory is empty.")
    def count_items(self):
        return len(self.items)

my_inventory = Inventory()
my_inventory.add_item("Milk")
my_inventory.add_item("Bread")
# print("current inventory:", my_inventory.items)
# my_inventory.remove_item("Milk")
# print("current inventorry after removing Milk:",my_inventory.items)
my_inventory.add_item("Eggs")
my_inventory.add_item("Butter")
my_inventory.list_items()
print(f"Total items in inventory: {my_inventory.count_items()}")