import heapq


# Base de conocimiento para las rutas
base_conocimiento = {
    "estaciones": {
        "A": {"B": {"tiempo": 10, "transbordos": 1}, "C": {"tiempo": 5, "transbordos": 0}},
        "B": {"A": {"tiempo": 10, "transbordos": 1}, "C": {"tiempo": 3, "transbordos": 0}},
        "C": {"A": {"tiempo": 5, "transbordos": 0}, "B": {"tiempo": 3, "transbordos": 0}},
    },
    "restricciones": [
        # Reglas adicionales
        {"de": "A", "a": "B", "restriccion": "horario_pico", "activo": False}
    ]
}



# Dijkstra
def dijkstra(base_conocimiento, inicio, destino):
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio, []))  # (costo, nodo, ruta)
    visitados = set()

    while cola_prioridad:
        costo_actual, nodo, ruta = heapq.heappop(cola_prioridad)

        if nodo == destino:
            return ruta + [nodo], costo_actual

        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, info in base_conocimiento["estaciones"].get(nodo, {}).items():
                if vecino not in visitados:
                    nuevo_costo = costo_actual + info["tiempo"]
                    nueva_ruta = ruta + [nodo]
                    heapq.heappush(cola_prioridad, (nuevo_costo, vecino, nueva_ruta))

    return None, float('inf')  # No se encontró ruta

# Ejemplo de uso
inicio = "A"
destino = "C"
ruta, costo = dijkstra(base_conocimiento, inicio, destino)
print(f"Ruta: {ruta}, Costo: {costo}")


def aplicar_reglas(base_conocimiento, ruta):
    """
    Aplica las reglas lógicas para verificar si hay restricciones en la ruta.
    """
    for regla in base_conocimiento["restricciones"]:
        if regla["activo"]:
            if regla["de"] in ruta and regla["a"] in ruta:
                print(f"Aplicando restricción: {regla}")
                

aplicar_reglas(base_conocimiento, ruta)

def encontrar_ruta_inteligente(base_conocimiento, inicio, destino):
    ruta, costo = dijkstra(base_conocimiento, inicio, destino)
    
    if ruta is None:
        print(f"No se encontró ruta desde {inicio} a {destino}.")
        return

    aplicar_reglas(base_conocimiento, ruta)

    print(f"La mejor ruta desde {inicio} hasta {destino} es: {ruta} con un costo de {costo} minutos.")
    
encontrar_ruta_inteligente(base_conocimiento, "A", "C")
