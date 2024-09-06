from fastapi import FastAPI
from http import HTTPStatus
from duzero_fastapi.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Ola, mundo!'}
