# Actividad 2 — Búsqueda y sistemas basados en reglas

Sistema inteligente de rutas para un transporte masivo. Recibe un origen y un destino, recorre la base de conocimiento de estaciones y elige la ruta de menor tiempo.

Curso: Inteligencia Artificial — Corporación Universitaria Iberoamericana.

## Contenido del repositorio

| Archivo | Descripción |
| --- | --- |
| `Ruta logica.py` | Programa principal: hechos, reglas, motor de inferencia e interfaz por consola |
| `Estructura de estaciones.jpeg` | Grafo de estaciones y tiempos de viaje (minutos) |
| `Actividad 2 - Búsqueda y sistemas basados en reglas.pdf` | Entrega en PDF |
| `Actividad 2 - Búsqueda y sistemas basados en reglas.docx` | Entrega en Word |

## Requisitos

- Python 3 (no hay dependencias externas)

## Cómo ejecutarlo

Desde la carpeta del proyecto:

```bash
python "Ruta logica.py"
```

El programa lista las estaciones, pide el **punto A** y el **punto B**, valida que existan y muestra la mejor ruta.

Nombres válidos (tal como están en la base de conocimiento):

- `Estacion 1` … `Estacion 8`

Ejemplo de uso:

```
Ingrese el punto A: Estacion 1
Ingrese el punto B: Estacion 8
```

Salida esperada (ruta de menor tiempo):

```
Mejor ruta encontrada:
Estacion 1 -> Estacion 3 -> Estacion 4 -> Estacion 5 -> Estacion 6 -> Estacion 8

Tiempo estimado: 35 minutos
```

Si el origen o el destino no están en la base, o no hay camino entre ellos, el programa lo indica.

## Red de estaciones

El grafo de `Estructura de estaciones.jpeg` se modela como conexiones no dirigidas con un costo en minutos:

| Conexión | Tiempo (min) |
| --- | ---: |
| Estación 1 — Estación 2 | 5 |
| Estación 1 — Estación 3 | 8 |
| Estación 2 — Estación 3 | 4 |
| Estación 3 — Estación 4 | 5 |
| Estación 4 — Estación 5 | 6 |
| Estación 4 — Estación 7 | 7 |
| Estación 5 — Estación 6 | 4 |
| Estación 6 — Estación 7 | 10 |
| Estación 6 — Estación 8 | 12 |
| Estación 7 — Estación 8 | 15 |

La estación 8 es el nodo de doble círculo en el diagrama (destino típico del recorrido).

## Cómo está construido el sistema

El código sigue la estructura clásica de un **sistema basado en reglas**:

1. **Base de conocimiento (hechos)**  
   Lista `conexiones`: tripletas `(origen, destino, tiempo)` que representan tramos directos.

2. **Reglas**  
   - `obtener_conexiones(estacion)`: si hay un hecho que une esa estación con otra, esa conexión se puede usar (en ambos sentidos).  
   - `existe_conexion(origen, destino)`: si dos estaciones aparecen juntas en un hecho, es posible desplazarse entre ellas.

3. **Motor de inferencia**  
   `encontrar_rutas` aplica las reglas de forma recursiva: parte del origen, expande vecinos no visitados y acumula caminos hasta el destino. Evita ciclos con un conjunto de estaciones ya visitadas. Devuelve **todas** las rutas acíclicas posibles con su tiempo total.

4. **Selección de la solución**  
   `mejor_ruta` elige la ruta cuyo tiempo acumulado es mínimo.

5. **Interfaz**  
   Consola: listado de estaciones, lectura de A y B, validación e impresión del resultado.

## Enfoque de búsqueda

No se usa una librería de grafos. La búsqueda es un recorrido en profundidad que enumera caminos simples y luego minimiza el costo. Con una red pequeña (8 estaciones) es suficiente y deja visible cómo las reglas generan las rutas a partir de los hechos.

## Autor

Damián Felipe Bernal Rodriguez — Ingeniería de software.
