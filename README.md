# FastAPI RediSearch Products
This project is designed to generate thousands of fake products, store them in a CSV file, and later index them using RediSearch for efficient searching. 
Additionally, a FastAPI-based API is provided to manually register products in RediSearch and search for products by description.

## How it works
#### 1. Generating Fake Products
- The script creates thousands of fake product entries.
- These entries are stored in a CSV file for later indexing.

#### 2. Indexing in RediSearch
- The generated products can be indexed in RediSearch for fast retrieval.
- A FastAPI endpoint allows manual addition of products to RediSearch.

#### 3. Searching for Products
- The FastAPI application provides an endpoint to search for products by description.
- RediSearch enables efficient full-text search over the indexed products.

## How to run the project
#### 1. Build the Docker Image
First, navigate to the root directory of the project where the docker-compose.yaml file is located.
Then, build and start the container using the following command:
```bash
docker-compose up --build
```
This will build the image and start the API application inside a container.

#### 2. Access the API
Once the container is running, the API application will be available at:
```bash
http://localhost:8400/docs
```

## Generate indexed products
#### 1. Activate the virtual environment:
```bash
source .venv/bin/activate
```

#### 2. Generating Fake Products
```bash
python -m app.utils.generate_fake_products
```

#### 3. Indexing in RediSearch
```bash
python -m app.utils.generate_indexed_products
```
