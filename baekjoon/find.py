def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

a,b,c = map(int,input().split())
road = [[] for i in range(a)]
for i in range(a):
    v,k=input().split()
    road[v]
    
graph = {}

dfs(graph, 'A')