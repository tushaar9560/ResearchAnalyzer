from llama_index.core.workflow import Event
from pydantic import Field
from typing import List
from .schema import *


class ScraperEvent(Event):
    queries: List[str]

class ResearchAnalysisEvent(Event):
    context: str
    papers: List[Paper] = Field(..., description="List of scraped papers")

class UserRequestEvent(Event):
    request_type: str = Field(..., description="Type of request: 'problem_statements' or 'methodologies'")
    initial_resutl: InitialAnalysisResult

class ProblemStatementsEvent(Event):
    problem_statements: List[str] = Field(..., description="Generated problem statements")

class MethodologiesEvent(Event):
    methodologies: List[str] = Field(..., description="Suggested methodologies")