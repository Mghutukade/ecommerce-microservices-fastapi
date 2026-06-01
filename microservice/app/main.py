from fastapi import FastAPI
from redis_om import get_redis_connection 

app = FastAPI()

redis = get_redis_connection(
    host="horse-color-cook-49943.db.redis.io",
    port=14005,
    password="F9eo0tCdGNhYYvjPUb1deZjafliCsMJJ",
    decode_responses=True 
)


class Product():
    name = str
    price = float
    quantity = int 
    
    class Meta:
        database=redis 
    
@app.get('/prodcuts')
def all():
    return []

