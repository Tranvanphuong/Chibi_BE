from fastapi import FastAPI
from app.routers import vocabulary
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="Japanese Learning App API")

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
