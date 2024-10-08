from llama_index.core.workflow import Workflow, step, Context, StartEvent, StopEvent
from .events import *
from typing import Tuple, Optional
from ..utils import create_llm
from .helper import create_conversation, prepare_conversation

class AnalysisWorkflow(Workflow):
    def __init__(self, memory: Conversation = None, *args, **kwargs):
        self.memory = memory if memory else create_conversation()

    @step
    async def query_creator(self, ctx: Context, event: StartEvent) -> ScraperEvent:
        pass
        
    @step
    async def scraper(self, ctx: Context, event: ScraperEvent) -> ResearchAnalysisEvent:
        pass
    
    @step
    async def gap_analyzer(self, event: ResearchAnalysisEvent) -> InitialAnalysisResult:
        pass

    @step
    async def related_works(self, event: ResearchAnalysisEvent) -> InitialAnalysisResult:
        pass

    @step
    async def problem_statement(self, event: UserRequestEvent) -> ProblemStatementsEvent:
        pass

    @step
    async def methodologies(self, event: UserRequestEvent) -> MethodologiesEvent:
        pass

    # @step
    # async def lone_wolf(self, event: LoneLLMEvent):
    #     pass

    @step
    async def final_result_collector(self, initial_result: InitialAnalysisResult, problem_statements: Optional[ProblemStatementsEvent], methodologies: Optional[MethodologiesEvent]) -> StopEvent:
        pass
