from fastapi import FastAPI, HTTPException

from database import (fetch_one_todo, fetch_all_todos,
                      create_todo, update_todo, remove_todo)
from model import Todo

# App object
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ['http://localhost:3000']

# what is a middleware? 
# software that acts as a bridge between an operating system or database and applications, especially on a network.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# home page


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response


@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title):
    response = fetch_one_todo(title)
    if response:
        return response
    # return Page not found
    raise HTTPException(404, f"No TODO with {title}" )


@app.post("/api/todo", response_model=Todo)
async def post_todo(todo:Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    # 400: bad request
    raise HTTPException(400, "Something went wrong")


@app.put("/api/todo/{title}/", response_model=Todo)
async def put_todo(title:str, desc:str):
    response = await update_todo(title, desc)
    if response:
        return response
    # return Page not found
    raise HTTPException(404, f"No TODO with f{title}" )

@app.delete("/api/todo/{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted item"
    # return Page not found
    raise HTTPException(404, f"No TODO with f{title}" )

