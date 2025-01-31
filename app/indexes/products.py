from redisearch import Client, TextField

def create_products_index(connection):
    product_index = Client('products', conn=connection)

    try:
        product_index.info()
    except:
        product_index.create_index([
            TextField('description'),
            TextField('supplier')
        ])

    return product_index