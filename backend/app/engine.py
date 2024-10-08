import logging
from llama_index.core.workflow import Workflow, step, Context, StartEvent, StopEvent
from .events import *
from typing import Tuple, Optional, List
from ..utils import create_llm
from .helper import create_conversation, prepare_conversation, add_message_to_conversation
from .schema import *
from .constants import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AnalysisWorkflow(Workflow):
    def __init__(self, memory: Conversation = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.memory = memory if memory else create_conversation()
        self.llm = create_llm("")

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
    async def problem_statement(self, event: UserRequestEvent) -> ProblemStatementsEvent:
        pass

    @step
    async def methodologies(self, event: UserRequestEvent) -> MethodologiesEvent:
        pass


    @step
    async def final_result_collector(self, initial_result: InitialAnalysisResult, problem_statements: Optional[ProblemStatementsEvent], methodologies: Optional[MethodologiesEvent]) -> StopEvent:
        pass
