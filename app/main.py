from fastapi import FastAPI
from app.database import engine, Base
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "project otter api"}