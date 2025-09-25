from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID # Import UUID

class VocabularyIn(BaseModel):
    class_id: Optional[int] = None # class_id can be null
    kanji: Optional[str] = None
    kanji_main: Optional[str] = None # Add kanji_main
    hiragana: str
    romaji: str
    nghia: str
    audio_url: Optional[str] = None
    image_ids: List[str] = []
    sort_order: Optional[int] = 0

class VocabularyOut(VocabularyIn):
    id: UUID # Change id type to UUID
    created_at: str
