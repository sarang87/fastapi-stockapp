import yfinance as yf
from typing import List, Dict, Any, Optional

class Stock:
    def __init__(self, code: str) -> None:
        self.code: str = code
        self.stock_obj: yf.Ticker = yf.Ticker(self.code)
        self.history: Optional[Any] = self.get_history()
        self.current_price: float = self.get_current_price()
        self.info: Dict[str, Any] = self.get_info()
        self.name: str = self.info.get("shortName", "Unknown")
        self.max_price: float = self.get_max_price()
        self.min_price: float = self.get_min_price()
        self.growth_ratio: float = self.calc_growth_ratio()
        self.shrink_ratio: float = self.calc_shrink_ratio()
        self.risk_rating: Optional[float] = None
        self.trends: Dict[str, float] = self.get_analysis()

    def get_info(self) -> Dict[str, Any]:
        try:
            return self.stock_obj.info
        except Exception as e:
            print(f"Exception occurred for {self.code}: get_info - {e}")
            return {}

    def get_analysis(self) -> Dict[str, float]:
        analysis: Dict[str, float] = {
            "name": self.name,
            "current_price": round(self.current_price, 2),
            "max_price": round(self.max_price, 2),
            "min_price": round(self.min_price, 2),
            "growth_ratio": round(self.growth_ratio, 2),
            "shrink_ratio": round(self.shrink_ratio, 2)
        }
        for k, v in analysis.items():
            print(f"{k} : {v}\n")
        return analysis

    def get_current_price(self) -> float:
        return float(self.history['Close'].iloc[-1])

    def calc_growth_ratio(self) -> float:
        return self.max_price / self.current_price

    def calc_shrink_ratio(self) -> float:
        return self.current_price / self.min_price

    def get_history(self) -> Any:
        return self.stock_obj.history(period="5y", interval="1d")

    def get_max_price(self) -> float:
        return float(self.history["High"].max())

    def get_min_price(self) -> float:
        return float(self.history["Low"].min())
