from fastapi import FastAPI,HTTPException
from typing import List
from uuid import UUID, uuid4
from app.models import User, Gender, Role, UpdateUser

app = FastAPI()
db: List[User] = [
    User(
        id = uuid4(),
        first_name  = "John",
        last_name = "Doe",
        gender = Gender.female,
        roles = [Role.student]
    ),
    User(
        id = uuid4(),
        first_name  = " kane",
        last_name = " bow",
        gender = Gender.male,
        roles = [Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/api/v1/users")
async def fetch_users():
    return db
@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:  # loop through users in db
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted successfully"}
    raise HTTPException(
        status_code=404,
        detail="User not found")

@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, update_user: UpdateUser):
    for user in db:  # loop through users in db
        if user.id == user_id:
            user.first_name = update_user.first_name or user.first_name
            user.last_name = update_user.last_name or user.last_name
            user.middle_name = update_user.middle_name or user.middle_name
            user.roles = update_user.roles or user.roles
        return {"message": "User updated successfully"}
    raise HTTPException(
        status_code=404,
        detail="User not found")


# # @app.get("/items/{item_id}")
# # def read_item(item_id: int, q: Union[str, None] = None):
# #     return {"item_id": item_id, "q": q}
# @app.get("users/me")
# def me():
#     return{"user_id": "the current user"}
# @app.get("users/{user_id}")
# def read_user(user_id: str):
#     return {"user_id": user_id}
# ---------------------------
# from enum import Enum

# from fastapi import FastAPI


# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"


# app = FastAPI()


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

    #     return {"model_name": model_name, "message": "Have some residuals"}
# ---------------------------
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}

# from fastapi import FastAPI

# app = FastAPI()

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]
# ---------------------------
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item

# from fastapi import FastAPI
# from pydantic import BaseModel


# class Item(BaseModel):
#     name: str
#     description: str or None = None
#     price: float
#     tax: float or None = None


# app = FastAPI()
# # @app.get("/items/")
# # async def read_items():
# #     return {"message": "This is a GET endpoint for items."}

# @app.post("/items/")
# async def create_item(item: Item):
#     item.name = item.name.capitalize()
#     item.description = item.description or "This is a description"
#     return item
