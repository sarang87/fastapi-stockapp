from fastapi import FastAPI
from app.routers import stock

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Stock App"}

app.include_router(stock.router)
