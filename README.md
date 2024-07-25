# Celes technical test
This project is a system that requires the configuration of a virtual environment, specific environment variables, and includes documentation on endpoints, tests, and running with Docker.

## Prerequisites
* [Python 3.12]

## Installation

**1. Create the virtual environment
To create a virtual environment, follow these steps:**

```bash
python3.12 -m venv venv
source venv/bin/activate  # On Linux/MacOS
venv\Scripts\activate  # On Windows
```
**2. Install dependencies
With the virtual environment activated, install the project dependencies:**

```bash
Copiar código
pip install -r requirements.txt
```
**3. Configure environment variables
You need to configure the following environment variables:**

DATA_DIRECTORY: Directory where the data files are located.

SECRET_KEY: Secret key for generating the token.

You can configure these environment variables in your system or create a .env file in the root of the project with the following content:

```
.env
Copiar código
DATA_DIRECTORY=path/to/data
SECRET_KEY=your_secret_key
```

## 4. Documented Endpoints

Below is a list of available endpoints in the system:

**Endpoint 1:**
GET /sales/by-product/{product_id}

Method: **GET**

Description: This endpoint retrieves the total sales for a specific product within a given date range.

Query Parameters
* start_date: The start date for the sales period (format: YYYY-MM-DD).
* end_date: The end date for the sales period (format: YYYY-MM-DD).

**Request Example**

```GET http://127.0.0.1:8000/sales/by-product/1/44733?start_date=2022-11-01&end_date=2024-01-31```

**Headers**

_Authorization: Bearer <token>_

**Response**

```{
    "total_sales": 4,
    "name": "BICARBONATO DE AMONIO (SCO X 25 KLS)",
    "start_date": "2022-11-01",
    "end_date": "2024-01-31"
}
```

### **Response Fields**

total_sales: The total number of sales for the specified product within the given date range.
name: The name of the product.
start_date: The start date of the queried sales period.
end_date: The end date of the queried sales period.


**Endpoint 2:**
GET /sales/by-employee/{employee_id}

Method: **GET**

Description: This endpoint retrieves the total sales for a specific employee within a given date range.

Query Parameters
* start_date: The start date for the sales period (format: YYYY-MM-DD).
* end_date: The end date for the sales period (format: YYYY-MM-DD).

**Request Example**

```GET http://127.0.0.1:8000/sales/by-employee/1|569?start_date=2023-11-01&end_date=2024-01-31```

**Headers**

_Authorization: Bearer <token>_

**Response**

```{
    "total_sales": 10,
    "name": "Diego fernando",
    "start_date": "2022-11-01",
    "end_date": "2024-01-31"
}
```

### **Response Fields**

total_sales: The total number of sales for the specified product within the given date range.
name: The name of the product.
start_date: The start date of the queried sales period.
end_date: The end date of the queried sales period.

**Endpoint 3:**
GET /sales/by-store/{store_id}

Method: **GET**

Description: This endpoint retrieves the total sales for a specific store within a given date range.

Query Parameters
* start_date: The start date for the sales period (format: YYYY-MM-DD).
* end_date: The end date for the sales period (format: YYYY-MM-DD).

**Request Example**

```GET http://127.0.0.1:8000/sales/by-store/1|023?start_date=2023-11-15&end_date=2024-01-31```

**Headers**

_Authorization: Bearer <token>_

**Response**

```{
    "total_sales": 40,
    "name": "Unicentro",
    "start_date": "2022-11-01",
    "end_date": "2024-01-31"
}
```

### **Response Fields**

total_sales: The total number of sales for the specified product within the given date range.
name: The name of the product.
start_date: The start date of the queried sales period.
end_date: The end date of the queried sales period.


**Endpoint 4:**
GET /sales/total-and-average-sales/by-store/{store_id}

Method: **GET**

Description: This endpoint retrieves the total and average sales for a specific employee within a given date range.

Query Parameters
* start_date: The start date for the sales period (format: YYYY-MM-DD).
* end_date: The end date for the sales period (format: YYYY-MM-DD).

**Request Example**

```GET http://127.0.0.1:8000/total-and-average-sales/by-store/1|023?start_date=2022-11-01&end_date=2024-01-31```

**Headers**

_Authorization: Bearer <token>_

**Response**

```{
    "total_sales": 10,
    "name": "Unilago",
    "start_date": "2022-11-01",
    "end_date": "2024-01-31"
}
```

### **Response Fields**

total: The total of sales for the specified product within the given date range.
average: The average of sales
name: The name of the product.
start_date: The start date of the queried sales period.
end_date: The end date of the queried sales period.

**Endpoint 5:**
GET /sales/total-and-average-sales/by-product/{product_id}

Method: **GET**

Description: This endpoint retrieves the total and average sales for a specific employee within a given date range.

Query Parameters
* start_date: The start date for the sales period (format: YYYY-MM-DD).
* end_date: The end date for the sales period (format: YYYY-MM-DD).

**Request Example**

```GET http://127.0.0.1:8000/total-and-average-sales/by-product/1|44733?start_date=2022-11-01&end_date=2024-01-31```

**Headers**

_Authorization: Bearer <token>_

**Response**

```{
    "total_sales": 10,
    "name": "Bicarbonato",
    "start_date": "2022-11-01",
    "end_date": "2024-01-31"
}
```

### **Response Fields**

total: The total of sales for the specified product within the given date range.
average: The average of sales
name: The name of the product.
start_date: The start date of the queried sales period.
end_date: The end date of the queried sales period.

**Endpoint 6:**
GET /sales/total-and-average-sales/by-employee/{employee_id}

Method: **GET**

Description: This endpoint retrieves the total and average sales for a specific employee within a given date range.

Query Parameters
* start_date: The start date for the sales period (format: YYYY-MM-DD).
* end_date: The end date for the sales period (format: YYYY-MM-DD).

**Request Example**

```GET http://127.0.0.1:8000/total-and-average-sales/by-store/1|023?start_date=2022-11-01&end_date=2024-01-31```

**Headers**

_Authorization: Bearer <token>_

**Response**

```{
    "total_sales": 10,
    "name": "Diego fernando",
    "start_date": "2022-11-01",
    "end_date": "2024-01-31"
}
```

### **Response Fields**

total: The total of sales for the specified product within the given date range.
average: The average of sales
name: The name of the product.
start_date: The start date of the queried sales period.
end_date: The end date of the queried sales period.

**Endpoint 7:**
GET /login

Method: **post**

Description: This endpoint generate login and gives token.

form-data body
* username
* password

**Request Example**

```GET http://127.0.0.1:8000/login```


**Response**

```
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1pbGxlcjk0IiwiZXhwIjoxNzIxOTUzNDAwLjM2MDMzNX0.s82_AKZAZGs5Qcqxl2qLHDo133YHM8U8CRdNllmIOh0",
    "token_type": "bearer"
}
```



**5. Run tests**
To run the tests, ensure the virtual environment is activated and execute:

```bash

pytest
```
**6. Run with Docker
To run the project using Docker, follow these steps:**

Build the Docker image:
```

docker build -t prueba-tecnica-celes .

```

**Run the Docker container:**

```
docker run -d -p 8000:8000 --env-file .env prueba-tecnica-celes
```
Suggestions
Make sure to keep dependencies in the requirements.txt file updated.
Consider adding additional tests for the sales controllers to ensure their proper functionality.



