from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.task import TaskCreate, TaskOut
from database import get_db
from core.security import get_current_user
from controller import task 

router = APIRouter()

@router.post("/", response_model=TaskOut)
def create(taskdata: TaskCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return task.create_tasks(db, taskdata, owner_id=current_user.id)

@router.get("/", response_model=list[TaskOut])
def read_all(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return task.get_tasks(db, owner_id=current_user.id)

