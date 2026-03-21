from fastapi import FastAPI
from app.database import engine, Base
import app.models.user_model
from app.routes import user_routes


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router)