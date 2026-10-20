from fastapi import FastAPI


from auth_routes import auth_router
from order_routes import order_router



app = FastAPI(
    title="API de Delivery",
    description="API para gerenciamento de pedidos de uma pizzaria",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(order_router)

@app.get("/")
def pagina_inicial():
    return {
        "mensagem": "API de Delivery em execução",
        "status": "operacional"
    }