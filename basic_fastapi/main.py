from fastapi import FastAPI
from mockData import products

app = FastAPI()

@app.get("/")   #route
def home():  #normal fun
    return "Welcome to FastAPI Series !"

@app.get("/products")
def get_products():
    return products


#path params
app.get("/product/{product_id}")
def get_one_product(product_id):
    return[]
