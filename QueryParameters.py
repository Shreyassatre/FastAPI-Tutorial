# When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"},{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"},{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"},{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"},{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]



# Optioanal Parameters
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None): # Here q is optional parameter
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}



#Query Parameters Type conversion:
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# Required query parameters
# If you don't want to add a specific value but just make it optional, set the default as None.
@app.get("/products/{product_id}")
async def read_user_item(
    product_id: str, needy: str, skip: int = 0, limit: int | None = None # Here limit is optional parameter
):
    item = {"product_id": product_id, "needy": needy, "skip": skip, "limit": limit}
    return item

