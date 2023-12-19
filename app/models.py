from pydantic import BaseModel
from typing import Optional,List
from uuid import UUID, uuid4
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    gender: Gender
    roles: List[Role]

class UpdateUser(BaseModel):

    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]

    #update user
# craete a model
# first last middle and roles optional
# create @app.put(path)
# if any of the feild not none then update the existing field with the new value
# path variables
