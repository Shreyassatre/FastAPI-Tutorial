from fastapi import FastAPI, Query
from typing import Annotated, Union

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[list[str], Query(title='Query parameters', min_length=3, max_length=50)]=None): # Annotated can be used to add metadata to your parameters
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results