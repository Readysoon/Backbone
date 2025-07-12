from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class Platte(BaseModel):
    name: Optional[str] = None
    koerperteil: Optional[str] = None
    status: Optional[int] = None
    productzustand: Optional[str] = None
    sdk: Optional[str] = None
    masse: Optional[str] = None
    hersteller: Optional[str] = None
    bewahrungsort: Optional[str] = None
    bestellungstag: Optional[date] = None
    ansprechpartner: Optional[str] = None
    beschreibung: Optional[str] = None
    chartData: Optional[List[int]] = None