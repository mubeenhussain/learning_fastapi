from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1:{
        "name":"Mubeen Hussain",
        "age":12,
        "year":"12"
    },
    2:{
        "name":"Jalal Hussain",
        "age":12,
        "year":"12"
    },
    3:{
        "name":"Nabeel Hussain",
        "age":12,
        "year":"12"
    },
}

class Student(BaseModel):
    name:str
    age:str
    year:str      

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None
    

@app.get("/")
def index():
    return {
        "name":"First data"
    }
    

# @app.get("/get-student/{student_id}")
# def get_student(student_id:int):
#     print(student_id)
#     return students[student_id]

@app.get("/get-student/{student_id}")
def get_student(student_id:int = Path(..., description="The id of student you want to view",gt=0)):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student_by_name(*,student_id: int, name:Optional[str] = None, test: int):
    for student in students:
        if students[student]['name'] == name:
            return students[student]
    return {
        "Data":"Not found"
    }
    
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {
            "Error": "Student Exists"
        }
    
    students[student_id] = student
    return students[student_id]

@app.put('/update-student/{student_id}')
def update_student(student_id: int, student:UpdateStudent):
    if student_id not in students:
        return {
            "Error":"Student doesnot exist"
        }
    if student.name != None:
        students[student] = student.name
    if student.age != None:
        students[student] = student.age
    if student.year != None:
        students[student] = student.year   
        
    students[student_id] = student
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error":"Student doesnot exist"}

    del students[student_id]
    return {
        "message":
            "student deleted successfully"
    }