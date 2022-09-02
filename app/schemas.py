from typing import List, Optional, Union
from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    email: Optional[str] = None


# Properties to receive on user creation
class UserCreate(UserBase):
    password: str


# Properties shared by models stored in DB
class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class User(BaseModel):
    data: Union[List[UserInDBBase], UserInDBBase]


# Properties stored in DB
class UserInDB(UserInDBBase):
    is_active: bool
