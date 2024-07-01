from fastapi import FastAPI

# Create an app instance.
app = FastAPI()

# path operation decorator
@app.get("/")
# path operation function
async def root():
    return {"message": "Hello World"}