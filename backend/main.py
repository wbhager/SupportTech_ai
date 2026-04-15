from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from dotenv import load_dotenv
from pathlib import Path

# Load .env variables
load_dotenv()
app = FastAPI()



model_name = "Qwen/Qwen2.5-1.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype="auto",
    device_map="mps"
)

system_prompt = Path("system_prompt.txt").read_text()
tool_prompt = Path("tool_prompt.txt").read_text()
formatter_prompt = Path("formatter_prompt.txt").read_text()

def generate_response(user_input):
    prompt = f"""You are a helpful tech support assistant.

User: {user_input}

Assistant:"""

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=120,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Remove prompt from output
    response = response.split("Assistant:")[-1].strip()
    return response

if __name__ == "__main__":
    print(generate_response("How do I fix a 404 error in FastAPI?"))