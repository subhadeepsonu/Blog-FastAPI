from fastapi import APIRouter

blogRouter = APIRouter(
    prefix="/blog",
    tags=["blog"]
)
@blogRouter.get("/")
def get():
    return "haha"
@blogRouter.get("/{id}")
def get():
    return "haha"
@blogRouter.post("/")
def get():
    return "haha"
@blogRouter.put("/{id}")
def get():
    return "haha"
@blogRouter.delete("/{id}")
def get():
    return "haha"