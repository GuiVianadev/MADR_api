from http import HTTPStatus

from fastapi import APIRouter

from app.schemas.account_schema import AccountPublic, AccountSchema

router = APIRouter(prefix='/accounts', tags=['accounts'])


@router.post('/', status_code=HTTPStatus.CREATED, response_model=AccountPublic)
async def create_account(account: AccountSchema): ...
