from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection 
from redis_om import HashModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)


redis = get_redis_connection(
    host="horse-color-cook-49943.db.redis.io",
    port=14005,
    password="F9eo0tCdGNhYYvjPUb1deZjafliCsMJJ",
    decode_responses=True
)


class Product(HashModel, index=True):
    name : str
    price : float
    quantity : int 
    
    class Meta:
        database=redis 
    
@app.get("/")
def home():
    return {"message": "Ecommerce Microservice Running"}

@app.get("/products")
def all():
    return Product.all_pks()

@app.post("/products")
def create(product: Product):
    pk = product.save()
    return {"pk": pk}

@app.get("/test")
def test():
    return {"ping": redis.ping()}

@app.delete("/products/{pk}")
def delete(pk: str):
    product = Product.get(pk)
    if not product:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Product not found")
        
    # Delete the specific instance, not the whole class
    product.delete() 
    return {"message": f"Product {pk} deleted successfully"}
