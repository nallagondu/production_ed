from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Live from production via WSL + Vercel + GitHub"}

