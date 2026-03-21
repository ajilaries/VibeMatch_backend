from fastapi import FastAPI
from app.database import engine, Base
import app.models.user_model
from app.routes import user_routes
from app.routes import like_routes
from app.routes import connection_routes
from app.routes import match_routes


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router)
app.include_router(like_routes.router)
app.include_router(connection_routes.router)
app.include_router(match_routes.router)
