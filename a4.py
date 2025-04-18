from heapq import heappop, heappush
def astar(grid, start, goal):
    H = lambda x, y: abs(goal[0]-x)+abs(goal[1]-y)
    open, visited = [(H(*start), 0, start, [])], set()
    while open:
        _, cost, (x, y), path = heappop(open)
        if (x, y) in visited: continue
        path = path + [(x, y)]
        if (x, y) == goal: return path
        visited.add((x, y))
        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and not grid[nx][ny]:
                heappush(open, (cost+1+H(nx, ny), cost+1, (nx, ny), path))
grid = [[0,0,0,0],[1,1,0,1],[0,0,0,0],[0,1,1,0]]
path = astar(grid, (0,0), (3,3))
print(path)
