from fastapi import FastAPI
from models import Todo

app=FastAPI()



todos=[]

@app.get("/todos")
async def get_todos():
    return "hello" , todos

#get all todos
#get single todo
@app.get("/todos/{todo_id}")
async def single_todo(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
          return {"todo":todo}
    return {"Message":"Todo not found"}
#create todo
@app.post("/todos")
async def create_todo(todo:Todo):
    todos.append(todo)
    return {"Message":"Todo Added"}
#update todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id:int,todo_obj:Todo):
    for todo in todos:
        if todo.id==todo_id:
            todo.id= todo_id
            todo.item= todo_obj.item
            return {"todo":todo}
    return {"Message":"Todo not found to update"}
#delete todo

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            todos.remove(todo)
            return {"Message":"Todo Deleted"}
    return {"Message":"Todo not found"}