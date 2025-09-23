from app.core.db import supabase
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
