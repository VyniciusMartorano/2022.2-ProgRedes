# pip install fastapi
# https://fastapi.tiangolo.com/
# pip install uvicorn
from fastapi import FastAPI

myapi = FastAPI()

@myapi.get('/')
def root():
    return 'Ola Mundo Cruel!!!!'

@myapi.get("/ifrn")
def root():
    return {"message": "IFRN"}

@myapi.get('/redes')
def root():
    return 'Curso Superior de Redes...'

@myapi.get('/cnat')
def root():
    return 'Campus Natal-Central'