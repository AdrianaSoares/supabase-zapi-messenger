import os
from supabase import create_client, Client
import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_URL = os.getenv("ZAPI_URL")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_contacts():
    response = supabase.table("contatos").select("*").execute()
    return response.data


def send_message(phone, name):
    message = f"Olá, {name} tudo bem com você?"
    payload = {
        "phone": phone,
        "message": message
    }
    headers = {"Content-Type": "application/json"}
    r = requests.post(ZAPI_URL, json=payload, headers=headers)
    print(f"Enviado para {phone}: {r.status_code}")


if __name__ == "__main__":
    contatos = get_contacts()
    for contato in contatos[:3]:  # até 3 contatos
        send_message(contato["telefone"], contato["nome"])
