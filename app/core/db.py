from supabase import create_client, Client
from app.core.config import settings

# Khởi tạo client Supabase
supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

# Test kết nối
def test_connection():
    try:
        # Query 1 dòng bất kỳ từ bảng vocabulary (nếu chưa có bảng thì sẽ báo lỗi)
        response = supabase.table("vocabulary").select("*").limit(1).execute()
        print("✅ Supabase connected successfully!")
        print("Sample data:", response.data)
    except Exception as e:
        print("❌ Supabase connection failed:", e)


if __name__ == "__main__":
    test_connection()
