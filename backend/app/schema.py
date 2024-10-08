from pydantic import BaseModel, Field
from typing import List, Optional

class AnalysisRequest(BaseModel):
    research_field: str = Field(..., description="The main area of research")
    specific_interests: List[str] = Field(..., description="Specific topics or subfields of interest")
    academic_background: Optional[str] = Field(None, description="Brief description of the user's academic background")
    research_goals: str = Field(..., description="The user's research objective or goals")
    time_frame: Optional[str] = Field(None, description="Optional time frame for the research")


class Paper(BaseModel):
    title: str
    authors: List[str]
    abstract: str
    url: str
    publication_year: Optional[int] = None
    citations: Optional[int] = None

    def summary(self) -> str:
        return f"{self.title}\n{','.join(self.authors)}\n{self.abstract}"


class RelatedWork(BaseModel):
    title: str
    authors: List[str]
    year: int
    relevance_score: Optional[float] = Field(None, description="A score indicating relevance to the current research")


class ResearchGap(BaseModel):
    description: str
    potential_impact: Optional[str] = None
    related_papers: List[str] = Field(default_factory=list, description="Titles of papers related to this gap")


class ResearchTrend(BaseModel):
    description: str
    key_papers: List[str] = Field(default_factory=list, description="Titles of key papers in this trend")
    growth_rate: Optional[float] = None


class ResearchIdeas(BaseModel):
    title: str
    description: str
    related_gaps: List[str] = Field(default_factory=list, description="Descriptions of related research gaps")


class InitialAnalysisResult(BaseModel):
    trends: List[ResearchTrend]
    gaps: List[ResearchGap]
    related_works: List[RelatedWork]
    papers: List[Paper]


class UserRequest(BaseModel):
    request_type: str = Field(..., description="Type of request: 'problem statements' or 'methodologies'")
    initial_result: InitialAnalysisResult


class ProblemStatement(BaseModel):
    statement: str
    gaps: List[str]
    research_ideas: Optional[List[ResearchIdeas]]


class Methodology(BaseModel):
    name: str
    description: str
    problem_statement: List[str] = Field(default_factory=list, description="Problem statements this methodology is suitable for")
    pros: List[str] = Field(default_factory=list)
    cons: List[str] = Field(default_factory=list)


class FurtherResult(BaseModel):
    problem_statements: Optional[List[ProblemStatement]] = None
    methodologies: Optional[List[Methodology]] = None
    research_ideas: Optional[List[ResearchIdeas]] = None


class Message(BaseModel):
    role: str
    content: str


class Conversation(BaseModel):
    messages: List[Message]=[]
    id_: str = Field(..., description="Unique identifier for the conversation")