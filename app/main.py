from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.services.routing import RoutingService
from app.models import RouteRequest, RouteResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

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

@app.get("/map")
def mapa():
    return FileResponse("static/map.html")

