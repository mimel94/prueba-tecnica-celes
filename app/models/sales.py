from dataclasses import dataclass
from datetime import date


@dataclass
class SalesModel:
    total_sales: int
    name: str
    start_date: date
    end_date: date


@dataclass
class SalesAverageModel:
    total: int
    average: float
    name: str
    start_date: date
    end_date: date
