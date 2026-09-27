# ============================================================
# SISTEMA INTELIGENTE DE RUTAS - TRANSPORTE MASIVO
# ============================================================

# ------------------------------------------------------------
# 1. BASE DE CONOCIMIENTO
# ------------------------------------------------------------

# Hechos: conexiones directas entre estaciones.
# Cada conexión tiene un tiempo estimado en minutos.

conexiones = [
    ("Estacion 1", "Estacion 2", 5),
    ("Estacion 2", "Estacion 3", 4),
    ("Estacion 3", "Estacion 4", 5),
    ("Estacion 4", "Estacion 5", 6),
    ("Estacion 5", "Estacion 6", 4),
    ("Estacion 6", "Estacion 7", 10),
    ("Estacion 7", "Estacion 8", 15),
    ("Estacion 6", "Estacion 8", 12),
    ("Estacion 7", "Estacion 4", 7),
    ("Estacion 1", "Estacion 3", 8),
]


# ------------------------------------------------------------
# 2. REGLAS LÓGICAS
# ------------------------------------------------------------

def obtener_conexiones(estacion):
    """
    Regla 1:
    Si una estación tiene una conexión directa,
    entonces esa conexión puede ser utilizada.
    """

    resultado = []

    for origen, destino, tiempo in conexiones:

        if origen == estacion:
            resultado.append((destino, tiempo))

        elif destino == estacion:
            resultado.append((origen, tiempo))

    return resultado


def existe_conexion(origen, destino):
    """
    Regla 2:
    Si dos estaciones están conectadas,
    entonces es posible desplazarse entre ellas.
    """

    for estacion1, estacion2, tiempo in conexiones:

        if ((estacion1 == origen and estacion2 == destino) or
            (estacion1 == destino and estacion2 == origen)):

            return True

    return False


# ------------------------------------------------------------
# 3. MOTOR DE INFERENCIA
# ------------------------------------------------------------

def encontrar_rutas(origen, destino, visitadas=None):
    """
    El sistema aplica las reglas de la base de conocimiento
    para descubrir las rutas posibles entre el origen y destino.
    """

    if visitadas is None:
        visitadas = set()

    # Evita visitar nuevamente una estación.
    visitadas = visitadas | {origen}

    # Si llegamos al destino, encontramos una ruta.
    if origen == destino:
        return [([destino], 0)]

    rutas = []

    # Obtener las estaciones conectadas.
    vecinos = obtener_conexiones(origen)

    for vecino, tiempo in vecinos:

        # Solo continuar si no hemos visitado esa estación.
        if vecino not in visitadas:

            rutas_encontradas = encontrar_rutas(
                vecino,
                destino,
                visitadas
            )

            # Agregar el origen y sumar el tiempo.
            for ruta, tiempo_total in rutas_encontradas:

                nueva_ruta = [origen] + ruta
                nuevo_tiempo = tiempo + tiempo_total

                rutas.append(
                    (nueva_ruta, nuevo_tiempo)
                )

    return rutas


# ------------------------------------------------------------
# 4. SELECCIONAR LA MEJOR RUTA
# ------------------------------------------------------------

def mejor_ruta(origen, destino):

    rutas = encontrar_rutas(origen, destino)

    if not rutas:
        return None, None

    # Selecciona la ruta con menor tiempo.
    ruta, tiempo = min(
        rutas,
        key=lambda x: x[1]
    )

    return ruta, tiempo


# ------------------------------------------------------------
# 5. INTERFAZ DEL SISTEMA
# ------------------------------------------------------------

print("============================================")
print("   SISTEMA INTELIGENTE DE TRANSPORTE")
print("============================================")

print("\nEstaciones disponibles:")

estaciones = set()

for origen, destino, tiempo in conexiones:
    estaciones.add(origen)
    estaciones.add(destino)

for estacion in sorted(estaciones):
    print("-", estacion)


# ------------------------------------------------------------
# 6. ENTRADA DEL USUARIO
# ------------------------------------------------------------

origen = input("\nIngrese el punto A: ")
destino = input("Ingrese el punto B: ")


# ------------------------------------------------------------
# 7. VALIDACIÓN
# ------------------------------------------------------------

if origen not in estaciones:

    print("\nEl punto A no existe en la base de conocimiento.")

elif destino not in estaciones:

    print("\nEl punto B no existe en la base de conocimiento.")

else:

    # El sistema realiza la inferencia.
    ruta, tiempo = mejor_ruta(origen, destino)

    if ruta is None:

        print("\nNo existe una ruta entre los puntos seleccionados.")

    else:

        print("\n============================================")
        print("              RESULTADO")
        print("============================================")

        print("\nMejor ruta encontrada:")

        print(" -> ".join(ruta))

        print("\nTiempo estimado:", tiempo, "minutos")