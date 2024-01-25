from typing import Union

from fastapi import FastAPI
import redis
import debugpy

debugpy.listen({"0.0.0.0",5678})

app = FastAPI()

r = redis.Redis(host='redis', port=6379, db=0)

@app.get("/")
def read_root():
    return {"Hello": "World!!!!asdfas"}

@app.get("/hits")
def read_root():
    r.incr('hits')
    return {"hits": r.get('hits')}
    

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}