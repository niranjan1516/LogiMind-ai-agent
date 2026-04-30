from fastapi import FastAPI

app = FastAPI(title="LogiMind OS API", version="1.0.0")

@app.get("/")
def read_root():
    return {"status": "operational", "message": "LogiMind OS Backend is running"}