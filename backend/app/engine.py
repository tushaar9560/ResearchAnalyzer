from llama_index.core.workflow import Workflow, step, Context, StartEvent, StopEvent
from .events import *
from typing import Tuple, Optional
from ..utils import create_llm


class AnalysisWorkflow(Workflow):
    def __init__(self):
        pass
    @step
    async def query_creator(self, ctx: Context, event: StartEvent) -> ScraperEvent:
        pass
        
    @step
    async def scraper(self, ctx: Context, event: ScraperEvent):
        pass
    
    @step
    async def gap_analyzer(self, event: ResearchGapEvent):
        pass

    @step
    async def related_works(self, event: RelatedWorksEvent):
        pass

    @step
    async def problem_statement(self, event: ProblemStatementsEvent):
        pass

    @step
    async def methodologies(self, event: MethodologiesEvent):
        pass

    # @step
    # async def lone_wolf(self, event: LoneLLMEvent):
    #     pass

    @step
    async def collector(self, event: ResultEvent)-> StopEvent:
        pass
