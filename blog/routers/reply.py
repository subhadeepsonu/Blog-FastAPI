from fastapi import APIRouter

replyRouter = APIRouter(
     prefix="/reply",
    tags=["reply"]
)
@replyRouter.get("/{id}")
def get():
    return "haha"
@replyRouter.post("")
def get():
    return "haha"
@replyRouter.put("")
def get():
    return "haha"

@replyRouter.delete("/{id}")
def get():
    return "haha"