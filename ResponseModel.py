from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items2/", response_model= list[Item])
async def read_items():
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]



# Return Type and Data Filtering
class BaseUser(BaseModel):
    username: str
    email: str
    full_name: str | None = None


class UserIn(BaseUser):
    password: str


@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user


# Other Return Type Annotations
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi import Response

@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.example.com")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})