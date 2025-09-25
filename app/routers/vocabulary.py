from fastapi import APIRouter, HTTPException
from typing import List, Optional
from uuid import UUID # Import UUID
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
def get_one(vocab_id: UUID): # Change vocab_id type to UUID
    response = crud.vocabulary.get_vocabulary(vocab_id)
    if response.data:
        return response.data[0]
    raise HTTPException(status_code=404, detail="Không tìm thấy từ vựng")

@router.put("/{vocab_id}", response_model=VocabularyOut)
def update(vocab_id: UUID, item: VocabularyIn): # Change vocab_id type to UUID
    response = crud.vocabulary.update_vocabulary(vocab_id, item)
    if response.data:
        return response.data[0]
    raise HTTPException(status_code=400, detail="Không thể cập nhật từ vựng")

@router.delete("/{vocab_id}")
def delete(vocab_id: UUID): # Change vocab_id type to UUID
    response = crud.vocabulary.delete_vocabulary(vocab_id)
    if response.data:
        return {"message": "Đã xóa thành công", "deleted": response.data}
    raise HTTPException(status_code=404, detail="Không tìm thấy từ vựng")
