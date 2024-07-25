from fastapi import FastAPI
import uvicorn

from app.routers.sales_router import router as sales_router
from app.routers.user import router as user_router


app = FastAPI()
app.include_router(sales_router)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
