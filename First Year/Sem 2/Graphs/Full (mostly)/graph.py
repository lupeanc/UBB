import math
from collections import deque
from copy import deepcopy
from random import choice


class Graph:
    def __init__(self, n):
        self.dictIn = {}
        self.dictOut = {}
        self.dictCost = {}

        self.dictEdges = {}
        for i in range(0, n):
            self.dictEdges[i] = []
        self.E = []

        for i in range(n):
            self.dictIn[i] = []
            self.dictOut[i] = []

        self.__duration = [] * self.nrVertices()  # the duration of activity i
        self.__earliest_start = [-999999] * self.nrVertices()  # the earliest time when activity i begins
        self.__earliest_end = [-999999] * self.nrVertices() # the earliest time when activity i ends
        self.__latest_start = [999999] * self.nrVertices()  # the time at the latest when activity i begins
        self.__latest_end = [999999] * self.nrVertices()  # the time at the latest when activity i ends

    def setOfVertices(self):
        """
        :return: the set of vertices
        """
        return iter(self.dictOut.keys())

# CHECK IF V IS ... FUNCTIONS ------------------------------------------------------------------------------------------
    def isVertex(self, val):
        """
        Checks if val is vertex by checking if there's any other nodes going into it
        :param val: val of vertex we want to check
        :return: true if val is a vertex, false if otherwise
        """
        if val in self.dictOut.keys():
            return True
        return False

    def isEdge(self, Vstart, Vend):
        """
        Checks if there is an edge between Vstart and Vend by checking if Vend is one of the vertexes Vstart points to
        :param Vstart: base vertex
        :param Vend: end vertex
        :return: true of there is an edge, false if otherwise
        """
        if Vend in self.dictOut[Vstart]:
            return True
        return False

# NUMBER OF ... FUNCTIONS ----------------------------------------------------------------------------------------------
    def nrVertices(self):
        """
        returns the number of vertices
        :return:
        """
        return len(self.dictIn)

    def nrEdges(self):
        """
        :return: the number of edges
        """
        return len(self.dictCost.keys())

# DEGREES --------------------------------------------------------------------------------------------------------------
    def inDeg(self, n):
        """
        :param n: vertex
        :return: the number of in vertices
        """
        return len(self.dictIn[n])

    def outDeg(self, n):
        """
        :param n: vertex
        :return: the number of out degrees
        """
        return len(self.dictOut[n])

# INBOUND / OUTBOUND EDGES
    def inboundEdge(self, n):
        """
        :param n: vertex
        :return: number of inbound edges
        """
        return iter(self.dictIn[n])

    def outboundEdge(self, n):
        """
                :param n: vertex
                :return: number of outbound edges
                """
        return iter(self.dictOut[n])

# ADD/REMOVE -----------------------------------------------------------------------------------------------------------

    # VETRICES
    def addVertex(self, val):
        """
        adds a vertex
        :param val: the value of the vertex
        :return:
        """
        if self.isVertex(val):
            raise ValueError("Vertex already exists")
        self.dictOut[val] = []
        self.dictIn[val] = []

    def addVertexNoErr(self, val):
        """
        adds a vertex
        :param val: the value of the vertex
        :return:
        """
        self.dictOut[val] = []
        self.dictIn[val] = []


    def removeVertex(self, vertex):
        """
        removes vertex
        :param vertex: the vertex to be removed
        :return:
        """
        for v in self.dictOut[vertex]:
            del self.dictCost[(vertex, v)]

            self.dictIn[v].remove(vertex)

        for v in self.dictIn[vertex]:
            del self.dictCost[(v, vertex)]

            self.dictOut[v].remove(vertex)

        del self.dictIn[vertex]
        del self.dictOut[vertex]


    # EDGES
    def addEdge(self, Vstart, Vend, cost = 0):
        """
        adds an edge
        :param Vstart: first vertex
        :param Vend: last vertex
        :param cost: the cost of the path
        :return:
        """
        if not self.isVertex(Vstart) or not self.isVertex(Vend):
            raise ValueError("Invalid vertex")
        if self.isEdge(Vstart, Vend):
            raise ValueError("Edge already exists")

        self.dictOut[Vstart].append(Vend)
        self.dictIn[Vend].append(Vstart)
        self.dictCost[(Vstart, Vend)] = cost

    def removeEdge(self, Vstart, Vend):
        """
        removes an edge
        :param Vstart: first vertex
        :param Vend: second vertex
        :return:
        """
        if not self.isVertex(Vstart) or not self.isVertex(Vend):
            raise ValueError("Invalid vertex")
        if not self.isEdge(Vstart, Vend):
            raise ValueError("Edge does not exist")

        for cost in self.dictCost.keys():
            if Vstart == cost[0] and Vend == cost[1]:
                del self.dictCost[cost]
                break

        self.dictIn[Vend].remove(Vstart)
        self.dictOut[Vstart].remove(Vend)

