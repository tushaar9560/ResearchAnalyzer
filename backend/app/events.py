from llama_index.core.workflow import Event
from pydantic import BaseModel, Field
from typing import List, Optional
from .schema import *


class ScraperEvent(Event):
    queries: List[str]


class ResearchAnalysisEvent(Event):
    context: str
    papers: List[Paper] = Field(..., description="List of scraped papers")


class UserRequestEvent(Event):
    request_type