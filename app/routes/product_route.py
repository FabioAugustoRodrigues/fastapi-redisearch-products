from fastapi import APIRouter

from ..schemas.product_schema import ProductRequest
from ..services.product_service import ProductService

import random

router = APIRouter()
product_service = ProductService()


@router.post("/", status_code=201)
async def create_product(product: ProductRequest):
    random_id = random.randint(1, 1000000)
    product_service.create_product(random_id, product.dict())

    product_dict = {
        "id": random_id,
        "description": product.description,
        "supplier": product.supplier
    }

    return product_dict

@router.get("/")
async def search_products(description: str):
    return product_service.search_product_by_description(description)