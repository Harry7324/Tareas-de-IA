
# Algoritmos de Búsqueda en AIMA (Capítulos 4, 5 y 6)

## Capítulo 4: Algoritmos de búsqueda no informada
Estos algoritmos no utilizan conocimiento adicional sobre el problema más allá de su definición:

1. **Búsqueda en amplitud (Breadth-First Search)**  
   - **Inspiración**: Está inspirado en explorar todos los nodos de un nivel antes de pasar al siguiente, asegurando encontrar la solución más corta en términos de pasos.  
   - **Clasificación**: Completa y óptima si todos los costos de paso son iguales.

2. **Búsqueda en profundidad (Depth-First Search)**  
   - **Inspiración**: Explora tan profundamente como sea posible en una rama antes de retroceder, imitando un enfoque exploratorio exhaustivo.  
   - **Clasificación**: No completa ni óptima en general.

3. **Búsqueda de profundidad limitada (Depth-Limited Search)**  
   - **Inspiración**: Combina la búsqueda en profundidad con un límite explícito para evitar bucles infinitos o explorar demasiado lejos.  
   - **Clasificación**: No completa ni óptima, pero más eficiente en memoria.

4. **Búsqueda iterativa en profundidad (Iterative Deepening Search)**  
   - **Inspiración**: Integra la búsqueda en amplitud y en profundidad, incrementando gradualmente el límite de profundidad.  
   - **Clasificación**: Completa y óptima si los costos de paso son iguales.

5. **Búsqueda uniforme en costo (Uniform Cost Search)**  
   - **Inspiración**: Prioriza los caminos de menor costo acumulado, modelando decisiones basadas en economía de recursos.  
   - **Clasificación**: Completa y óptima.

## Capítulo 5: Búsqueda informada (heurística)
Estos algoritmos aprovechan una función heurística para guiar la búsqueda hacia la solución más prometedora.

1. **Búsqueda voraz (Greedy Best-First Search)**  
   - **Inspiración**: Se inspira en la estrategia de ir directamente hacia el objetivo más cercano según la heurística, imitando el comportamiento de búsqueda eficiente en humanos.  
   - **Clasificación**: No completa ni óptima en general.

2. **Búsqueda A***  
   - **Inspiración**: Combina el costo acumulado con una estimación heurística, buscando soluciones más rápidas y eficientes mediante balance de exploración y optimización.  
   - **Clasificación**: Completa y óptima si la heurística es admisible (subestima el costo real).

3. **Búsqueda con reducción de memoria (Iterative Deepening A* o IDA*)**  
   - **Inspiración**: Aplica límites crecientes sobre el costo estimado total, aprovechando técnicas de búsqueda iterativa con memoria optimizada.  
   - **Clasificación**: Completa y óptima.

## Capítulo 6: Búsqueda en juegos (adversarial)
Explora algoritmos diseñados para entornos donde hay un oponente activo.

1. **Minimax**  
   - **Inspiración**: Evalúa todos los movimientos posibles asumiendo que el oponente jugará de manera óptima, buscando maximizar la ganancia mínima.  
   - **Clasificación**: Exacto para juegos de suma cero con información perfecta.

2. **Alpha-Beta Pruning**  
   - **Inspiración**: Mejora el Minimax eliminando ramas que no afectan el resultado final, optimizando recursos de cálculo.  
   - **Clasificación**: Completo y óptimo, con mejor eficiencia en tiempo.