import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from intermediate_certification_3.server.db import SessionLocal, engine
from intermediate_certification_3.server import models, crud, schemas

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
    print(f'hera ', type(task))
    if task['success'] == 'true':
        return {'success': 'true'}
    else:
        return 'Ошибка'


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)