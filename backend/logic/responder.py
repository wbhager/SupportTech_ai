from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from pathlib import Path
import os
from backend.tools.memory import add_to_history, get_trimmed_history

model_name = "Qwen/Qwen2.5-1.5B-Instruct"
hf_token = os.getenv("HF_TOKEN")

tokenizer = AutoTokenizer.from_pretrained(model_name, token=hf_token)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    token = hf_token,
    dtype="auto",
    device_map="mps"
)

system_prompt = Path(__file__).parent.parent / "prompts" / "system_prompt.txt"
system_prompt = system_prompt.read_text()

def respond_to_user(user_input, conv_id, tool_name=None, tool_result=None, system_prompt=system_prompt):
    if tool_result:
        if tool_name == "file_reader":
            augmented_message = f"The following is file contents to analyze as text only, do not output json UNLESS the extension type is .json and it is used in conjunction to help provide context:\n\n{tool_result}\n\nQuestion: {user_input}"
        elif tool_name == "web_search":
            augmented_message = f"Use this search result to answer:\n\n{tool_result}\n\nQuestion: {user_input}"
        elif tool_name == "parse_log":
            augmented_message = f"The following is log contents and additional context information to analyze as text only, and it is used in conjunction to help provide context:\n\n{tool_result}\n\nQuestion: {user_input}"
        else:
            augmented_message = user_input

    add_to_history(conv_id, role = "user", content = user_input)

    history = get_trimmed_history(conv_id, max_messages = 10)
    clean_history = [{"role": msg["role"], "content": msg["content"]} for msg in history]
    
    messages = [
        {"role": "system", "content": system_prompt},
        *clean_history,
        {"role": "user", "content": augmented_message}
    ]

    text = tokenizer.apply_chat_template(messages, tokenize = False, add_generation_prompt = True)
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens = 512, do_sample = True, temperature = 0.7, top_p = 0.9)

    return tokenizer.decode(outputs[0][inputs.input_ids.shape[-1]:], skip_special_tokens = True)