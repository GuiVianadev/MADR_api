from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_session
from app.models.models import Account
from app.schemas.account_schema import (
    AccountList,
    AccountPublic,
    AccountSchema,
)

router = APIRouter(prefix='/accounts', tags=['accounts'])


@router.post('/', status_code=HTTPStatus.CREATED, response_model=AccountPublic)
async def create_account(
    account: AccountSchema, session: Session = Depends(get_session)
):
    db_account = session.scalar(
        select(Account).where(
            (Account.username == account.username)
            | (Account.email == account.email)
        )
    )
    if db_account:
        if db_account.username == account.username:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail='Username already exists',
            )
        elif db_account.email == account.email:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail='Email already exists',
            )

    db_account = Account(
        username=account.username,
        password=account.password,
        email=account.email,
    )
    session.add(db_account)
    session.commit()
    session.refresh(db_account)

    return db_account


@router.get('/', response_model=AccountList)
def read_accounts(
    session: Session = Depends(get_session),
    limit: int = 10,
    skip: int = 0,
):
    account = session.scalars(select(Account).limit(limit).offset(skip))
    return {'accounts': account}
