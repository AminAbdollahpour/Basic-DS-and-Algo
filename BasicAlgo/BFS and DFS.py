def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
    return visited


def dfs(graph,start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop(0)
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
    return visited
