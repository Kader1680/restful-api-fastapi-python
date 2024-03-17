from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "all items"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/")
async def create_item(item: dict):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "updated_item": item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"item_id": item_id, "message": "Item deleted successfully"}
