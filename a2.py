g = [
    [1, 2],
    [0, 3, 4],
    [0, 4],
    [1],
    [1, 2]
]

def bfs(s):
    print("BFS Traversal:")
    q, v = [s], {s}
    while q:
        n = q.pop(0)
        print(n, end=" ")
        for x in g[n]:
            if x not in v:
                v.add(x)
                q.append(x)
    print()

def dfs(n, v=set()):
    if n in v: return
    print(n, end=" ")
    v.add(n)
    for x in g[n]: dfs(x, v)

bfs(0)
print("DFS Traversal:")
dfs(0)
