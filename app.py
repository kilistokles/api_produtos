from fastapi import FastAPI

app = FastAPI()


vendas = {
    1: {"item": "lata", "preço_unitario": 4, "quantidade": 5},
    2: {"item": "cola", "preco_unitario": 6, "quantidade": 3},
    3: {"item": "colher", "preco_unitario": 1, "quantidade": 10},
    4: {"item": "prato", "preco_unitario": 7, "quantidade": 4},

}

@app.get("/")
def home():
    return "Teste da api"

@app.get("/produtos")
def produtos():
    return vendas