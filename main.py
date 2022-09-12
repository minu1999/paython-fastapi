from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app =FastAPI()

class Item(BaseModel): #serilizer
    firstname:int
    lastname:str
    conatc:str
    drivers_license_number:int
    region:bool
    
#code changes to the marte branch to  from new branch     

@app.get('/')
def index():
    return{"message": "Hello World"}

@app.get('/great/{name}')
def great_name(name:str):
    return {"greeting":f"Hello {name}"}


@app.get('/greet')
def greet_Optional_name(name:Optional[str]='user'):
    return {"message":f"Hello {name}"}


@app.put('/item/{item_id}')
def update_item(item_id:int,item:Item):
    return {'name': item.name,
            'description':item.description,
            'price':item.price,
            'on_offer':item.on_offer
            }
