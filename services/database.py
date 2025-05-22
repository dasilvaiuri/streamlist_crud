from supabase import create_client, Client
import os

# Load environment variables from .env file
#load_dotenv(dotenv_path=os.path.join("venv", ".env"))
# Initialize connection.
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)
