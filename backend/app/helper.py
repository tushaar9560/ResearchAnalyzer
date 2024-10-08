import uuid
from .schema import Conversation, Message


def prepare_conversation(memory: Conversation) -> str:
    '''
    prepares and formats the conversation in string format for prompts and easy readability
    
    Args:
        memory: Conversation - the conversation class with defined schema
    Returns:
        str - the formatted conversation
    '''
    try:
        context = "\n".join([f"{message.role}: {message.content}" for message in memory.messages])
        return context
    except Exception as e:
        raise ValueError(f"Error preparing conversation")

def create_conversation() -> Conversation:
    '''
    creates a new conversation with new UUID as unique conversation id
    
    Returns:
        Conversation - the newly created conversation with defined schema
    '''
    return Conversation(messages=[], id_=str(uuid.uuid4()))

def add_message_to_conversation(conversation: Conversation, role: str, content: str) -> Conversation:
    """
    Adds a new message to an existing conversation.

    Args:
        conversation (Conversation): The existing conversation.
        role (str): The role of the message sender.
        content (str): The content of the message.

    Returns:
        Conversation: The updated conversation.
    """
    new_message = Message(role=role, content=content)
    conversation.messages.append(new_message)
    return conversation