from pydantic import BaseModel, Field

class RouteRequest(BaseModel):
    origen_lat: float = Field(..., ge=-90, le=90)
    origen_lon: float = Field(..., ge=-180, le=180)
    destino_lat: float = Field(..., ge=-90, le=90)
    destino_lon: float = Field(..., ge=-180, le=180)
    autonomia: float = Field(..., gt=0)  # km/lt
    precio_combustible: float = Field(default=1.5)  # $/lt

class RouteResponse(BaseModel):
    distancia_km: float
    costo_estimado: float
    ruta_coords: list[tuple[float, float]]
    nodos: list[int]