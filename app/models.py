from pydantic import BaseModel
from typing import List, Optional

class LocationQuery(BaseModel):
    location: str

class Property(BaseModel):
    name: str
    latitude: float
    longitude: float
    distance_km: Optional[float] = None

class PropertyListResponse(BaseModel):
    properties: List[Property]
    message: Optional[str] = None