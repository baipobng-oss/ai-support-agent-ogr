from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API Running"}

@app.get("/chat")
def chat():

    try:

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": "Hello"
                }
            ]
        )

        return {
            "reply": response.choices[0].message.content
        }

    except Exception as e:

        return {
            "error": str(e)
        }