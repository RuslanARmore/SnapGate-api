
from typing import Optional
from fastapi import Body, FastAPI, status, HTTPException
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "Luchshie plyazi floridi", "content": "Konchenniy content", "id": 1}, {"title": "title", "content": "content2", "id": 2}]
@app.get("/") 
def read_root():
    return {"Hello": "okey"}

@app.get("/summary")
def get_summaries():
    return {"summary": my_posts}

@app.post("/createSummary", status_code=status.HTTP_201_CREATED)
def create_summary(new_post: Post):
    post_dic = new_post.model_dump()
    post_dic['id'] = randrange(0, 1000000)
    print(post_dic)
    my_posts.append(post_dic)
    return {"data": post_dic}

    
@app.get("/posts/{id}")
def get_post(id: int): 
    post = findPost(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with {id} not found")

    return post

def findPost(id):
    for post in my_posts:
        if post["id"] == id:
            return post