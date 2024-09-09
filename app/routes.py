from fastapi import APIRouter
from business_logic.inventory_service import InventoryService
from models.item_model import Item

router = APIRouter()
service = InventoryService()

@router.get("/items")
def get_items():
    return service.get_items()

@router.get("/items/{item_name}")
def get_item(item_name: str):
    return service.get_item(item_name)

@router.post("/items")
def create_item(item: Item):
    return service.create_item(item)

@router.put("/items/{item_name}")
def update_item(item_name: str, item: Item):
    return service.update_item(item_name, item)

@router.delete("/items/{item_name}")
def delete_item(item_name: str):
    return service.delete_item(item_name)
