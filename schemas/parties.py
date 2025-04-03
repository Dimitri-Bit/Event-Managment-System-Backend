from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class PartyCreate(BaseModel):
    name_party: str = Field(min_length=3, max_length=255)
    url_image_full: str
    name_organizer: str = Field(min_length=3, max_length=255)
    date_start: datetime
    date_end: datetime
    name_town: str = Field(min_length=2, max_length=255)
    name_country: str = Field(min_length=2, max_length=255)
    name_type: str = Field(min_length=3, max_length=255)
    text_entry_fee: Optional[float] = None
    text_more: Optional[str] = Field(max_length=1000)
    url_organizer: Optional[str] = None
    url_party: Optional[str] = None

class PartyResponse(BaseModel):
    id: int
    name_party: str
    url_image_full: str
    name_organizer: str
    date_start: datetime
    date_end: datetime
    name_town: str
    name_country: str
    name_type: str
    text_entry_fee: Optional[float] = None
    text_more: Optional[str] = None
    url_organizer: Optional[str] = None
    url_party: Optional[str] = None

    class Config:
        from_attributes = True

class PartyUpdate(BaseModel):
    name_party: Optional[str] = Field(min_length=3, max_length=255)
    url_image_full: Optional[str]
    name_organizer: Optional[str] = Field(min_length=3, max_length=255)
    date_start: Optional[datetime]
    date_end: Optional[datetime]
    name_town: Optional[str] = Field(min_length=2, max_length=255)
    name_country: Optional[str] = Field(min_length=2, max_length=255)
    name_type: Optional[str] = Field(min_length=3, max_length=255)
    text_entry_fee: Optional[float] = None
    text_more: Optional[str] = Field(max_length=1000)
    url_organizer: Optional[str] = None
    url_party: Optional[str] = None

    class Config:
        orm_mode = True
