from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)
    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (afirmação)
    assert response.json() == {'message': 'Hello World!!!'}


def test_read_root_deve_retornar_ok_e_texto_html_ola_mundo():
    client = TestClient(app)  # Arrange (organização)
    response = client.get('/home')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (afirmação)
    assert '<h1> Olá Mundo </h1>' in response.text # Assert (afirmação)
