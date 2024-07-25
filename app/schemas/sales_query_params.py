from pydantic import BaseModel, validator
from datetime import date


class SalesQueryParams(BaseModel):
    start_date: date
    end_date: date
    key_value: str

    @validator('end_date')
    def check_dates(cls, value, values, **kwargs):
        if 'start_date' in values and value < values['start_date']:
            raise ValueError('end_date must be after start_date')
        return value
