from http import HTTPStatus

from fastapi.testclient import TestClient

from duzero_fastapi.app import app


def test_read_root_deve_retornar_OK_e_ola_mundo():
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Ola, mundo!'}
