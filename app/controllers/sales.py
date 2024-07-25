from typing import Optional

from app.controllers.datamart import DatamartController
from app.models.sales import SalesModel
from app.schemas.sales_query_params import SalesQueryParams


class SalesController:

    def __init__(self, datamart_model: DatamartController):
        self.datamart = datamart_model

    def get_sales_by_key(self, key_type: str, data_key: str, data_name: str, params: SalesQueryParams) -> Optional[SalesModel]:

        filtered_data = self.datamart.dataframe[
            (self.datamart.dataframe[key_type] == params.key_value) &
            (self.datamart.dataframe['KeyDate'] >= params.start_date) &
            (self.datamart.dataframe['KeyDate'] <= params.end_date)
            ]
        if filtered_data.empty:
            return None
        else:
            total_sales = filtered_data.count()
            sales = SalesModel(
                total_sales=int(total_sales['KeySale']),
                Name=filtered_data.iloc[0][data_key][data_name],
                start_date=params.start_date,
                end_date=params.end_date
            )
            return sales

    def get_sales_by_key_employee(self, params: SalesQueryParams) -> Optional[SalesModel]:
        return self.get_sales_by_key('KeyEmployee', 'Employees','EmployeeName', params)

    def get_sales_by_key_product(self, params: SalesQueryParams) -> Optional[SalesModel]:
        return self.get_sales_by_key('KeyProduct', 'Products', 'ProductName', params)
