from fastapi import HTTPException

from app.models.datamart import DatamartModel
from app.schemas.sales_query_params import SalesQueryParams


class SalesController:

    def __init__(self, datamart_model: DatamartModel):
        self.datamart_model = datamart_model

    def get_sales_by_key(self, key_type: str, data_key: str, params: SalesQueryParams) -> dict:
        try:
            filtered_data = self.datamart_model.dataframe[
                (self.datamart_model.dataframe[key_type] == params.key_value) &
                (self.datamart_model.dataframe['KeyDate'] >= params.start_date) &
                (self.datamart_model.dataframe['KeyDate'] <= params.end_date)
                ]
            total_sales = filtered_data.count()

            return {"total_sales": int(total_sales['KeySale']),
                    'name': filtered_data.iloc[0][data_key],
                    'start date': params.start_date,
                    'end date': params.end_date}
        except Exception as e:
            return {"message": 'data not found', "error": str(e)}

    def get_sales_by_key_employee(self, params: SalesQueryParams) -> dict:
        return self.get_sales_by_key('KeyEmployee', 'Employees', params)


    def get_sales_by_key_product(self, params: SalesQueryParams) -> dict:
        return self.get_sales_by_key('KeyProduct', 'Products', params)
