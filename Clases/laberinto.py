def solve_maze_backtracking(maze, x, y, end, path, visited):
    if (x, y) == end:
        path.append((x, y))
        return True
    
    if (x, y) in visited or maze[x][y] == 1:
        return False
    
    visited.add((x, y))
    path.append((x, y))
    
    directions = [(0,1), (1,0), (0,-1), (-1,0)] # Derecha, Abajo, Izquierda, Arriba
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
            if solve_maze_backtracking(maze, nx, ny, end, path, visited):
                return True
    
    path.pop()
    return False

# Ejemplo de laberinto (0 = camino, 1 = pared)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)
path = []
visited = set()

if solve_maze_backtracking(maze, start[0], start[1], end, path, visited):
    print("¡Laberinto resuelto!")
    print("Ruta:", path)
else:
    print("No hay solución para el laberinto")