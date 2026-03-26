from pydantic import BaseModel
from typing import Optional
from datetime import date

class UpdateProfileSchema(BaseModel):
    username:Optional[str]=None
    bio:Optional[str]=None
    dob:Optional[date]=None
    profile_image:Optional[str]=None
    profile_video:Optional[str]=None
    location:Optional[str]=None
