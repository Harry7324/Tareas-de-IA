
# Problema de Cotidianidad: Encontrar el camino más corto en un supermercado

## Contexto  
Eres un cliente en un supermercado y tienes una lista de compras con varios productos que se encuentran en diferentes secciones del lugar. 
El supermercado tiene un diseño con pasillos que conectan las distintas secciones, y algunos caminos pueden ser más largos o estar bloqueados.

## Objetivo  
Encontrar el recorrido óptimo para visitar todas las secciones necesarias y minimizar el tiempo total de compras.

## Algoritmos aplicables  

1. **Búsqueda en amplitud (Breadth-First Search)**  
   - Útil si todos los caminos tienen el mismo costo. Encuentra el camino más corto en términos de pasos.

2. **Búsqueda uniforme en costo (Uniform Cost Search)**  
   - Ideal para este problema si las distancias entre secciones varían, ya que garantiza encontrar el camino de menor costo acumulado.

3. **Búsqueda A***  
   - Si disponemos de un mapa del supermercado y una heurística (por ejemplo, la distancia en línea recta a la siguiente sección), este algoritmo puede acelerar la búsqueda.

4. **Búsqueda voraz (Greedy Best-First Search)**  
   - Puede ser útil si queremos aproximarnos rápidamente a las secciones más cercanas, aunque no garantiza encontrar el camino óptimo.

---
Este problema modela una situación común y puede ampliarse para incluir múltiples factores, como restricciones de tiempo o preferencias de orden.
