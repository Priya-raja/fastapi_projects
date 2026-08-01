from fastapi import FastAPI, Query, HTTPException
from models import MenuItem, MenuResponse
from data import menu_items

app = FastAPI(
    title="Chai Point menu API",
    description="Read only menu API for kiosk displays and mobile app"
    )

@app.get("/")
def root():
    return {"message": "Welcome to the Chai Point menu API!"}

@app.get("/menu", response_model=MenuResponse)
def get_menu(category:str | None = Query(None, description="Filter menu items by category")):
    if category:
        filtered = [item for item in menu_items if item.get("category","") == category.lower()]
    
        if not filtered:
           raise HTTPException(status_code=404, detail="No menu items found for the specified category")
        return MenuResponse(count=len(filtered), items=filtered)

    return MenuResponse(count=len(menu_items), items=menu_items)

@app.get("/menu/{item_id}", response_model=MenuItem)
def get_menu_item(item_id: int):
    for item in menu_items:
        if item.get("id") == item_id:
            return item
  
    raise HTTPException(status_code=404, detail="Menu item with id {item_id} not found")
   

