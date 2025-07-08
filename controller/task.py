# crud/task.py
from sqlalchemy.orm import Session
from models.task import TaskModel
from schemas.task import TaskCreate, TaskUpdate

def create_tasks(db: Session, task: TaskCreate, owner_id: int):
    db_task = TaskModel(**task.dict(), owner_id=owner_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int):
    return db.query(TaskModel).filter(TaskModel.id == task_id).first()

def get_tasks(db: Session, owner_id: int):
    return db.query(TaskModel).filter(TaskModel.owner_id == owner_id).all()

def update_task(db: Session, db_task: TaskModel, updates: TaskUpdate):
    update_data = updates.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, db_task: TaskModel):
    db.delete(db_task)
    db.commit()
