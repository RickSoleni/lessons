from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()


@app.get('/items/{item_id}')
async def get_items(item_id: int):
    soma = item_id * 10
    return soma


@app.put('/')
async def pentakill():
    return 'pentakill'


class Lists(BaseModel):
    lista: list


@app.delete('/array/deleterandom')
async def delete_random(lista: Lists):
    """This endpoint receives an list, and then returns it without a random value that was inside it."""
    random.shuffle(lista)
    lista.pop()
    return lista
