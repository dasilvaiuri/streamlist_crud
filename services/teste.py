from supabase import create_client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")  # Deve ser a Service Role Key

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

response = supabase.table("Clientes").select("*").execute()
print(response.data)