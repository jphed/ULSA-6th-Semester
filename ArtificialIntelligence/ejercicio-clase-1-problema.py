# Grafo representado como lista de adyacencia
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# DFS: Recorrido en profundidad
def dfs(graph, start):
    visited = set()   # Conjunto de nodos visitados
    stack = [start]   # Pila para DFS
    
    while stack:
        # TODO: Extraer el nodo de la pila.
 
        
        # TODO: Verificar si el nodo ya ha sido visitado.
 
            # TODO: Marcar el nodo como visitado.

            
            # TODO: Agregar a la pila los vecinos del nodo que aún no han sido visitados.
            # Nota: Puedes invertir la lista de vecinos para controlar el orden del recorrido.
   
# BFS: Recorrido en anchura
def bfs(graph, start):
    visited = set()   # Conjunto de nodos visitados
    queue = [start]   # Cola para BFS (utilizaremos una lista y el método pop(0) para simular una cola)
    
    while queue:
        # TODO: Extraer el primer nodo de la cola.
    
        
        # TODO: Verificar si el nodo ya ha sido visitado.
     
            # TODO: Marcar el nodo como visitado.

            
            # TODO: Agregar a la cola los vecinos del nodo que aún no han sido visitados.
 
# Ejemplo de uso
print("DFS desde nodo 'A':")
dfs(graph, 'A')
print("\nBFS desde nodo 'A':")
bfs(graph, 'A')