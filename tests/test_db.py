from dataclasses import asdict

from sqlalchemy import select

from app.models.models import Account


def test_create_account(session, mock_db_time):
    with mock_db_time(model=Account) as time:
        new_account = Account(
            username='Junin', password='secret', email='test@test'
        )
        session.add(new_account)
        session.commit()

    account = session.scalar(
        select(Account).where(Account.username == 'Junin')
    )

    assert asdict(account) == {
        'id': 1,
        'username': 'Junin',
        'password': 'secret',
        'email': 'test@test',
        'created_at': time,
        'updated_at': time,
    }
