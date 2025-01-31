from ..indexes.products import create_products_index
from ..connection import create_redis_connection

from redisearch import Query, Client

import random

class ProductService:
    def __init__(self):
        self.redis_connection = create_redis_connection()
        self.product_index = create_products_index(self.redis_connection)

    def create_product(self, product: dict):
        return self.product_index.add_document(self.generate_random_code(), **product)

    def search_product_by_description(self, description: str):
        query_string = f'@description:({description}*)'
        query = Query(query_string).verbatim()
        return self.product_index.search(query)

    def generate_random_code(self):
        return str(random.randint(100000, 999999))
