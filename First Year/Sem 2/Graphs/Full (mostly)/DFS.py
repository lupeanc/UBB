from graph import *

def makeUndirected(graph):
    """
    Makes graph undirected by adding a 'reversed' edge to all existing edges
    :param graph: the current directed graph
    :return: new undirected graph
    """
    new_graph = graph.copyGraph()
    for vertexStart in new_graph.setOfVertices():
        for vertexEnd in new_graph.dictOut[vertexStart]:
            if not new_graph.isEdge(vertexEnd, vertexStart):
                new_graph.addEdge(vertexEnd, vertexStart, new_graph.getCost(vertexStart, vertexEnd))

    return new_graph

def DFS(graph, firstVertex):
    """
    Finds a connected component starting with a given vertex.
    It searches the graph using the depth-first search algorithm:
    Adds the start vertex to the visited list -> adds all its outbounds to the queue ->
    -> It pops the first elem of the queue, and it repeats the process until the queue is empty
    :param graph: the undirected graph
    :param firstVertex: starting vertex
    :return: visited set = set of the connected component
    """
    visited = set()
    queue = [firstVertex]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            for node in graph.dictOut[vertex]:
                queue.append(node)
    return visited

def findConnectedComponents(graph):
    """
    finds the components using the undirected version of the graph
    :param graph: undirected version of the graph
    :return: the components
    """
    visited = set()
    components = []
    for vertex in graph.setOfVertices():
        if vertex not in visited:
            visited.add(vertex)
            component = DFS(graph, vertex)
            visited = visited.union(component)
            components.append(component)
    return components

def makeConnectedComponentsGraphs(components, original_graph):
    """
    Creates 'mini-graphs' for every component so they can be printed out
    :param components: current components
    :param original_graph: the original graph with all the components
    :return:
    """
    graphs = []
    for component in components:
        graph = Graph(0)
        for vertex in component:
            graph.addVertex(vertex)


        for vertex in component:
            for node in original_graph.dictOut[vertex]:
                if node in component:
                    graph.addEdge(vertex, node, original_graph.getCost(vertex, node))

        graphs.append(graph)

    return graphs

def getConnectedComponents(graph):
    """
    gets the components using the functions above
    :param graph: graph we want to get the components of
    :return:
    """
    undirectedGraph = makeUndirected(graph)
    components = findConnectedComponents(undirectedGraph)
    graphs = makeConnectedComponentsGraphs(components, undirectedGraph)

    return graphs