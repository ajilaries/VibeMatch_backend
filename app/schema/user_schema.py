from pydantic import BaseModel
from datetime import date
from typing import Optional

class UserSchema(BaseModel):
    username:str
    email:str
    password:str
    dob:date
    bio:Optional[str]=None
    location:Optional[str]=None