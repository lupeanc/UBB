
import random

from graph import Graph, readFile, readFile1k, readFile10k
from DFS import *
from texttable import Texttable

class UI:
    def __init__(self, graph):
        self.sortedDAG = None
        self._graph = graph

    @staticmethod
    def printMenu():
        print('Graph Operations')
        print('1. Get the number of vertices')
        print('2. The set of vertices')
        print('3. Check if there is an edge between 2 vertices')
        print('4. In degree of a vertex')
        print('5. Out degree of a vertex')
        print('6. The outbound edges of a vertex')
        print('7. The inbound edges of a vertex')
        print('8. Get the cost of an edge')
        print('9. Modify the cost of an edge')
        print('10. Add edge')
        print('11. Remove edge')
        print('12. Add vertex')
        print('13. Remove vertex')
        print('14. Save graph to file')
        print('15. Display Graph')
        print('16. Connected Components')
        print('17. Lowest cost walk')
        print('18. Topological sort')
        print('19. Earliest and latest starting time + total time')
        print('20. Get critical activities')
        print('0. Exit')

    def nrVert(self):
        print(self._graph.nrVertices())

    def setVert(self):
        r = []
        for i in self._graph.setOfVertices():
            r.append(int(i))
        print(r)

    def checkEdge(self):
        x = int(input('Vertex 1: '))
        y = int(input('Vertex 2: '))
        print(self._graph.isEdge(x, y))

    def inDeg(self):
        x = int(input('Vertex: '))
        print(self._graph.inDeg(x))

    def outDeg(self):
        x = int(input('Vertex: '))
        print(self._graph.outDeg(x))

    def outEdges(self):
        x = int(input('Vertex: '))
        r = ''
        for i in self._graph.outboundEdge(x):
            r += str(i) + ' '
        print(r)

    def inEdges(self):
        x = int(input('Vertex: '))
        r = ''
        for i in self._graph.inboundEdge(x):
            r += str(i) + ' '
        print(r)

    def edgeCost(self):
        x = int(input('Vertex 1: '))
        y = int(input('Vertex 2: '))
        print(self._graph.getCost(x, y))

    def changeEdge(self):
        x = int(input('Vertex 1: '))
        y = int(input('Vertex 2: '))
        val = int(input('Value: '))
        self._graph.changeCost(x, y, val)

    def addEdge(self):
        x = int(input('Vertex 1: '))
        y = int(input('Vertex 2: '))
        val = int(input('Cost: '))
        self._graph.addEdge(x, y, val)

    def removeEdge(self):
        x = int(input('Vertex 1: '))
        y = int(input('Vertex 2: '))
        self._graph.removeEdge(x, y)

    def addVertex(self):
        x = int(input('Vertex: '))
        self._graph.addVertex(x)

    def removeVertex(self):
        x = int(input('Vertex: '))
        self._graph.removeVertex(x)

    def copyGraph(self):
        file = input('File name: ')
        f = open(file, 'w')
        g = self._graph.copyGraph()
        f.write(str(g.nrVertices()) + ' ' + str(g.nrEdges()) + '\n')
        f.write(str(g))

    def getConnectedComponents(self):
        list_of_components = getConnectedComponents(self._graph)
        i = 1
        for graph_iterator in list_of_components:
            print()
            print("Component ", i)

            for vertex in graph_iterator.dictOut.keys():

                print("Vertex ", vertex)

            list_of_edges = []

            for vertex in graph_iterator.dictOut.keys():
                for node in graph_iterator.dictOut[vertex]:
                    list_of_edges.append((vertex, node))

            #removes reversed edges
            for edge in list_of_edges:
                if (edge[1], edge[0]) in list_of_edges:
                    list_of_edges.remove((edge[1], edge[0]))

            for edge in list_of_edges:
                print("Edge: ", edge[0], " ", edge[1])

            i = i + 1

        print()

    def lowestCostWalk(self):
        start = int(input('Vertex 1: '))
        end = int(input('Vertex 2: '))

        # Checks if the inserted vertices have negative cost cycles
        if self._graph.checkNegCostCycle(start) or self._graph.checkNegCostCycle(end):
            print("There are negative cost cycles")
            print()
            return

        cost = self._graph.costWalkByLength(start, end)
        #if cost[0](cost) is -99999999 and cost[1](path) is empty, there was a neg cost cycle
        # print(cost[1], cost[0])
        if cost[1] == []:
            print("There are negative cost cycles")
            print()
            return
        if cost[0]>=99999999:
            print("There is no path between the 2 vertices")
        else:

            print("Lowest cost walk: ", cost[0])

        print()


    def performDAG(self):
        sortedDAG = self._graph.DAG()
        if sortedDAG != []:
            print(sortedDAG)
            self.sortedDAG = sortedDAG
            print("Done computing topological sorting with dfs.")
        else:
            print("Graph is not DAG")

    def earliest_and_latest_times(self):
        earliest_start, earliest_end, latest_start, latest_end, duration = self._graph.get_times()

        if duration == -1:
            print("The graph is not a DAG.")
        else:
            from texttable import Texttable
            t = Texttable()
            table_list = list()
            table_list.append(['Activity', 'Earliest Time', 'Latest Time'])

            for i in range(self._graph.nrVertices()):
                table_list.append([str(i), str(earliest_start[i]) + "-" + str(earliest_end[i]),
                                   str(abs(latest_start[i])) + "-" + str(abs(latest_end[i]))])

            t.add_rows(table_list)
            print(t.draw())
            print("The duration of the project is:" + str(duration))

    def criticalactivities(self):
        critical = self._graph.critical_activities()
        if not critical:
            print("The graph is not a DAG.")
        else:
            print("The critical activities are:")
            for activity in critical:
                if activity == critical[-1]:
                    print(activity)
                else:
                    print(activity, end=", ")

    def greedyVertexCover(self):
        print("The vertices forming the approximate minimum vertex cover are:")
        print(self._graph.greedyVertexCover())

    def start(self):
        d = {
            '1': self.nrVert,
            '2': self.setVert,
            '3': self.checkEdge,
            '4': self.inDeg,
            '5': self.outDeg,
            '6': self.outEdges,
            '7': self.inEdges,
            '8': self.edgeCost,
            '9': self.changeEdge,
            '10': self.addEdge,
            '11': self.removeEdge,
            '12': self.addVertex,
            '13': self.removeVertex,
            '14': self.copyGraph,
            '16': self.getConnectedComponents,
            '17': self.lowestCostWalk,
            '18': self.performDAG,
            '19': self.earliest_and_latest_times,
            '20': self.criticalactivities,
        }
        print()
        while True:
            self.printMenu()
            cmd = input('Command: ')
            if cmd == '0':
                return 0
            elif cmd == '15':
                print(str(self._graph))
                # print("tryout")
                # print(str(makeUndirected(self._graph)))
            elif cmd in d.keys():
                d[cmd]()
            else:
                print('Invalid command')


