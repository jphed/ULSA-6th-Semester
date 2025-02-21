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
        # Extraer el nodo de la pila.
        node = stack.pop()
        
        # Verificar si el nodo ya ha sido visitado.
        if node not in visited:
            # Marcar el nodo como visitado.
            print(node, end=" ")
            visited.add(node)
            
            # Agregar a la pila los vecinos del nodo que aún no han sido visitados.
            # Nota: Puedes invertir la lista de vecinos para controlar el orden del recorrido.
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# BFS: Recorrido en anchura
def bfs(graph, start):
    visited = set()   # Conjunto de nodos visitados
    queue = [start]   # Cola para BFS (utilizaremos una lista y el método pop(0) para simular una cola)
    
    while queue:
        # Extraer el primer nodo de la cola.
        node = queue.pop(0)
        
        # Verificar si el nodo ya ha sido visitado.
        if node not in visited:
            # Marcar el nodo como visitado.
            print(node, end=" ")
            visited.add(node)
            
            # Agregar a la cola los vecinos del nodo que aún no han sido visitados.
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Ejemplo de uso
print("DFS desde nodo 'A':")
dfs(graph, 'A')
print("\nBFS desde nodo 'A':")
bfs(graph, 'A')