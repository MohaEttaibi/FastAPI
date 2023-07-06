from typing import List, Optional, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# from model import Item
# from api import (create_item, read_items, read_item_by_id,
#                  update_item, delete_item)

class Student(BaseModel):
    name:str
    age:int
    department:str

import mysql.connector
cnx = mysql.connector.connect(
    host='127.0.0.1', 
    port=3306,
    user='root',
    password='', 
    database='FastAPI'
)
cursor = cnx.cursor()

app = FastAPI()

# students = [
#     {"name":"Mohammed", "age":35, "department":"IT"},
#     {"name":"Khaled", "age":40, "department":"HR"}
# ]

@app.get('/')
def index():
    return {"Hello": "World"}

@app.get("/students")
def get_all_student():
    sql = "SELECT * FROM `students`"
    cursor.execute(sql)
    students = cursor.fetchall()
    return students

@app.get("/student/{id}")
def get_student_by_id(id:int):
    sql = "SELECT * FROM `students` WHERE id=%s"
    val = (id,)
    cursor.execute(sql,val)
    students = cursor.fetchall()
    if len(students) == 0:
        raise HTTPException(status_code=500, detail="Student Not Found")
    return students[0]


@app.delete("/student/{id}")
def delete_student_by_id(id:int):
    sql = "DELETE FROM `students` WHERE id=%s"
    val = (id,)
    cursor.execute(sql,val)
    cnx.commit()
    # students.pop(id)
    return {
        "message":"Deleted Successfully",
    }

@app.post("/student/create")
def add_new_student(student:Student):
    sql = "INSERT INTO `students`(`name`, `age`, `department`) VALUES (%s,%s,%s);"
    val = (student.name, student.age, student.department)
    cursor.execute(sql, val)
    cnx.commit()
    # students.append(student)
    return {
        "message":"Added Successfully"
    }


@app.post("/student/update")
def update_student(id:int, student:Student):
    # new_student = students[id]
    # new_student['name'] = name['name']
    # new_student['age'] = name['age']
    # new_student['department'] = name['department']
    # students[id] = new_student
    sql = "UPDATE `students` SET `name` = %s, `age` = %s, `department` = %s WHERE id = %s"
    val = (student.name, student.age, student.department, id)
    cursor.execute(sql, val)
    cnx.commit()
    return {
        "message":"Updated Successfully"
    }


# @app.get("/items", response_model=List[Item])
# async def get_all_items():
#     items = await read_items()
#     return items


# @app.get("/items/{item_id}", response_model=Item)
# async def get_item_by_id(item_id: str):
#     item = await read_item_by_id(item_id)
#     if item is None:
#         raise HTTPException(status_code=404, detail="item not found")
#     return item


# @app.post("/items", response_model=Item)
# async def create_new_item(item: Item):
#     new_item = await create_item(item)
#     return new_item


# @app.put("/items/{item_id}")
# async def update_existing_item(item_id: str,
#                                name: Optional[str] = None,
#                                description: Optional[str] = None,
#                                price: Optional[str] = None,
#                                is_offer: Optional[bool] = None):
#     updated_item = await update_item(item_id, name, description, price, is_offer)
#     if updated_item is None:
#         raise HTTPException(status_code=404, detail="Item Not Found")
#     return updated_item


# @app.delete("/items/{item_id}")
# async def delete_existing_item(item_id: str):
#     deleted_item = await delete_item(item_id)
#     if deleted_item is None:
#         raise HTTPException(status_code=404, detail="Item Not Found")
#     return {"message": "item deleted with success."}
