from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi import Body
from pydantic import BaseModel
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

while True:
    try:
        conn = psycopg2.connect(
            host='172.17.0.3', 
            database='fastapi', 
            user='postgres', 
            password='%VC#c4NXK9eFg6', 
            port='5432')
        cursor = conn.cursor()
        print("Database conneciton was successful!")
        break
    except Exception as error:
        print("Connecting to database failed!")
        print("Error: ", error)
        time.sleep(2)

@app.get("/")
def read_root():
    return {"Hello from root"}

@app.get("/posts/{id}")
def get_post(id: int):
    return {f"Here is post with id: {id}"}

@app.post("/posts")
def created_posts(post: Post):
    return {"Hello, this is post function"}

@app.delete("/posts/{id}")
def delete_post(id: int):
    return {f"Deleted post with id: {id}"}

@app.put("/posts/{id}")
def update_post(id: int):
    return {f"Updated post with id: {id}"}
