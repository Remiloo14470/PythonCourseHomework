from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models.task import Task
from app.models.user import User
from app.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify


router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks(get_db: Annotated[Session, Depends(get_db)]):
    tasks = get_db.scalars(select(Task)).all()
    return tasks


@router.get("/task_id")
async def task_by_id(get_db: Annotated[Session, Depends(get_db)], task_id: int):
    task = get_db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return task


@router.post("/create")
async def create_task(get_db: Annotated[Session, Depends(get_db)], user_id: int, create_task: CreateTask):
    user = get_db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    get_db.execute(insert(Task).values(title=create_task.title,
                                       content=create_task.content,
                                       priority=create_task.priority,
                                       user_id=user_id,
                                       slug=slugify(create_task.title)))
    get_db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put("/update")
async def update_task(get_db: Annotated[Session, Depends(get_db)], task_id: int, update_task: UpdateTask):
    task = get_db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    get_db.execute(update(Task).where(Task.id == task_id).values(title=update_task.title,
                                                                 content=update_task.content,
                                                                 priority=update_task.priority,
                                                                 slug=slugify(update_task.title)))
    get_db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task updated successfully'
    }


@router.delete("/delete")
async def delete_task(get_db: Annotated[Session, Depends(get_db)], task_id: int):
    task = get_db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    get_db.execute(delete(Task).where(Task.id == task_id))
    get_db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task deleted successfully'
    }

