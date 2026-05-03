from fastapi import FastAPI
from dotenv import load_dotenv
from routes import chat
from logic.generate_response import generate_response
from fastapi.middleware.cors import CORSMiddleware


# Load .env variables
load_dotenv()
app = FastAPI()

app.include_router(chat.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

