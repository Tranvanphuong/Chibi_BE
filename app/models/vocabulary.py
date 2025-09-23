from pydantic import BaseModel
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
