from fastapi import FastAPI, Request
#from fastapi.responses import HTMLResponse since we are using templates 
from fastapi.templating import JinjaTemplates 


app = FastAPI()

templates = JinjaTemplates(directory="templates") #tells the app to look the templates directory for templates rendering. 

posts: list[dict] = [
    {
    "id": 1,
    "author": "COrey Schafer",
    "title": "FastAPI is Awesome",
    "content": "THis framework is really easy to use and super fast",
    "date_posted": "April 20, 2025",
    },
    {
    "id": 2,
    "author": "Joe Mark",
    "title": "Django Web framework is Awesome",
    "content": "Helps to build and ship fullstack applications on the fly",
    "date_posted": "April 20, 2025",
    },
    {
    "id": 3,
    "author": "karima shata",
    "title": "PhP Web framework is amazing!",
    "content": "Helps to build and ship fullstack applications on the fly",
    "date_posted": "April 20, 2025",
    },
]


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"

@app.get("/api/posts")
def get_posts():
    return posts