from fastapi import FastAPI, HTTPException
from app.services.routing import RoutingService
from app.models import RouteRequest, RouteResponse

app = FastAPI()
routing_service = RoutingService()

@app.get("/")
def root():
    return {"message": "API para calcular la ruta más económica entre dos puntos."}

@app.post("/route", response_model=RouteResponse)
async def calcular_ruta(request: RouteRequest):
    try:
        return routing_service.calcular_ruta(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