# COST -----------------------------------------------------------------------------------------------------------------
    def getCost(self, Vstart, Vend):
        """
        :param Vstart: first vertex
        :param Vend: last vertex
        :return: the cost
        :raises: error if the edge does not exist
        """
        if not self.isEdge(Vstart, Vend):
            raise ValueError("Edge does not exist\n")
        else:
            return self.dictCost[(Vstart, Vend)]

    def changeCost(self, Vstart, Vend, newVal):
        """
        cahnges the cost of an edge
        :param Vstart: first vertex
        :param Vend: second vertex
        :param newVal: new value for cost
        :return:
        """
        if not self.isEdge(Vstart, Vend):
            raise ValueError("Edge does not exist\n")
        else:
            self.dictCost[(Vstart, Vend)] = newVal

# COST WALK BY LENGTH

    def checkNegCostCycle(self, vertex):
        dist = [[0 for i in range(self.nrVertices() + 1)] for j in range(self.nrVertices() + 1)]
        n = self.nrVertices()
        for i in range(n):
            for j in range(n):
                if self.isEdge(i, j):
                    dist[i][j] = self.dictCost[(i, j)]
                else:
                    dist[i][j] = 99999999999

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        if dist[vertex][vertex] < 0:
            return True
        return False

# INFINITE CYCLE FROM 0 TO 3 OR 0 TO 1
# 8 10
# 0 1 4
# 1 2 3
# 2 1 -7
# 2 3 4
# 4 3 0
# 0 5 1
# 5 6 2
# 6 7 3
# 7 6 5
# 7 5 1

#NO INFINITE CYCLES + NO WALK TO VERTEX 4
# 5 10
# 0 3 1
# 0 1 20
# 1 0 5
# 1 2 3
# 1 3 40
# 2 1 30
# 2 3 8
# 3 2 10
# 3 1 2
# 3 0 3
    def costWalkByLength(self, start, end):
        n = self.nrVertices()
        walk = []
        for i in range(n + 1):
            walk.append([99999999999] * (n + 1))
        # print(walk)
        walk[start][0] = 0

        for k in range(n):
            for i in range(n):
                for v in self.dictOut[i]:
                    walk[v][k + 1] = min(walk[i][k] + self.dictCost[(i, v)], walk[v][k + 1])
                    # print("k: ", k)
                    # print("i: ", i)
                    # print("v: ", v)
                    # print(f"w[{v}][{k+1}]: ", walk[v][k + 1])
            # for elem in walk:
            #     print(elem)
            #     print()
                    # print(walk)
        # print(walk)

        #Building path
        cost = 99999999999
        nr = 0
        poz = 0
        for i in walk[end]:
            if i == cost:
                nr += 1
            elif i < cost:
                poz = walk[end].index(i)
                cost = i
                nr = 1
        x = end
        poz += 1
        path = [x]
        for k in reversed(range(n)):
            for y in range(n):
                if self.isEdge(y, x) and k == poz - 1 and walk[y][k] + self.dictCost[(y, x)] == walk[x][poz]:
                    # if there is a negative cost cycle on the vertex-to-be-added,
                    # return the "error tuple", (-1, []) where
                    # -99999999999 is cost (just to mark it as error),
                    # [] is path (no valid path found)
                    if self.checkNegCostCycle(y):
                        return -99999999999, []

                    path.append(y)
                    x = y
                    poz -= 1
        path.append(start)

        return cost, path

