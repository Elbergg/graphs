def dfs(G):
    time = 0

    def dfs_visit(G, u):
        nonlocal time
        time += 1
        u.distance = time
        u.color = "gray"
        adjecents = G.adj[u]
        for a in adjecents:
            v = a[0]
            if v.color == "white":
                v.parent = u
                dfs_visit(G, v)
        u.color = "black"
        time += 1
        u.f = time

    for element in G.adj:
        element.color = "white"
        element.parent = None

    for element in G.adj:
        if element.color == "white":
            dfs_visit(G, element)
