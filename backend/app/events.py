from llama_index.core.workflow import Event
from pydantic import BaseModel, Field

class ScraperEvent(Event):
    queries : list[str]

class ResearchGapEvent(Event):
    context : str
    query : str
    is_sequential : bool

class RelatedWorksEvent(Event):
    context : str
    query : str
    is_sequential : bool

class ProblemStatementsEvent(Event):
    context : str
    query : str
    is_sequential : bool

class MethodologiesEvent(Event):
    context : str
    query : str
    is_sequential : bool

class LoneLLMEvent(Event):
    context: str
    query: str

class ResultEvent(Event):
    source: str
    content: str

class Queries(BaseModel):
    queries : list[str] = Field(description="")
    