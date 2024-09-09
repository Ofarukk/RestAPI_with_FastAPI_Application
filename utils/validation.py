from fastapi import HTTPException

def validate_item_name(name: str):
    if not name or not name.strip():
        raise HTTPException(status_code=400, detail="Item name cannot be empty.")
    if len(name) > 50:
        raise HTTPException(status_code=400, detail="Item name is too long (max 50 characters).")

def validate_item_price(price: float):
    if price <= 0:
        raise HTTPException(status_code=400, detail="Price must be more than 0.")
