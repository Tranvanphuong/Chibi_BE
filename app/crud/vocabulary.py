from app.core.db import supabase
from app.models.vocabulary import VocabularyIn
from uuid import UUID # Import UUID

def create_vocabulary(item: VocabularyIn):
    # Convert Pydantic model to dictionary, excluding unset fields to allow DB defaults
    item_dict = item.dict(exclude_unset=True)
    return supabase.table("vocabulary").insert(item_dict).execute()

def get_vocabulary(vocab_id: UUID): # Change vocab_id type to UUID
    return supabase.table("vocabulary").select("*").eq("id", str(vocab_id)).execute()

def list_vocabulary(class_id: int = None):
    query = supabase.table("vocabulary").select("*").order("sort_order")
    if class_id is not None: # Check for None explicitly
        query = query.eq("class_id", class_id)
    return query.execute()

def update_vocabulary(vocab_id: UUID, item: VocabularyIn): # Change vocab_id type to UUID
    # Convert Pydantic model to dictionary, excluding unset fields to allow partial updates
    item_dict = item.dict(exclude_unset=True)
    return supabase.table("vocabulary").update(item_dict).eq("id", str(vocab_id)).execute()

def delete_vocabulary(vocab_id: UUID): # Change vocab_id type to UUID
    return supabase.table("vocabulary").delete().eq("id", str(vocab_id)).execute()
