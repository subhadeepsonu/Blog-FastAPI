from fastapi import APIRouter

userRouter = APIRouter(
    prefix="/user",
    tags=["user"]
)
@userRouter.post("/login")
def get():
    return "haha"
@userRouter.post("/register")
def get():
    return "haha"
@userRouter.get("")
def get():
    return "haha"
@userRouter.put("")
def get():
    return "haha"