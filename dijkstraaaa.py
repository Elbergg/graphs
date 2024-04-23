def dijkstra(G, start, end):
    start.color = "gray"
    queue = [start]
    start.distance = 0
    end_adj = []
    for element in G.adj:
        """
        el stupido loopo resposible for checking collecting
        all nodes that lead to the end node
        so we can check if they all have been marked as black later
        there has to be a better way to do this
        """
        adjecencies = G.adj[element]
        for edge in adjecencies:
            if end in edge:
                end_adj.append(element)
    while queue != []:
        u = queue[0]
        if u.color != "black":
            adjecencies = G.adj[u]  ###get
            all_black = True
            for node in end_adj:
                """
                checks if all paths to the end have been checked
                -> they are all black,
                if so, return
                """
                if node.color != "black":
                    all_black = False
                    break
            if all_black:
                return

            for element in adjecencies:
                node = element[0]
                weight = element[1]
                if node.distance is not None:
                    if weight + u.distance < node.distance:
                        node.color == "gray"
                        node.parent = u
                        node.distance = weight + u.distance
                        queue.append(node)
                else:
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
