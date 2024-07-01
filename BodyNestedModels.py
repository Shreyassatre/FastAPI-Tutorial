from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# You can define an attribute to be a subtype
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list = []
    tags2: set[str] = set()


@app.put("/items/")
async def update_item(item: Item):
    return {"item": item}


# Nested Models
class Image(BaseModel):
    url: HttpUrl
    name: str


class Item2(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: list[Image] | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item2):
    results = {"item_id": item_id, "item": item}
    return results


