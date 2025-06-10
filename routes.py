
from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/teste-envio")
def enviar_teste_telegram():
    TOKEN = "7590925126:AAFiCWBAFfztEm_EqLoU2QibTfYkndPhv9M"
    CHAT_ID = 1146864652
    MSG = "🚀 Teste de envio: o bot Rochinha Pé Duro está online e funcionando!"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": MSG}
    response = requests.post(url, data=data)

    return {
        "status_code": response.status_code,
        "response": response.text
    }
