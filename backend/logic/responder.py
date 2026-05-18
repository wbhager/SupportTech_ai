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