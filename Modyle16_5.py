from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Annotated
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="Templates")

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int = None


@app.get("/")
async def main(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}")
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id-1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.post("/user/{username}/{age}")
async def add_user_func(username: Annotated[str, Path(max_length=15, min_length=3, description='Enter you username', example='Remiloo')],
                        age: int = Path(ge=0, le=100, description='Enter your age', example='23')) -> User:
    user_id = max(users, key=lambda x: int(x.id)).id + 1 if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user_info(user_id: int, username: str, age: int) -> User:
    try:
        for user in users:
            if user_id == user.id:
                user_updated = User(id=user_id, username=username,age=age)
                return user_updated
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> User:
    try:
        for user in users:
            if user_id == user.id:
                users.remove(user)
                return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8099)