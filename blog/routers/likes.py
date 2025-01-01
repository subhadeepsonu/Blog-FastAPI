from fastapi import APIRouter

likeRouter = APIRouter(
     prefix="/likes",
    tags=["likes"]
)
@likeRouter.get("")
def get():
    return "haha"
@likeRouter.post("")
def get():
    return "haha"
@likeRouter.delete("/{id}")
def get():
    return "haha"
