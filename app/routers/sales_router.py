from fastapi import APIRouter, Depends, Query

from app.controllers.sales import SalesController
from app.dependencies.dependencies import get_datamart_model
from app.models.datamart import DatamartModel
from app.schemas.sales_query_params import SalesQueryParams
from datetime import date

router = APIRouter()


@router.get("/sales/by-employee/{employee_id}")
def sales_by_employee(
    employee_id: str,
    start_date: date = Query(..., description="Start date of the period"),
    end_date: date = Query(..., description="End date of the period"),
    datamart: DatamartModel = Depends(get_datamart_model)
):
    sales_controller = SalesController(datamart)
    params = SalesQueryParams(start_date=start_date, end_date=end_date, key_value=employee_id)
    return sales_controller.get_sales_by_key(params)
