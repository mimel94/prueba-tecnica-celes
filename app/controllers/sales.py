from fastapi import HTTPException

from app.models.datamart import DatamartModel
from app.schemas.sales_query_params import SalesQueryParams


class SalesController:

    def __init__(self, datamart_model: DatamartModel):
        self.datamart_model = datamart_model

    def get_sales_by_key(self, params: SalesQueryParams) -> dict:
        try:
            filtered_data = self.datamart_model.dataframe[
                (self.datamart_model.dataframe['KeyEmployee'] == params.key_value) &
                (self.datamart_model.dataframe['KeyDate'] >= params.start_date) &
                (self.datamart_model.dataframe['KeyDate'] <= params.end_date)
            ]
            total_sales = filtered_data.count()

            return {"total_sales": int(total_sales['KeySale']),
                    'employee name': filtered_data.iloc[0]['Employees']['EmployeeName']}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))