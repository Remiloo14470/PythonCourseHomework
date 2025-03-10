from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def welcome_func() -> dict:
    return {"message": "Welcome to Main Page!"}


@app.get("/user/admin")
async def admin_func() -> dict:
    return {"message": "Вы вошли как администратор!"}


@app.get("/user/{username}/{age}")
async def user_info(username: Annotated[str, Path(max_length=20, min_length=5, description='Enter your username', examples='Remi')],
                    age: int = Path(ge=18, le=120, description='Enter your age', examples='23')) -> dict:
    return {"message": f"Информация о пользователе: Имя: {username}, Возраст {age}"}


@app.get("/user/{user_id}")
async def user_id(user_id: int = Path(le=100, ge=0, description='Enter your User ID', examples='1')) -> dict:
    return {"message": f"Вы вошли как пользователь№: {user_id}"}


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8099)
