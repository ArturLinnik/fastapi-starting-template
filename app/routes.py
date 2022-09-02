from fastapi import APIRouter, Depends, status
from fastapi.responses import Response
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from . import crud, schemas
from .database import get_db

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=schemas.User)
async def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    data = jsonable_encoder(users)
    print(data)
    return {"data": data}


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    db_user = crud.get_user_by_email(db=db, email=user.email)

    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists"
        )

    new_user = crud.create_user(db=db, user=user)
    data = jsonable_encoder(new_user)
    return {"data": data}


@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user(db=db, user_id=user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
