from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10, q: str = None):
    if q:
        return {"skip": skip, "limit": limit, "q": q}
    else:
        return {"skip": skip, "limit": limit}