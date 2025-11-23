from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API para calcular la ruta más económica entre dos puntos."}
