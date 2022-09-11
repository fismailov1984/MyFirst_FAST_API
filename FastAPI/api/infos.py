from fastapi import APIRouter, status, HTTPException, Depends
from .schemas import InfoSchemaIn, InfoSchema, UserSchema, InfoSchemaInPut, InfoSchemaPut, InfoSchemaInGetBalanse
from .db import Info, database
from typing import List
from .Token import get_current_user

router = APIRouter(
    tags=["Client"]
)


@router.get('/infos', response_model=List[InfoSchema])
async def get_infos(current_user: UserSchema = Depends(get_current_user)):
    query = Info.select()
    return await database.fetch_all(query=query)


@router.post('/infos/', status_code=status.HTTP_201_CREATED, response_model=InfoSchema)
async def insert_info(info: InfoSchemaIn, current_user: UserSchema = Depends(get_current_user)):
    query = Info.insert().values(user_name=info.user_name,
                                    wallet_number=info.wallet_number,
                                    nickname=info.nickname,
                                    balance=info.balance)
    last_record_id = await database.execute(query)
    return {**info.dict(), "id": last_record_id}


@router.get('/infos/{nickname}/', response_model=InfoSchemaPut)
async def get_details(nickname: str, current_user: UserSchema = Depends(get_current_user)):
    query = Info.select().where(nickname == Info.c.nickname)
    myinfo = await database.fetch_one(query=query)

    if not myinfo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Info not found")

    return {**myinfo}


@router.put('/infos/{user_name}/', response_model=InfoSchemaInPut)
async def update_info(nickname: str, info: InfoSchemaInPut, current_user: UserSchema = Depends(get_current_user)):
    query = Info.select().where(Info.c.nickname == nickname)
    myinfo = await database.fetch_one(query=query)
    query = Info.update().where(Info.c.nickname == nickname).values(balance=(info.balance + myinfo.balance))
    await database.execute(query)
    return {**info.dict(), "nickname": nickname}


@router.delete('/infos/{nickname}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_info(nickname: str, current_user: UserSchema = Depends(get_current_user)):
    query = Info.delete().where(Info.c.nickname == nickname)
    await database.execute(query)
    return {"message": "Info deleted"}


