from pydantic import BaseModel, Field
from typing import List

class RouteRequest(BaseModel):
    origen_lat: float = Field(..., ge=-90, le=90, description="Latitud del punto de origen")
    origen_lon: float = Field(..., ge=-180, le=180, description="Longitud del punto de origen")
    destino_lat: float = Field(..., ge=-90, le=90, description="Latitud del punto de destino")
    destino_lon: float = Field(..., ge=-180, le=180, description="Longitud del punto de destino")
    autonomia: float = Field(..., gt=0, description="Autonomía del vehículo en kilómetros por litro")
    precio_combustible: float = Field(..., description="Precio del combustible en pesos por litro")

class GeoJSONGeometry(BaseModel):
    type: str = "LineString"
    coordinates: List[List[float]]

class RouteResponse(BaseModel):
    distancia_km: float = Field(..., description="Distancia total en kilómetros")
    costo_combustible: float = Field(..., description="Costo estimado en pesos")
    geometria: GeoJSONGeometry