from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.task import TaskBase, TaskCreate, TaskOut, TaskUpdate
from database import get_db
from core.security import get_current_user
from controller import task 

router = APIRouter()

@router.post("/", response_model=TaskOut)
def create(task: TaskCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return task.create_task(db, task, owner_id=current_user.id)

@router.get("/", response_model=list[TaskOut])
def read_all(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return task.get_tasks(db, owner_id=current_user.id)

@router.get("/{task_id}", response_model=TaskOut)
def read(task_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    db_task = task.get_task(db, task_id)
    if db_task is None or db_task.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.put("/{task_id}", response_model=TaskOut)
def update(task_id: int, updates: TaskUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    db_task = task.get_task(db, task_id)
    if db_task is None or db_task.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    return task.update_task(db, db_task, updates)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(task_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    db_task = task.get_task(db, task_id)
    if db_task is None or db_task.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    task.delete_task(db, db_task)
    return
    

