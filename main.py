from fastapi import FastAPI
from app.routes.product_route import router as product_route

app = FastAPI(
    title="FastAPI Redisearh Products",
    description="",
    version="0.1.0"
)

app.include_router(product_route, prefix="/products", tags=["Products"])