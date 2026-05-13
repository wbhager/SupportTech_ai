from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from pathlib import Path
import os

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
# tool_prompt = Path("tool_prompt.txt").read_text()
# formatter_prompt = Path("formatter_prompt.txt").read_text()

def generate_response(user_input):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(text, return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=350,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )

    response = tokenizer.decode(outputs[0][inputs.input_ids.shape[-1]:], skip_special_tokens=True)

    return response