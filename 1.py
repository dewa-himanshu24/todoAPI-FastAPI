from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Custom(BaseModel):
  name: str
  age: int

@app.get("/ping")
async def ping():
  return {"message": "Hello World!!!"}

@app.get("/")
async def root():
  return {"message": "Welcome"}

@app.get("/blogs/comments")
async def read_blog_comment(q: str = None, name: str = ""):
  print(q, name)
  return {"message": "No comments yet!"}
  
@app.get("/blogs/{blog_id}")
async def read_blog(blog_id: int):
  return {"blog_id": blog_id}

@app.post("/blogs")
async def create_blog(request_body: Custom):
  print("request_body", request_body)
  return request_body