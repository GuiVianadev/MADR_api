from fastapi import FastAPI

from app.api.endpoints import accounts, authors, books

app = FastAPI()
app.include_router(accounts.router)
app.include_router(books.router)
app.include_router(authors.router)


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}
