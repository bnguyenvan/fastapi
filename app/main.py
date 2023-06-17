from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello from root"}

@app.get("/posts/{id}")
def get_post(id: int):
    return {f"Here is post with id: {id}"}

@app.post("/posts")
def created_posts():
    return {"Hello, this is post function"}

@app.delete("/posts/{id}")
def delete_post(id: int):
    return {f"Deleted post with id: {id}"}

@app.put("/posts/{id}")
def update_post(id: int):
    return {f"Updated post with id: {id}"}
