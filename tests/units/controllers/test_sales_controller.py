from datetime import date
from unittest.mock import patch

from app.controllers.datamart import DatamartController
from app.controllers.sales import SalesController
from app.schemas.sales_query_params import SalesQueryParams


class TestSalesController:
    def test_given_valid_sales_params_when_query_sales_by_employee_then_return_correct_sales_data(self, mocker,
                                                                                                  data_fixture_employee):
        mocker.patch.object(DatamartController, 'load_data', return_value=data_fixture_employee)
        data_controller = SalesController(datamart_model=DatamartController())
        response = data_controller.get_sales_by_key_employee(params=SalesQueryParams(start_date=date(2023, 11, 1),
                                                                          end_date=date(2024, 1, 31),
                                                                          key_value='1|569'))
        assert response.total_sales == 113
        assert response.start_date == date(2023,11,1)
        assert response.end_date == date(2024,1,31)
        assert response.name == 'ROMERO MEZA FREDDY JESUS'

    def test_given_invalid_sales_params_when_query_sales_by_employee_then_return_none_sales_data(self, mocker,
                                                                                                 data_fixture_employee):
        mocker.patch.object(DatamartController, 'load_data', return_value=data_fixture_employee)
        data_controller = SalesController(datamart_model=DatamartController())
        response = data_controller.get_sales_by_key_employee(params=SalesQueryParams(start_date=date(2023, 11, 1),
                                                                                     end_date=date(2024, 1, 31),
                                                                                     key_value='1|564'))
        assert response is None


    def test_given_valid_sales_params_when_query_sales_by_store_then_return_correct_sales_data(self, mocker,
                                                                                               data_fixture_store):
        mocker.patch.object(DatamartController, 'load_data', return_value=data_fixture_store)
        data_controller = SalesController(datamart_model=DatamartController())
        response = data_controller.get_sales_by_key_store(params=SalesQueryParams(start_date=date(2023, 11, 1),
                                                                          end_date=date(2024, 1, 31),
                                                                          key_value='1|023'))
        assert response.total_sales == 1512
        assert response.start_date == date(2023,11,1)
        assert response.end_date == date(2024,1,31)
        assert response.name == 'UNICO BQLLA'


    def test_given_invalid_sales_params_when_query_sales_by_store_then_return_correct_sales_data(self, mocker,
                                                                                               data_fixture_store):
        mocker.patch.object(DatamartController, 'load_data', return_value=data_fixture_store)
        data_controller = SalesController(datamart_model=DatamartController())
        response = data_controller.get_sales_by_key_store(params=SalesQueryParams(start_date=date(2023, 11, 1),
                                                                          end_date=date(2024, 1, 31),
                                                                          key_value='1|021'))
        assert response is None
