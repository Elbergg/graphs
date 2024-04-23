def dijkstra(G, start, end):
    start.color = "gray"
    queue = [start]
    start.distance = 0
    while queue != []:
        u = queue[0]
        if u == end:
            break
        if u.color != "black":
            adjecencies = G.adj[u]
            for element in adjecencies:
                node = element[0]
                weight = element[1]
                if node.distance is not None:
                    """
                    check if going through the parent is faster
                    than the current route to node
                    """
                    if weight + u.distance < node.distance:
                        node.color == "gray"
                        node.parent = u
                        node.distance = weight + u.distance
                        queue.append(node)
                else:
                    """
                    route to node not yet defined
                    """
                    node.distance = weight + u.distance
                    node.color == "gray"
                    queue.append(node)
                    node.parent = u
            queue.sort(key=lambda x: x.distance)
            queue.pop(0)
            u.color = "black"
        else:
            queue.pop(0)
    return
