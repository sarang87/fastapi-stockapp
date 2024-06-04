from fastapi import APIRouter, HTTPException
from app.models.stock import Stock
from app.utils.stock_data import stock_list
import time

router = APIRouter(
    prefix="/stocks",
    tags=["stocks"]
)

@router.get("/{stock_code}")
def get_stock(stock_code: str):
    try:
        stock = Stock(stock_code)
        return stock.get_analysis()
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Stock {stock_code} not found - {e}")

@router.get("/")
def get_all_stocks():
    stock_results = []
    for name in stock_list:
        try:
            stock = Stock(name)
            stock_results.append(stock.get_analysis())
            time.sleep(1)  # Pause to avoid rate limiting
        except Exception as e:
            print(f"Exception on stock: {name} - {e}")
    return stock_results
