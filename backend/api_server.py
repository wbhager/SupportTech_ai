from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from dotenv import load_dotenv
from pathlib import Path
from logic.generate_response import generate_response

# Load .env variables
load_dotenv()
app = FastAPI()

if __name__ == "__main__":
    print(generate_response("How do I fix a 404 error in FastAPI?"))