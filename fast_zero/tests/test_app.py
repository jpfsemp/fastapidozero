from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    # client = TestClient(app)  # Arrange (organização)
    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (afirmação)
    assert response.json() == {'message': 'Hello World!!!'}


def test_html_404(client):
    response = client.get('/404')
    message = '<img src="https://httpstatusdogs.com/img/404.jpg" alt="404" />'

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert message in response.text


def test_read_root_deve_retornar_ok_e_texto_html_ola_mundo(client):
    # client = TestClient(app)  # Arrange (organização)
    response = client.get('/home')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (afirmação)
    assert '<h1> Olá Mundo </h1>' in response.text  # Assert (afirmação)


def test_create_user(client):
    # client = TestClient(app)  # Arrange (organização)
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email': 'test@test.com',
            'password': '12354',
        },
    )  # Act (ação)

    # Voltou o status code correto?
    assert response.status_code == HTTPStatus.CREATED  # Assert (afirmação)

    # Validar UserPublic
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'email': 'test@test.com',
                'id': 1,
            }
        ]
    }


def test_read_user_by_id(client):
    response = client.get('/user/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_get_user_by_id_not_found(client):
    response = client.get('/user/555')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'testusername2',
            'email': 'test@test2.com',
            'id': 1,
            'password': '1234',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testusername2',
        'email': 'test@test2.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/555',
        json={
            'username': 'testusername2',
            'email': 'test@test2.com',
            'password': '4567',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('/users/555')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
