from sqlalchemy import select, insert, delete
from sqlalchemy.orm import Session
from .models import Task
from .schemas import TaskCreate, TaskSchema


def get_tasks_list(db: Session) -> list[TaskSchema]:
    tasks = db.query(Task).all()
    return [TaskSchema(id=task.id, name=task.name, deadline=task.deadline) for task in tasks]


def get_task(db: Session, task_name: int):
    task = db.query(select(Task).filter(Task.name == task_name)).first()
    return task


def add_task(db:Session, task: TaskCreate):
    task = Task(name=task.name, deadline=task.deadline)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    db.delete(task)
    db.commit()
    return {'success': 'true'}
