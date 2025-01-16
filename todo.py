from fastapi import FastAPI
from sqlalchemy.orm import DeclarativeBase, Session, mapped_column, Mapped
from sqlalchemy import create_engine
from sqlalchemy.types import String, Integer, DateTime, Boolean
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Default table class
class Base(DeclarativeBase): 
    pass

# ORM Table class
class Tasks(Base):
    __tablename__ = 'Notes'

    id: Mapped[Integer] = mapped_column(Integer, autoincrement=True, primary_key=True)
    title: Mapped[String] = mapped_column(String, default='Title..')
    content: Mapped[String] = mapped_column(String, default='')
    completed: Mapped[Boolean] = mapped_column(Boolean, default=False)
    date: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())


# Pydantic validation class
class Task(BaseModel):
    title: str
    content: str
    completed: Optional[bool] = False


# Create API app
app = FastAPI()

# Create engine & table
engine = create_engine(url='sqlite:///base.db')
Base.metadata.create_all(engine)


@app.get('/get_tasks')
async def get_tasks():
    tasks = Session(engine).query(Tasks).all()
    return {"tasks": tasks}


@app.post('/create_task')
async def create_task(task: Task):
    with Session(engine) as db:
        obj = Tasks(title=task.title, content=task.content)
        db.add(obj)
        db.commit()
        return {'details': 'Successfully!'}


@app.put('/update_task/{task_id}')
async def update_task(task_id: str, new: Task):
    with Session(engine) as db:
        task = db.query(Tasks).filter(Tasks.id == task_id).first()
        if task:
            task.title = new.title
            task.content = new.content
            if new.completed:
                task.completed = new.completed
            db.commit()
            return {"details": "Successfully!"}


@app.delete('/delete_task/{task_id}')
async def delete_task(task_id: int): 
    with Session(engine) as db:
        task = db.query(Tasks).filter(Tasks.id == task_id).first()
        db.delete(task)
        db.commit()
        return {'details': "Successfully!"}

# uvicorn todo:app --reload