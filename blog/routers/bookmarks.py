from fastapi import APIRouter

bookmarkRouter = APIRouter(
     prefix="/bookmark",
    tags=["bookmark"]
)
@bookmarkRouter.get("")
def get():
    return "haha"
@bookmarkRouter.post("")
def get():
    return "haha"
@bookmarkRouter.delete("/{id}")
def get():
    return "haha"
