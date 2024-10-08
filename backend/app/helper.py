import uuid
from .schema import Conversation


def prepare_conversation(memory: Conversation) -> str:
    '''
    prepares and formats the conversation in string format for prompts and easy readability
    
    Args:
        memory: Conversation - the conversation class with defined schema
    Returns:
        str - the formatted conversation
    '''
    context = ""
    for message in memory.messages:
        context += message.role + ": " + message.content
    return context

def create_conversation() -> Conversation:
    '''
    creates a new conversation with new UUID as unique conversation id
    
    Returns:
        Conversation - the newly created conversation with defined schema
    '''
    return Conversation(messages=[], id_=str(uuid.uuid4()))