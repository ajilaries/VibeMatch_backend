from fastapi import FastAPI
from app.database import engine
from app.models.user_model import Base
from app.routes import user_routes

app=FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(user_routes.router)

@app.get("/")
def home():
    return {"message":"Vibematch backend running"}
