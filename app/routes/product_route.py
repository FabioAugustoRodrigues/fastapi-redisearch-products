from fastapi import APIRouter

from ..schemas.product_schema import ProductRequest
from ..indexes.products import create_products_index

from ..connection import create_redis_connection

router = APIRouter()
redis_connection = create_redis_connection()
product_index = create_products_index(redis_connection)


@router.post("/")
async def create_product(product: ProductRequest):
    return product