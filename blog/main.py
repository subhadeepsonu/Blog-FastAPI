from fastapi import FastAPI
from  blog.routers import blog,bookmarks,comments,likes,reply,user
from . import database
from . import models
app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)
@app.get("/ping",tags=["health check"])
def test():
    return {
        "message":"pong"
    }
app.include_router(blog.blogRouter)
app.include_router(bookmarks.bookmarkRouter)
app.include_router(comments.commentRouter)
app.include_router(likes.likeRouter)
app.include_router(reply.replyRouter)
app.include_router(user.userRouter)

