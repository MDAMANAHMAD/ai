import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {'G': 1},
    'E': {'G': 2},
    'F': {'G': 5},
    'G': {}
}

h = {
    'A': 7, 'B': 6, 'C': 5, 'D': 3, 'E': 4, 'F': 6, 'G': 0
}

def astar(start, goal):
    q = [(h[start], 0, start, [])]
    visited = set()

    while q:
        f, g, n, path = heapq.heappop(q)

        if n in visited:
            continue
        visited.add(n)

        path = path + [n]

        if n == goal:
            print("Path:", '->'.join(path), "\nCost:", g)
            return

        for nbr, cost in graph[n].items():
            if nbr not in visited:
                heapq.heappush(q, (g + cost + h[nbr], g + cost, nbr, path))

    print("No path found.")
astar('A', 'G')
