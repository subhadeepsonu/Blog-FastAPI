from blog.database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Boolean
from sqlalchemy.orm import relationship
class blog(Base):
    __tablename__="blogs"
    id = Column(Integer,primary_key=True)
    title = Column(String)
    body = Column(String)
    edited = Column(Boolean,default=False)
    user_id = Column(Integer,ForeignKey("user.id"))
    user = relationship("user",back_populates="blog")
    comments = relationship("comments", back_populates="blog")
    bookmarks = relationship("Bookmark", back_populates="blog")

class user(Base):
    __tablename__="user"
    id= Column(Integer,primary_key=True)
    username= Column(String)
    email = Column(String,unique=True)
    password= Column(String)
    blogs = relationship("blog",back_populates="user")
    comments = relationship("comments", back_populates="user")
    bookmarks = relationship("Bookmark", back_populates="user")
    likes = relationship("likes",back_populates="user")

class comments(Base):
    __tablename__="comments"
    id=Column(Integer,primary_key=True)
    comment = Column(String)
    edited = Column(Boolean,default=False)
    user_id = Column(Integer,ForeignKey("user.id"))
    user = relationship("user",back_populates="comments")
    blog_id = Column(Integer,ForeignKey("blog.id"))
    blog = relationship("blog",back_populates="comments")
    

class bookmark(Base):
    __tablename__="bookmarks"
    id=Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey("user.id"))
    user = relationship("user",back_populates="bookmarks")
    blog_id = Column(Integer,ForeignKey("blog.id"))
    blog = relationship("blog",back_populates="bookmarks")

class reply(Base):
    __tablename__ = "replies"
    id=Column(Integer,primary_key=True)
    edited = Column(Boolean,default=False)
    comment_id = Column(Integer,ForeignKey("comments.id"))
    comment = relationship("comments",back_populates="reply") 
    user_id = Column(Integer,ForeignKey("user.id"))
    user = relationship("user",back_populates="reply")
    
class likes(Base):
    __tablename__ = "likes"
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey("user.id"))
    user = relationship("user",back_populates="likes")
    blog_id = Column(Integer,ForeignKey("blog.id"))
    blog = relationship("blog",back_populates="likes")



