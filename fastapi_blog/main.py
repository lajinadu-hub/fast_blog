from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader
# Environment is the core Jinja2 object that manages templates.
#FileSystemLoader tells Jinja2 where your HTML template files live on disk.

app = FastAPI()

templates = Environment(loader=FileSystemLoader("templates"))

posts: list[dict] = [
    {
    "id": 1,
    "author": "Corey Schafer",
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

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    template = templates.get_template("home.html")
    return template.render({"request": request, "posts": posts, "title": "Home"})
