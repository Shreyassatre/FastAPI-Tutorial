from fastapi import FastAPI

app = FastAPI()

# Path Parameters, Here item_id is path parameter
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

# Path parameters with types
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# in this case if try to input string then it will throw data validation error:
# Please correct the following validation errors and try again.
# Value must be an integer

# All the data validation is performed under the hood by Pydantic, so you get all the benefits from it. And you know you are in good hands.



#Order Matters
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# Because path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the one for /users/{user_id}
# Otherwise, the path for /users/{user_id} would match also for /users/me, "thinking" that it's receiving a parameter user_id with a value of "me"




# Enum:

# If you have a path operation that receives a path parameter, but you want the possible valid path parameter values to be predefined, you can use a standard Python Enum
from enum import Enum

# By inheriting from str the API docs will be able to know that the values must be of type string and will be able to render correctly.
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}




# Path parameters containing paths
# Using an option directly from Starlette you can declare a path parameter containing a path using a URL like:/files/{file_path:path}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}