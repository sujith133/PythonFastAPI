from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

from fastapi import FastAPI

engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Todo(Base):  
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    todo = Column(String)
    is_done = Column(Boolean, default=False)


Base.metadata.create_all(engine)

app_fast = FastAPI()

@app_fast.get('/')
async def home():
    session = Session()
    todos = session.query(Todo).all()
    return {'todos': todos}

@app_fast.post("/create/")
async def create_todo(todo: str, is_done: bool = False):
    session = Session()
    new_todo = Todo(todo=todo, is_done=is_done)
    session.add(new_todo)
    session.commit()
    return {"todo added": new_todo.todo}

@app_fast.put("/update/{todo_id}")
async def update_todo(todo: str, is_done: bool = False):
    session = Session()
    existing_todo = session.query(Todo).filter(Todo.todo == todo).first()
    if existing_todo:
        existing_todo.todo = todo
        existing_todo.is_done = is_done
        session.commit()
        return {"message": "Todo updated successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")

@app_fast.delete("/delete/{todo_id}")
async def delete_todo(todo: str):
    session = Session()
    todo_to_delete = session.query(Todo).filter(Todo.todo == todo).first()
    if todo_to_delete:
        session.delete(todo_to_delete)
        session.commit()
        return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
