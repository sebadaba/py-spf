import osmnx as ox
from app.models import RouteRequest, RouteResponse, GeoJSONGeometry

class RoutingService:
    def __init__(self):
        self.graph_cache = {} 
    
    def obtener_grafo(self, lat, lon, radio_km):
        tile_lat = round(lat, 2)
        tile_lon = round(lon, 2)
        key = f"{tile_lat},{tile_lon}"

        if key not in self.graph_cache:
            G = ox.graph_from_point(
                (lat, lon),
                dist=radio_km * 1000,
                network_type="drive",
                simplify=True
            )
            G = ox.utils_graph.truncate.largest_component(G, strongly=True)
            self.graph_cache[key] = G

        return self.graph_cache[key]
    
    def calcular_ruta(self, request: RouteRequest) -> RouteResponse:
        """Calcula la ruta más económica usando el algoritmo de Dijkstra"""
        
        G = self.obtener_grafo(request.origen_lat, request.origen_lon, radio_km=10)
        #G = ox.project_graph(G)

        
        orig_node = ox.distance.nearest_nodes(G, X=request.origen_lon, Y=request.origen_lat )
        dest_node = ox.distance.nearest_nodes(G, X=request.destino_lon, Y=request.destino_lat)
        
		# placeholder
        route = ox.shortest_path(G, orig_node, dest_node, weight='length')

        edge_lengths = ox.routing.route_to_gdf(G, route)["length"]
        distancia_m = round(sum(edge_lengths))

        distancia_km = distancia_m / 1000

        costo = (distancia_km / request.autonomia) * request.precio_combustible
        
        coordenadas = [
            [G.nodes[node]['x'], G.nodes[node]['y']]
            for node in route
        ]
        
        return RouteResponse(
            distancia_km=round(distancia_km, 2),
            costo_combustible=round(costo, 2),
            geometria=GeoJSONGeometry(
                type="LineString",
                coordinates=coordenadas
            )
        )