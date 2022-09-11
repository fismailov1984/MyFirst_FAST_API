
from fastapi import FastAPI
from .db import metadata, database, engine
from . import infos, users, auth


metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(infos.router)
app.include_router(users.router)
app.include_router(auth.router)




