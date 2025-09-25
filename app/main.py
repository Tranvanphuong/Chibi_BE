from fastapi import FastAPI, APIRouter, HTTPException
from app.routers import vocabulary
from fastapi.middleware.cors import CORSMiddleware
from app.services.audio_service import generate_and_save_audio
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
app = FastAPI(title="Japanese Learning App API")

# Mount static files directory
app.mount("/asset", StaticFiles(directory="app/asset"), name="asset")

origins = [
    "http://localhost",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "https://chibiv2.netlify.app",
    "file://",
    "http://127.0.0.1:8000" # Thêm cả origin của API nếu cần
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}
# Gắn router
app.include_router(vocabulary.router, prefix="/vocabulary", tags=["Vocabulary"])

# Audio Router
audio_router = APIRouter()

@audio_router.get("/speak")
async def speak_word(word: str):
    """
    Generates or retrieves an audio file for a given Japanese word.
    """
    if not word:
        raise HTTPException(status_code=400, detail="Word parameter is required.")
    
    try:
        file_path = generate_and_save_audio(word)
        # Return the full URL for frontend to access
        # Assuming the base URL is http://127.0.0.1:8000 and static files are served from /asset
        full_url = f"/asset/speaking/{os.path.basename(file_path)}"
        return {"audio_path": full_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate audio: {e}")

app.include_router(audio_router, prefix="/audio", tags=["Audio"])
