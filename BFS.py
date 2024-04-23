def bfs(G, s):
    for element in G.adj:
        element.color = "white"
        element.parent = None
        element.distance = 0
    queue = [s]
    s.color = "gray"
    while len(queue) != 0:
        u = queue[0]
        adjecents = G.adj[u]
        for a in adjecents:
            v = a[0]
            if v.color == "white":
                v.color = "gray"
                v.distance = u.distance + 1
                v.parent = u
                queue.append(v)
        queue.pop(0)
        u.color = "black"
