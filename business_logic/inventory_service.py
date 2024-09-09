from data_access.inventory_repository import InventoryRepository
from models.item_model import Item
from utils.validation import validate_item_name, validate_item_price

class InventoryService:
    def __init__(self):
        self.repo = InventoryRepository()

    def get_items(self):
        return self.repo.get_all_items()

    def get_item(self, item_name: str):
        return self.repo.get_item_by_name(item_name)

    def create_item(self, item: Item):
        validate_item_name(item.name)
        validate_item_price(item.price)
        
        return self.repo.add_item(item)

    def update_item(self, item_name: str, item: Item):
        validate_item_name(item.name)
        validate_item_price(item.price)
        
        return self.repo.update_item(item_name, item)

    def delete_item(self, item_name: str):
        return self.repo.delete_item(item_name)
