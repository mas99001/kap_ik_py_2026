import subprocess as sb
sb.run('cls', shell=True)
                            # QUEATION 12 #
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import HumanMessage

# Create memory
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Add conversation
memory.save_context({"input": "Hello"}, {"output": "Hi!"})
memory.save_context(
    {"input": "What can you do?"},
    {"output": "I can browse websites."}
)
memory.save_context(
    {"input": "Explain memory."},
    {"output": "I use a conversation buffer to remember our chat."}
)

def get_user_messages(memory_obj):
    """
    Return all user messages from chat history.
    """
    history = memory_obj.load_memory_variables({})
    chat_history = history["chat_history"]

    return [
        msg.content
        for msg in chat_history
        if isinstance(msg, HumanMessage)
    ]

print(get_user_messages(memory))