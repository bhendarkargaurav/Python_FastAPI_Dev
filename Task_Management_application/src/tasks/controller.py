from fastapi import APIRouter, Depends
from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from src.utils.db import get_db

def create_task(body: TaskSchema, db: Session):
    data = body.model_dump()

    new_task = TaskModel(
        title=data["title"],
        desciption=data["desciption"],
        is_completed=data["is_completed"]
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "status": "Task Created Successfully..",
        "data": new_task
    }


def get_tasks(db:Session):
    tasks = db.query(TaskModel).all()
    return {"status": "All Task", "data": tasks}