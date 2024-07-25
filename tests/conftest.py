from unittest.mock import patch

import pandas
import pytest

from app.controllers.datamart import DatamartController


@pytest.fixture
def data_fixture():
    data = pandas.read_json('tests/mocks/datamart/employee.json')
    data['KeyDate'] = pandas.to_datetime(data['KeyDate'] * 1000000).dt.date
    return data