def generateGraph():
    nrV = int(input('Nr Vertices: '))
    nrE = int(input('Nr Edges: '))
    if nrE>nrV*nrV:
        raise ValueError("Too many edges")
    aux = []
    G = Graph(nrV)
    for i in G.setOfVertices():
        aux.append(int(i))
    i = 0
    while i < nrE:
        tpl = (random.choice(aux), random.choice(aux), random.choice(list(range(-100, 100))))
        if G.isEdge(tpl[0], tpl[1]):
            continue
        G.addEdge(tpl[0], tpl[1], tpl[2])

        i -= -1

    return G

def read():
    print('Read graph from memory or generate? 1 - read, 2 - generate')
    cmd = input('Choice: ')
    if cmd == '2':
        g = generateGraph()
    elif cmd == '1':
        print("How many nodes?")
        print("1. Small graph - reads user input ")
        print("2. Medium graph - 1k")
        print("3. Large graph - 10k")
        print("4. Activity graph")
        graph_type = input(">")

        if graph_type == '1':
            while (1):
                try:
                    file_name = input("File Name: ")
                    g = readFile(file_name)
                    break
                except FileNotFoundError as fnf:
                    print(fnf)

        elif graph_type == '2':
            g = readFile1k()
        elif graph_type == '3':
            g = readFile10k()
        elif graph_type == '4':
            g = read_activities()
            # g = activityFile()
        else:
            raise ValueError("Invalid Option")
    else:
        print('Invalid')
        return
    return g

if __name__ == "__main__":
    g = read()
    u = UI(g)
    u.start()
