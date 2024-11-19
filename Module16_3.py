from fastapi import FastAPI
from fastapi import Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, Возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def add_user_func(username: Annotated[str,Path(max_length=15, min_length=3, description='Enter you username', example='Remiloo')],
                        age: int = Path(ge=0, le=100, description='Enter your age', example='23')) -> str:
    user_id = str(int(max(users, key=int))+1)
    users[user_id] = f'Имя: {username}, Возраст {age}'
    return f"Пользователь: {user_id} зарегистрирован"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user_info(user_id: str, username: str, age:int) -> str:
    users[user_id] = f"Имя: {username}, Возраст {age}"
    return f"Пользователь {user_id} обновлен"


@app.delete("/user/{user_id}")
async def delete_user(user_id) -> str:
    users.pop(user_id)
    return f"Пользователь {user_id} удлен"


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8099)