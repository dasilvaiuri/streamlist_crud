from supabase import create_client, Client
import os
import streamlit as st

# Load environment variables from .env file
#load_dotenv(dotenv_path=os.path.join("venv", ".env"))
# Initialize connection local
#url = os.getenv("SUPABASE_URL")
#key = os.getenv("SUPABASE_KEY")


# Initialize connection remote
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

supabase: Client = create_client(url, key)
