from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .db import SessionLocal, engine
from . import models, crud, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/tasks/')
def get_tasks_list(db: Session = Depends(get_db)):
    return crud.get_tasks_list(db=db)


@app.post("/tasks/")
def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.add_task(db=db, task=task)


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db=db, task_id=task_id)
    if task.success == 'true':
        return {'success': 'true'}
    else:
        return 'Ошибка'
