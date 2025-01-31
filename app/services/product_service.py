from ..indexes.products import create_products_index
from ..connection import create_redis_connection

import random

class ProductService:
    def __init__(self):
        self.redis_connection = create_redis_connection()
        self.product_index = create_products_index(self.redis_connection)

    def create_product(self, product: dict):
        return self.product_index.add_document(self.generateRandomCode(), **product)

    def generateRandomCode(self):
        return random.randint(100000, 999999)