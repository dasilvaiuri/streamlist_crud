import string
from typing import List
from services.database import supabase

def get_clientes():
    response = supabase.table("Clientes").select("*").execute()
    return response.data

def add_cliente(nome, idade, profissao):
    response = supabase.table("Clientes").insert({"nome": nome, "idade": idade, "profissao": profissao}).execute()
    return response.data