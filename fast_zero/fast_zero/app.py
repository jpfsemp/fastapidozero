from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World!!!'}


@app.get('/404', status_code=HTTPStatus.NOT_FOUND, response_class=HTMLResponse)
def not_found():
    return """
    <html>
      <head>
        <title>404</title>
      </head>
      <body>
        <img src="https://httpstatusdogs.com/img/404.jpg" alt="404" />
      </body>
    </html>"""


@app.get('/home', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def home():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
