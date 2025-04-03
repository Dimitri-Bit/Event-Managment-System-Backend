from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

class PartyBase(BaseModel):
    name_party: str
    url_image_full: HttpUrl
    name_organizer: str
    date_start: datetime
    date_end: datetime
    name_town: str
    name_country: str
    name_type: str
    text_entry_fee: Optional[float] = None
    text_more: Optional[str] = None
    url_organizer: Optional[HttpUrl] = None
    url_party: Optional[HttpUrl] = None

class PartyCreate(BaseModel):
    pass

class PartyUpdate(BaseModel):
    pass

class PartyResponse(BaseModel):

    class Config:
        orm_mode = True
