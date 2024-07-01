# You can define Header parameters the same way you define Query, Path and Cookie parameters.

from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header(convert_underscores=False)] = None): #If for some reason you need to disable automatic conversion of underscores to hyphens, set the parameter convert_underscores of Header to False
    return {"User-Agent": user_agent}



#Duplicate Headers
@app.get("/items2/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}