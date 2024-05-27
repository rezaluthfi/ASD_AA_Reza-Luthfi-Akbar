def dijkstra(graph, n, start):
    distances = {i: [float('inf'), 0] for i in range(1, n + 1)}
    visited = {i: False for i in range(1, n + 1)}
    distances[start] = [0, start]

    for _ in range(n):
        min_distance = float('inf')
        min_vertex = -1
        for vertex in distances:
            if not visited[vertex] and distances[vertex][0] < min_distance:
                min_distance = distances[vertex][0]
                min_vertex = vertex
        
        if min_vertex == -1:
            break

        visited[min_vertex] = True

        for neighbor, weight in graph[min_vertex]:
            new_distance = min_distance + weight
            if new_distance < distances[neighbor][0]:
                distances[neighbor] = [new_distance, min_vertex]
    
    return distances

def dfs(graph, start, target_distance):
    stack = [(start, 0, [start], {start})]

    while stack:
        current_node, current_distance, path, visited = stack.pop()
        if current_distance == target_distance:
            return path
        
        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                new_distance = current_distance + weight
                if new_distance <= target_distance:
                    stack.append((neighbor, new_distance, path + [neighbor], visited | {neighbor}))
    
    return None

def bfs(graph, n, start):
    distances = {i: [-1, 0] for i in range(1, n + 1)}
    visited = {i: False for i in range(1, n + 1)}
    distances[start] = [0, start]
    visited[start] = True
    queue = [start]

    while queue:
        current = queue.pop(0)
        for neighbor, weight in graph[current]:
            if not visited[neighbor]:
                queue.append(neighbor)
                distances[neighbor] = [distances[current][0] + 1, current]
                visited[neighbor] = True
    
    return distances

data = []
with open('data.txt', 'r') as file:
    for line in file:
        data.append(list(map(int, line.split())))

n, m, s = data[0][0], data[0][1], data[-1][0]
data = data[1:-1]

graph = {i: [] for i in range(1, n + 1)}
for x, y, z in data:
    graph[x].append((y, z))
    graph[y].append((x, z))

#Nomor 1
distances_no1 = dijkstra(graph, n, s)
longest_no1 = max(distances_no1, key=lambda k: distances_no1[k][0])
print(f"Vertex yang memiliki jarak terpendek tertinggi dari {s} yaitu {longest_no1} dengan jarak {distances_no1[longest_no1][0]}")
print()

#Nomor 2
target_distance = 2024
path_no2 = dfs(graph, s, target_distance)
if path_no2:
    print(f"Terdapat vertex yang berjarak {target_distance} dari {s}, yaitu {path_no2[-1]} dengan path: {' -> '.join(map(str, path_no2))}")
else:
    print(f"Tidak ada vertex yang berjarak {target_distance} dari {s}")
print()

#Nomor 3
distances_no3 = bfs(graph, n, s)
longest_distance = max(distances_no3.values(), key=lambda item: item[0])[0]
long_vertices = [v for v, d in distances_no3.items() if d[0] == longest_distance]
print(f"Jarak terjauh dari vertex {s} yaitu {longest_distance} sebanyak {len(long_vertices)}, sebagai berikut:")
print(long_vertices)
