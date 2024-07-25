from dataclasses import dataclass
from datetime import date


@dataclass
class SalesModel:
    total_sales: int
    Name: str
    start_date: date
    end_date: date