#TOPOLOGICAL SORT DFS-----------------------------------------------------------------------------------------------------------
    def set_duration(self, times):
        self.__duration = times

    def topologicalSortWithDFS(self, x, sorted, fullyProcessed, inProcess):
        #adds x (vertex) to the set inProcess and then goes through all of its inbound neighbours in order to sort them as well
        inProcess.add(x)
        for inboundNeighbour in self.inboundEdge(x):
            if inboundNeighbour in inProcess:
                return False
            else:
                if inboundNeighbour not in fullyProcessed:
                    ok = self.topologicalSortWithDFS(inboundNeighbour, sorted, fullyProcessed, inProcess)
                    if not ok:
                        print(sorted)
                        return False
        inProcess.remove(x)
        sorted.append(x)
        fullyProcessed.add(x)
        return True

    def DAG(self):
        #goes through the whole list of vertices and if it has not been processed yet, performs topo sort with dfs
        #returns a copy of the sorted list if the topo sort can be done
        #empty list if not -> graph is not a dag
        sorted = []
        fullyProcessed = set()
        inProcess = set()
        for vertex in self.setOfVertices():
            if vertex not in fullyProcessed:
                ok = self.topologicalSortWithDFS(vertex, sorted, fullyProcessed, inProcess)
                if not ok:
                    return []
        return sorted[:]

    def get_times(self):
        """
        Finds the earliest and the latest starting time for each activity and the total time of the project.
        Firstly, we topologically sort the graph associated to the list of activities and for each activity, we check
        what is the maximum earliest end date for one of its predecessors and that will be the earliest start date of
        the current activity. If the activity has no predecessors, its earliest start time is 0. Finally, knowing the
        duration, we can compute the earliest end time. We proceed similarly for the latest start/end time.
        Runtime: O(V+E), where V is the number of vertices and E the number of edges in the graph
        :return: -1 5 times, if the graph is a DAG
                 5 integers (the earliest start time, the earliest end time, the latest start time, the latest end time and the
                 total duration of the project), otherwise
        """
        sorted_vertices = self.DAG()
        self.__earliest_start = [-999999] * self.nrVertices()
        self.__earliest_end = [-999999] * self.nrVertices()
        self.__latest_start = [999999] * self.nrVertices()
        self.__latest_end = [999999] * self.nrVertices()

        for vertex in sorted_vertices:
            if self.inDeg(vertex) == 0:
                self.__earliest_start[vertex] = 0
            else:
                for neighbour in self.inboundEdge(vertex):
                    self.__earliest_start[vertex] = max(self.__earliest_start[vertex], self.__earliest_end[neighbour])
            self.__earliest_end[vertex] = self.__earliest_start[vertex] + self.__duration[vertex]

        sorted_vertices.reverse()
        for vertex in sorted_vertices:
            if self.outDeg(vertex) == 0:
                self.__latest_end[vertex] = self.__earliest_end[sorted_vertices[0]]
            for neighbour in self.outboundEdge(vertex):
                self.__latest_end[vertex] = min(self.__latest_end[vertex], self.__latest_start[neighbour])
            self.__latest_start[vertex] = self.__latest_end[vertex] - self.__duration[vertex]

        if not sorted_vertices:
            return -1, -1, -1, -1, -1
        return self.__earliest_start, self.__earliest_end, self.__latest_start, self.__latest_end, self.__latest_end[
            sorted_vertices[0]]

    def critical_activities(self):
        """
        Returns a list of the critical activities. A critical activity has a total time reserve of 0 (that means that
        its earliest start time is equal to the latest start time - it can only be done at that certain time).
        Runtime: O(V+E), where V is the number of vertices and E the number of edges in the graph
        :return: list of integers (activities/vertices of the DAG)
        """
        a = self.get_times()
        critical = []

        for i in range(self.nrVertices()):
            if self.__earliest_start[i] == self.__latest_start[i]:
                critical.append(i)

        return critical

# REPRESENTATION -------------------------------------------------------------------------------------------------------
    def __repr__(self):
        return str(self)

    def __str__(self):
        """
        string representation
        :return:
        """
        r = ''
        for i in self.dictCost.keys():
            r += str(i[0]) + ' ' + str(i[1]) + ' ' + str(self.dictCost[i]) + '\n'
        for i in self.dictIn.keys():
            if len(self.dictOut[i]) == 0 and len(self.dictIn[i]) == 0:
                r += str(i) + ' -1\n'
        return r

    def copyGraph(self):
        """
        copies graph to file
        :return:
        """
        return deepcopy(self)

