from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="Backbone API",
    description="Backend API for the Backbone project",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:4173"],  # Svelte dev and preview ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None

# In-memory storage (replace with database in production)
items_db = []
item_id_counter = 1

@app.get("/")
async def root():
    return {"message": "Welcome to Backbone API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "backbone-api"}

@app.get("/items", response_model=List[Item])
async def get_items():
    return items_db

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    global item_id_counter
    new_item = Item(
        id=item_id_counter,
        name=item.name,
        description=item.description
    )
    items_db.append(new_item)
    item_id_counter += 1
    return new_item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    for i, existing_item in enumerate(items_db):
        if existing_item.id == item_id:
            updated_item = Item(
                id=item_id,
                name=item.name,
                description=item.description
            )
            items_db[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for i, item in enumerate(items_db):
        if item.id == item_id:
            deleted_item = items_db.pop(i)
            return {"message": f"Item {deleted_item.name} deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 