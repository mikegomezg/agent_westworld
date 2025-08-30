from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class CharacterType(str, Enum):
    HOST = "host"
    HUMAN = "human"
    HYBRID = "hybrid"

class Character(BaseModel):
    id: str = Field(..., pattern="^C-[A-Z]+$")
    name: str
    full_name: Optional[str] = None
    type: CharacterType
    role: str
    status: str = "active"
    first_appearance: str
    traits: List[str] = []
    goals: List[str] = []
    relationships: Dict[str, str] = {}
    backstory: Optional[str] = None
    narrative_function: Optional[str] = None

class Location(BaseModel):
    id: str = Field(..., pattern="^L-[A-Z]+$")
    name: str
    description: str
    region: str
    significance: str
    connected_to: List[str] = []

class Scene(BaseModel):
    id: str = Field(..., pattern="^S[0-9]{2}E[0-9]{2}-[0-9]{3}$")
    episode: str
    title: str
    location: str
    characters: List[str]
    timestamp: Optional[str] = None
    synopsis: str
    themes: List[str] = []
    reveals: List[str] = []
    conflicts: List[str] = []
    
class Episode(BaseModel):
    id: str = Field(..., pattern="^S[0-9]{2}E[0-9]{2}$")
    title: str
    air_date: str
    director: str
    writers: List[str]
    synopsis: str
    themes: List[str]
    major_events: List[str]
    scenes: List[str] = []

class Theme(BaseModel):
    id: str = Field(..., pattern="^T-[A-Z]+$")
    name: str
    description: str
    examples: List[str] = []
    significance: str

class TimelineEvent(BaseModel):
    id: str = Field(..., pattern="^TE-[A-Z]+-[0-9]+$")
    title: str
    date: Optional[str] = None
    period: str
    description: str
    characters_involved: List[str] = []
    significance: str
    episode_reference: Optional[str] = None

