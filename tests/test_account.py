from http import HTTPStatus


def test_create_account(client):
    response = client.post(
        '/accounts',
        json={
            'username': 'testeusername',
            'email': 'testeu@sername.com',
            'password': 'testpassword',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'testeu@sername.com',
        'username': 'testeusername',
    }


def test_get_accounts(client):
    response = client.get('/accounts')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'accounts': []}
