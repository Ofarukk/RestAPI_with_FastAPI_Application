from models.item_model import Item

class InventoryRepository:
    def __init__(self):
        self.items_db = {
            "laptop": {"name": "laptop", "price": 1200},
            "phone": {"name": "phone", "price": 800},
        }

    def get_all_items(self):
        return self.items_db

    def get_item_by_name(self, item_name: str):
        return self.items_db.get(item_name)

    def add_item(self, item: Item):
        self.items_db[item.name] = {"name": item.name, "price": item.price}
        return self.items_db[item.name]

    def update_item(self, item_name: str, item: Item):
        if item_name in self.items_db:
            self.items_db[item_name] = {"name": item.name, "price": item.price}
        return self.items_db.get(item_name)

    def delete_item(self, item_name: str):
        return self.items_db.pop(item_name, None)
