import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

files_content = {
    "app/main.py": """from fastapi import FastAPI
from app.routers import vocabulary

app = FastAPI(title="Japanese Learning App API")

# Gắn router
app.include_router(vocabulary.router, prefix="/vocabulary", tags=["Vocabulary"])
""",

    "app/core/config.py": """import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SUPABASE_URL: str = os.getenv("SUPABASE_URL")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")

settings = Settings()
""",

    "app/core/db.py": """from supabase import create_client
from app.core.config import settings

supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
""",

    "app/models/vocabulary.py": """from pydantic import BaseModel
from typing import Optional, List

class VocabularyIn(BaseModel):
    class_id: int
    kanji: Optional[str] = None
    hiragana: str
    romaji: str
    nghia: str
    audio_url: Optional[str] = None
    image_ids: List[str] = []
    sort_order: Optional[int] = 0

class VocabularyOut(VocabularyIn):
    id: int
    created_at: str
""",

    "app/crud/vocabulary.py": """from app.core.db import supabase
from app.models.vocabulary import VocabularyIn

def create_vocabulary(item: VocabularyIn):
    return supabase.table("vocabulary").insert(item.dict()).execute()

def get_vocabulary(vocab_id: int):
    return supabase.table("vocabulary").select("*").eq("id", vocab_id).execute()

def list_vocabulary(class_id: int = None):
    query = supabase.table("vocabulary").select("*").order("sort_order")
    if class_id:
        query = query.eq("class_id", class_id)
    return query.execute()

def update_vocabulary(vocab_id: int, item: VocabularyIn):
    return supabase.table("vocabulary").update(item.dict()).eq("id", vocab_id).execute()

def delete_vocabulary(vocab_id: int):
    return supabase.table("vocabulary").delete().eq("id", vocab_id).execute()
""",

    "app/routers/vocabulary.py": """from fastapi import APIRouter, HTTPException
from typing import List, Optional
from app.models.vocabulary import VocabularyIn, VocabularyOut
from app import crud

router = APIRouter()

@router.post("/", response_model=VocabularyOut)
def create(item: VocabularyIn):
    response = crud.vocabulary.create_vocabulary(item)
    if response.data:
        return response.data[0]
    raise HTTPException(status_code=400, detail="Không thể thêm từ vựng")

@router.get("/", response_model=List[VocabularyOut])
def get_all(class_id: Optional[int] = None):
    response = crud.vocabulary.list_vocabulary(class_id)
    return response.data

@router.get("/{vocab_id}", response_model=VocabularyOut)
def get_one(vocab_id: int):
    response = crud.vocabulary.get_vocabulary(vocab_id)
    if response.data:
        return response.data[0]
    raise HTTPException(status_code=404, detail="Không tìm thấy từ vựng")

@router.put("/{vocab_id}", response_model=VocabularyOut)
def update(vocab_id: int, item: VocabularyIn):
    response = crud.vocabulary.update_vocabulary(vocab_id, item)
    if response.data:
        return response.data[0]
    raise HTTPException(status_code=400, detail="Không thể cập nhật từ vựng")

@router.delete("/{vocab_id}")
def delete(vocab_id: int):
    response = crud.vocabulary.delete_vocabulary(vocab_id)
    if response.data:
        return {"message": "Đã xóa thành công", "deleted": response.data}
    raise HTTPException(status_code=404, detail="Không tìm thấy từ vựng")
""",

    "app/services/audio_service.py": """# Service xử lý file âm thanh (upload/download)
# Có thể mở rộng dùng Supabase Storage hoặc AWS S3
def process_audio(file_path: str):
    return f"Processed audio: {file_path}"
""",

    "app/utils/file_utils.py": """import os

def allowed_file(filename: str, allowed_extensions=None) -> bool:
    if allowed_extensions is None:
        allowed_extensions = {"png", "jpg", "jpeg", "gif", "mp3"}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions
""",

    "tests/test_vocabulary.py": """from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/vocabulary")
    assert response.status_code == 200
""",

    "requirements.txt": """fastapi
uvicorn
supabase
python-dotenv
pydantic
""",

"README.md": """# Japanese Learning App (Backend)

## Chạy ứng dụng
```bash
uvicorn app.main:app --reload
API docs: http://127.0.0.1:8000/docs

""",
".env": """SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-service-role-key
"""
}