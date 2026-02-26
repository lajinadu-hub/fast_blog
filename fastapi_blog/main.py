from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader, select_autoescape
# Environment is the core Jinja2 object that manages templates.
#FileSystemLoader tells Jinja2 where your HTML template files live on disk.

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Create Jinja2 environment 
templates = Environment( 
    loader=FileSystemLoader("templates"), 
    autoescape=select_autoescape(["html", "xml"]) )


# Add url_for helper to Jinja2 
def url_for(name: str, *args, **kwargs): 
    if args: 
        kwargs["path"] = args[0] 
    return app.url_path_for(name, **kwargs) 
templates.globals["url_for"] = url_for

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

@app.get("/", response_class=HTMLResponse, include_in_schema=False, name="home")
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False, name="posts")
async def home(request: Request):
    template = templates.get_template("home.html")
    return template.render({"request": request, "posts": posts, "title": "Home"})

@app.get("/posts/{post_id}", include_in_schema=False, response_class=HTMLResponse)
async def get_posts(request: Request, post_id: int):
    template = templates.get_template("post.html")
    for post in posts:
        if post.get("id") == post_id:
            title = post["title"][:50]
            return template.render({"request": request, "post": post, "title": title})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Not Found!")