#lab5-------------------------------------------------------------------------------------------------------------------
    def addEdgeUndirected(self, x, y):
        if x not in self.dictEdges[y] and y not in self.dictEdges[x]:
            self.dictEdges[x].append(y)
            self.dictEdges[y].append(x)
            self.E.append((x, y))
            self.E.append((y, x))
        else:
            raise Exception("edge already exists")

    def addVertexUndirected(self, x):
        if x in self.dictEdges:
            raise Exception("vertex already exists")
        self.dictEdges[x] = []

    def parseNeighbours(self, x):
        return self.dictEdges[x]

    def parseKeys(self):
        return list(self.dictEdges.keys())

    def getDegree(self, vertex):
        try:
            a = len(self.dictEdges[vertex])
            b = 0
            for i in self.dictEdges:
                if i != vertex and vertex in self.dictEdges[i]:
                    b += 1
            return a + b
        except KeyError:
            raise Exception("vertex doesn't exist")

    def getMaxDegreeVertex(self):
        max = -1
        vertex = -1
        for i in self.parseKeys():
            if self.getDegree(i) > max:
                max = self.getDegree(i)
                vertex = i
        return vertex

    def approximateVertexCover(self):
        result = set()
        while self.E:
            # choose random (u,v) edge
            (u, v) = choice(self.E)

            # add u and v to the result set, if they aren't already in there
            if u not in result:
                result.add(u)
            if v not in result:
                result.add(v)

            # delete all the edges having as endpoints u or v

            ok = True
            while ok:
                ok = False
                for i in range(len(self.E)):
                    if self.E[i][0] == u or self.E[i][1] == u or self.E[i][0] == v or self.E[i][1] == v:
                        del self.E[i]
                        ok = True
                        break

        return result

    def greedyVertexCover(self):
        solution = set()
        while self.dictEdges != {}:
            v = self.getMaxDegreeVertex()
            if self.getDegree(v) == 0:
                break
            solution.add(v)
            del self.dictEdges[v]
            ok = True
            while ok:
                ok = False
                for x in self.dictEdges:
                    if v in self.dictEdges[x]:
                        self.dictEdges[x].remove(v)
                        ok = True
                        break
        return solution

# READ FROM FILE -------------------------------------------------------------------------------------------------------
def readFile(file_name):
    """
    reads file
    :param file_name: the name of the file we want to read
    :raises: FNF if the file is not found
    :return:
    """
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    # f = open('graph1k.txt', 'r')
    # f = open('graph10k.txt', 'r')
    line = f.readline().strip().split()
    n = int(line[0])
    m = int(line[1])

    graph = Graph(n)
    for i in range(m):
        line = f.readline().strip().split()
        graph.addEdge(int(line[0]), int(line[1]), int(line[2]))

    return graph


def readFile1k():
    """
    reads the file with 1k inputs
    :return:
    """
    f = open('graph1k.txt', 'r')
    line = f.readline().strip().split()
    n = int(line[0])
    m = int(line[1])

    graph = Graph(n)
    for i in range(m):
        line = f.readline().strip().split()
        graph.addEdge(int(line[0]), int(line[1]), int(line[2]))

    return graph

def readFile10k():
    """
    reads the file with 10k inputs
    :return:
    """
    f = open('graph10k.txt', 'r')
    line = f.readline().strip().split()
    n = int(line[0])
    m = int(line[1])

    graph = Graph(n)
    for i in range(m):
        line = f.readline().strip().split()
        graph.addEdge(int(line[0]), int(line[1]), int(line[2]))

    return graph

def read_activities():
    """
    Reads activities. Format: the first line contains the number of activities N and it is
    followed by N lines of the format: activity number, predecessors(separated by +; "-" if there are no predecessors)
    and the duration of the activity.
    :return: Graph object
    """
    vertices = []

    G = Graph(vertices)

    try:
        with open("activities.txt", "r") as file:
            lines = [data.split(',') for data in file.read().split('\n')]
            n = int(lines[0][0])
            for i in range(n):
                G.addVertex(i)

            times = [0] * n
            for line in lines[1:]:
                activity = int(line[0])
                duration = int(line[2])
                prerequisites = list()
                if line[1] != "-":
                    prerequisites = [vertex for vertex in line[1].split('+')]
                times[activity] = duration
                for vertex in prerequisites:
                    G.addEdge(int(vertex), activity, 0)
            G.set_duration(times)

        return G
    except FileNotFoundError as e:
        raise FileNotFoundError()