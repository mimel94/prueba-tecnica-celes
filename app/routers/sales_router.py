from fastapi import APIRouter, Depends, Query, HTTPException

from app.controllers.datamart import DatamartController
from app.controllers.sales import SalesController
from app.decorators.login_required import login_required
from app.dependencies.dependencies import get_datamart_controller

from app.schemas.sales_query_params import SalesQueryParams
from datetime import date

router = APIRouter()


@router.get("/sales/by-employee/{employee_id}", dependencies=[Depends(login_required)])
def sales_by_employee(
    employee_id: str,
    start_date: date = Query(..., description="Start date of the period"),
    end_date: date = Query(..., description="End date of the period"),
    datamart: DatamartController = Depends(get_datamart_controller)
):
    sales_controller = SalesController(datamart)
    params = SalesQueryParams(start_date=start_date, end_date=end_date, key_value=employee_id)
    data = sales_controller.get_sales_by_key_employee(params)
    if data:
        return data
    return HTTPException(status_code=404, detail='Employee not found')


@router.get("/sales/by-product/{product_id}", dependencies=[Depends(login_required)])
def sales_by_product(
    product_id: str,
    start_date: date = Query(..., description="Start date of the period"),
    end_date: date = Query(..., description="End date of the period"),
    datamart: DatamartController = Depends(get_datamart_controller)
):
    sales_controller = SalesController(datamart)
    params = SalesQueryParams(start_date=start_date, end_date=end_date, key_value=product_id)
    data = sales_controller.get_sales_by_key_product(params)
    if data:
        return data
    return HTTPException(status_code=404, detail='Product not found')


@router.get("/sales/by-store/{store_id}", dependencies=[Depends(login_required)])
def sales_by_store(
    store_id: str,
    start_date: date = Query(..., description="Start date of the period"),
    end_date: date = Query(..., description="End date of the period"),
    datamart: DatamartController = Depends(get_datamart_controller)
):
    sales_controller = SalesController(datamart)
    params = SalesQueryParams(start_date=start_date, end_date=end_date, key_value=store_id)
    data = sales_controller.get_sales_by_key_store(params)
    if data:
        return data
    return HTTPException(status_code=404, detail='Store not found')


@router.get("/total-and-average-sales/by-store/{store_id}", dependencies=[Depends(login_required)])
def total_and_average_sales_by_store(
    store_id: str,
    start_date: date = Query(..., description="Start date of the period"),
    end_date: date = Query(..., description="End date of the period"),
    datamart: DatamartController = Depends(get_datamart_controller)
):
    sales_controller = SalesController(datamart)
    params = SalesQueryParams(start_date=start_date, end_date=end_date, key_value=store_id)
    data = sales_controller.get_sales_average_by_key_store(params)
    if data:
        return data
    return HTTPException(status_code=404, detail='Store not found')


@router.get("/total-and-average-sales/by-product/{product_id}", dependencies=[Depends(login_required)])
def total_and_average_sales_by_product(
    product_id: str,
    start_date: date = Query(..., description="Start date of the period"),
    end_date: date = Query(..., description="End date of the period"),
    datamart: DatamartController = Depends(get_datamart_controller)
):
    sales_controller = SalesController(datamart)
    params = SalesQueryParams(start_date=start_date, end_date=end_date, key_value=product_id)
    data = sales_controller.get_sales_average_by_key_product(params)
    if data:
        return data
    return HTTPException(status_code=404, detail='Product not found')


@router.get("/total-and-average-sales/by-employee/{employee_id}", dependencies=[Depends(login_required)])
def total_and_average_sales_by_employee(
    employee_id: str,
    start_date: date = Query(..., description="Start date of the period"),
    end_date: date = Query(..., description="End date of the period"),
    datamart: DatamartController = Depends(get_datamart_controller)
):
    sales_controller = SalesController(datamart)
    params = SalesQueryParams(start_date=start_date, end_date=end_date, key_value=employee_id)
    data = sales_controller.get_sales_average_by_key_employee(params)
    if data:
        return data
    return HTTPException(status_code=404, detail='Employee not found')
