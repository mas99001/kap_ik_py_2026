import subprocess as sb
sb.run('cls', shell=True)
# 📌
# QUESTION 12 ##########################################################################################
# 📌
from langchain.memory import ConversationBufferMemory
# Step 1: Create a memory object and add some conversation
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
memory.save_context({"input": "Hello"}, {"output": "Hi!"})
memory.save_context({"input": "What can you do?"}, {"output": "I can browse websites."})
memory.save_context({"input": "Explain memory."}, {"output": "I use a conversation buffer to remember our chat."})

def get_user_messages(memory_obj):
    if isinstance(memory_obj, ConversationBufferMemory):
        print("memory is a ConversationBufferMemory object")
    else:
        print("memory is NOT a ConversationBufferMemory object")
        return []
    """
    Return a list of all user message contents from the conversation history.
    User messages are those at even indices in the chat history.
    """
    history = memory_obj.load_memory_variables({})
    chat_history = history["chat_history"]
    user_msgs = []
    # TODO: Loop through chat_history with index and append only user message contents to user_msgs
    for idx, message in enumerate(chat_history):
        # Complete the logic here
        print(f"Index: {idx}, Message: {message.content}")
        if(idx % 2 == 0):
            user_msgs.append(message.content)
    return user_msgs

# Task: Complete get_user_messages and print the result
print("\n# QUESTION 12:")
print(get_user_messages(memory))

# 📌
# QUEATION 13 ##########################################################################################
# 📌
from bs4 import BeautifulSoup
def extract_text_and_count(html):
    """
    Extract the visible text from HTML and return both the text and the number of words.
    """
    # TODO: Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    # TODO: Extract the visible text as a single string
    text = soup.get_text(separator=" ", strip=True)
    # TODO: Split the text into words and count them
    word_count = len(text.split())
    return text, word_count
# Example HTML snippet
html = "<html><body><h2>Agentic AI</h2><p>Agents use tools to solve tasks.</p></body></html>"
# Task: Complete extract_text_and_count and print the result
result = extract_text_and_count(html)
print("\n# QUESTION 13:")
print(result)

# 📌
# QUESTION 14 ##########################################################################################
# 📌
# Simple dictionary of web pages
pages = {
    "https://example.com": "Agents use tools to search data. Agents coordinate tasks.",
    "https://docs.ai": "AI documentation explains how to build agents with memory and tools.",
}
def count_keyword_occurrences(input_text):
    """
    Given an input string 'URL | keyword', return the number of times keyword appears in the page content.
    The search should be case-insensitive.
    """
    # TODO: Split the input_text into url and keyword
    url, keyword = input_text.split(" | ")
    # TODO: Get the page content from the pages dictionary
    content = pages[url]
    # TODO: Count occurrences of keyword in content (case-insensitive)
    count = content.lower().count(keyword.lower())
    return count

# Task: Complete count_keyword_occurrences and print the result for a given input
print("\n# QUESTION 14:")
print(count_keyword_occurrences("https://example.com | agents"))

# 📌
# QUESTION 15 ##########################################################################################
# 📌
# Initialize memory and add three turns (six messages total)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
memory.save_context({"input": "Hi"}, {"output": "Hello"})
memory.save_context({"input": "What can you do?"}, {"output": "I can use tools."})
memory.save_context({"input": "Explain memory."}, {"output": "Memory stores our past chats."})

def trim_history(memory_obj, max_len):
    """
    Return a trimmed list of message contents from the chat history containing only the last max_len messages.
    """
    history = memory_obj.load_memory_variables({})
    messages = history["chat_history"]
    # TODO: Slice the messages list so that only the last max_len elements are kept
    trimmed = messages[-max_len:]
    # Return a list of just the message contents (not the message objects)
    return [m.content for m in trimmed]

# Task: Trim the chat history to the last 4 messages and print the result
print("\n# QUESTION 15:")
print(trim_history(memory, 4))

# 📌
# QUESTION 16 ##########################################################################################
# 📌
# Create a memory and add two turns
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
memory.save_context({"input": "Hi"}, {"output": "Hello"})
memory.save_context({"input": "What are tools?"}, {"output": "Tools let me interact with external systems."})

def get_conversation_transcript(memory_obj):
    """
    Build a transcript string where each line is prefixed with 'User:' or 'Agent:'.
    """
    history = memory_obj.load_memory_variables({})
    transcript_lines = []
    # TODO: Loop over the chat history and build the transcript
    for idx, message in enumerate(history["chat_history"]):
        # Determine prefix based on index parity (even for user, odd for agent)
        prefix = "User: " if idx % 2 == 0 else "Agent: "
        # Append the formatted line to transcript_lines
        transcript_lines.append(prefix + message.content)
    return "\n".join(transcript_lines)

# Task: Complete get_conversation_transcript and print the transcript
print("\n# QUESTION 16:")
print(get_conversation_transcript(memory))
print("\n")