from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

# Create base model for each message to model, ensures correctness of input
class Message(BaseModel):
    content: str

# Load .env variables
load_dotenv()
app = FastAPI()

# Initialize OpenAI client
client = OpenAI()

# Health check endpoint - checks to see if the server is running
@app.get("/")
def root():
    return {"message": "API is running"}

# Chat endpoint - takes in user input and returns a response from the model
@app.post("/chat")
def chat(user_input: Message):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=user_input.content
    )

    return {
        "reply": response.output_text
    }