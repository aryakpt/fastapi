from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db, engine
import schemas, models
from typing import List

app = FastAPI()

# === ORM === #
# models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)


@app.get("/api/v1/blog")
async def getBlogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/api/v1/blog/{id}", response_model=schemas.Blog)
def getBlog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id: {id} is not found",
        )
    return blog


@app.post("/api/v1//blog", status_code=status.HTTP_201_CREATED)
async def createBlog(request: schemas.Blog, db: Session = Depends(get_db)):
    newBlog = models.Blog(
        title=request.title,
        body=request.body,
        created_at=request.created_at,
        updated_at=request.update_at,
    )
    db.add(newBlog)
    db.commit()
    # Calling again the newBlog
    db.refresh(newBlog)
    return newBlog


@app.put("/api/v1/blog/{id}")
async def updateBlog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise (
            HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with id: {id} is not found",
            )
        )
    blog.update(
        {
            "title": request.title,
            "body": request.body,
            "updated_at": request.update_at,
        },
        synchronize_session=False,
    )
    db.commit()
    db.refresh(blog)
    return blog


@app.delete("/api/v1/blog/{id}")
async def deleteBlog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise (
            HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with id: {id} is not found",
            )
        )
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Blog with id: {id} deleted"}


# Inisialisasi CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.post("/api/v1/user")
def createPost(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(request)
    return request
