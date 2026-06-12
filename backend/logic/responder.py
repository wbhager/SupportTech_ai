from pathlib import Path
import os
from ollama import Client
from backend.tools.memory import add_to_history, get_trimmed_history

ollama_client = Client(host="http://localhost:11434")

system_prompt = Path(__file__).parent.parent / "prompts" / "system_prompt.txt"
system_prompt = system_prompt.read_text()

def respond_to_user(user_input, conv_id, tool_name=None, tool_result=None, relevant_chunks=None, system_prompt=system_prompt):
    if tool_result:
        if tool_name == "file_reader":
            augmented_message = f"The following is file contents to analyze as text only, do not output json UNLESS the extension type is .json and it is used in conjunction to help provide context:\n\n{tool_result}\n\nQuestion: {user_input}"
        elif tool_name == "web_search":
            augmented_message = f"Use this search result to answer:\n\n{tool_result}\n\nQuestion: {user_input}"
        elif tool_name == "parse_log":
            augmented_message = f"The following is log contents and additional context information to analyze as text only, and it is used in conjunction to help provide context:\n\n{tool_result}\n\nQuestion: {user_input}"
    else:
        augmented_message = user_input

    history = get_trimmed_history(conv_id, max_messages = 4)
    clean_history = [{"role": msg["role"], "content": msg["content"]} for msg in history]
    clean_history = clean_history[:-1]

    rag_context = "\n\n".join(relevant_chunks)
    rag_message = f"""Here is some potentially relevant context from the codebase. 
        Use it only if it helps answer the question, ignore it otherwise:

        {rag_context}

        {augmented_message}"""
    
    messages = [
        {"role": "system", "content": system_prompt},
        *clean_history,
        {"role": "user", "content": rag_message}
    ]

    print(f"DEBUG RAG: retrieved {len(relevant_chunks)} chunks")
    for i, chunk in enumerate(relevant_chunks):
        print(f"DEBUG RAG chunk {i+1}: {chunk[:100]}...")

    response = ollama_client.chat(
        model="qwen2.5:3b",
        messages=messages,
        options={
            "num_predict": 256,
            "temperature": 0.7,
            "top_p": 0.9,
        }
    )

    result = response.message.content
    add_to_history(conv_id, "assistant", result)
    return result