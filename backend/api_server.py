from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
from logic.generate_response import generate_response

# Load .env variables
load_dotenv()
app = FastAPI()

app.include_router(chat.router)

if __name__ == "__main__":
    print(generate_response("How do I fix a 404 error in FastAPI?"))