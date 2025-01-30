from fastapi import APIRouter

from ..schemas.product_schema import ProductRequest
from ..connection import create_redis_connection

router = APIRouter()
connection = create_redis_connection()


@router.post("/")
async def create_product(product: ProductRequest):
    return product