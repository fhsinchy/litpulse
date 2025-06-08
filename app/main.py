from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.scheduler import start_scheduler
from utils.db import init_db
from app.scheduler import generate_and_save

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    start_scheduler()
    yield

app = FastAPI(title="LitPulse – Quote Image Generator", lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "LitPulse is running and will auto-generate quote images."}

@app.post("/generate-now")
def generate_now():
    path = generate_and_save(debug=True)
    return {"message": "Quote generated", "image_path": path}
