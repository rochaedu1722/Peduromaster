
from fastapi import FastAPI
from app.routes import router
from modes import ultra, omega, modo_rio_v12

app = FastAPI()
app.include_router(router)

def executar_modos():
    print("🔁 Iniciando execução dos modos ativos...")
    ultra.executar()
    omega.executar()
    modo_rio_v12.executar()

if __name__ == "__main__":
    executar_modos()
