from fastapi import APIRouter

commentRouter = APIRouter(
     prefix="/comment",
    tags=["comment"]
)
@commentRouter.get("")
def get():
    return "haha"
@commentRouter.post("")
def get():
    return "haha"
@commentRouter.put("/{id}")
def get(id):
    return "haha"
@commentRouter.delete("/{id}")
def get():
    return "haha"