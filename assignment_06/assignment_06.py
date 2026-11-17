#
# Question 11
#
'''
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
memory.save_context({"input": "Hello"}, {"output": "Hi!"})
memory.save_context({"input": "What can you do?"}, {"output": "I can browse websites."})
memory.save_context({"input": "Explain memory."}, {"output": "I use a conversation buffer to remember our chat."})

def get_user_messages(memory_obj):
    history = memory_obj.load_memory_variables({})
    chat_history = history["chat_history"]
    user_msgs = []
    for idx, message in enumerate(chat_history):
        if idx % 2 == 0:  # even indices correspond to user messages
            user_msgs.append(message.content)
    return user_msgs

print(get_user_messages(memory))
'''
#
# Question 12
#
'''
from bs4 import BeautifulSoup

def extract_text_and_count(html):
    """
    Extract the visible text from HTML and return both the text and the number of words.
    """
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
    word_count = len(text.split())
    return text, word_count

html = "<html><body><h2>Agentic AI</h2><p>Agents use tools to solve tasks.</p></body></html>"
result = extract_text_and_count(html)
print(result)
'''
#
# Question 13
#
'''
pages = {
    "https://example.com": "Agents use tools to search data. Agents coordinate tasks.",
    "https://docs.ai": "AI documentation explains how to build agents with memory and tools.",
}

def count_keyword_occurrences(input_text):
    url, keyword = [part.strip() for part in input_text.split("|", 1)]
    content = pages.get(url, "")
    count = content.lower().count(keyword.lower())
    return count

print(count_keyword_occurrences("https://example.com | agents"))
'''
#
# Question 14
#
'''
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
memory.save_context({"input": "Hi"}, {"output": "Hello"})
memory.save_context({"input": "What can you do?"}, {"output": "I can use tools."})
memory.save_context({"input": "Explain memory."}, {"output": "Memory stores our past chats."})

def trim_history(memory_obj, max_len):
    history = memory_obj.load_memory_variables({})
    messages = history["chat_history"]
    trimmed = messages[-max_len:]  # keep only the last max_len messages
    return [m.content for m in trimmed]

print(trim_history(memory, 4))
'''
#
# Question 15
#
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
memory.save_context({"input": "Hi"}, {"output": "Hello"})
memory.save_context({"input": "What are tools?"}, {"output": "Tools let me interact with external systems."})

def get_conversation_transcript(memory_obj):
    history = memory_obj.load_memory_variables({})
    transcript_lines = []
    for idx, message in enumerate(history["chat_history"]):
        prefix = "User: " if idx % 2 == 0 else "Agent: "
        transcript_lines.append(prefix + message.content)
    return "\n".join(transcript_lines)

print(get_conversation_transcript(memory))
