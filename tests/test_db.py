from sqlalchemy import select

from app.models.models import Account


def test_create_account(session):
    new_account = Account(
        username='Junin', password='secret', email='test@test'
    )
    session.add(new_account)
    session.commit()

    account = session.scalar(
        select(Account).where(Account.username == 'Junin')
    )

    assert account.username == 'Junin'
