# Helper Code
from collections import defaultdict
import sys


class Graph:
    def __init__(self):
        self.nodes = set()  # A set cannot contain duplicate nodes
        self.neighbours = defaultdict(
            list)  # Defaultdict is a child class of Dictionary that provides a default value for a key that does not exists.
        self.distances = {}  # Dictionary. An example record as ('A', 'B'): 6 shows the distance between 'A' to 'B' is 6 units

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbours[from_node].append(to_node)
        self.neighbours[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance  # lets make the graph undirected / bidirectional

    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Neighbours are: ", self.neighbours)
        print("Distances are: ", self.distances)


''' TO DO: Find the shortest path from the source node to every other node in the given graph '''


def dijkstra(graph, source):
    # Declare and initialize result, unvisited, and path
    result = dict()

    for node in graph.nodes:
        result[node] = sys.maxsize

    result[source] = 0
    unvisited = set(graph.nodes)
    path = {}

    # As long as unvisited is non-empty
    while unvisited:
        # 1. Find the unvisited node having smallest known distance from the source node.
        min_node = None

        for unvisited_node in unvisited:
            if min_node is None or result[unvisited_node] < result[min_node]:
                min_node = unvisited_node

        if min_node is None:
            break

        # known distance of min_node
        current_distance = result[min_node]

        # 2. For the current node, find all the unvisited neighbours.
        # For this, you have calculate the distance of each unvisited neighbour.
        for neighbour in graph.neighbours[min_node]:
            if neighbour in unvisited:
                distance = current_distance + graph.distances[(min_node, neighbour)]

                # 3. If the calculated distance of the unvisited neighbour is less than the already known distance in
                # result dictionary, update the shortest distance in the result dictionary.
                if (neighbour not in result) or (distance < result[neighbour]):
                    result[neighbour] = distance

                    # 4. If there is an update in the result dictionary,
                    # you need to update the path dictionary as well for the same key.
                    path[neighbour] = min_node

        # 5. Remove the current node from the unvisited set.
        unvisited.remove(min_node)

    return result


# Test 1
testGraph = Graph()
for node in ['A', 'B', 'C', 'D', 'E']:
    testGraph.add_node(node)

testGraph.add_edge('A', 'B', 3)
testGraph.add_edge('A', 'D', 2)
testGraph.add_edge('B', 'D', 4)
testGraph.add_edge('B', 'E', 6)
testGraph.add_edge('B', 'C', 1)
testGraph.add_edge('C', 'E', 2)
testGraph.add_edge('E', 'D', 1)

print(dijkstra(testGraph, 'A'))  # {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4}

# Test 2
graph = Graph()
for node in ['A', 'B', 'C']:
    graph.add_node(node)

graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 5)
graph.add_edge('A', 'C', 10)

print(dijkstra(graph, 'A'))  # {'A': 0, 'C': 10, 'B': 5}

# Test 3
graph = Graph()
for node in ['A', 'B', 'C', 'D', 'E', 'F']:
    graph.add_node(node)

graph.add_edge('A', 'B', 5)
graph.add_edge('A', 'C', 4)
graph.add_edge('D', 'C', 1)
graph.add_edge('B', 'C', 2)
graph.add_edge('A', 'D', 2)
graph.add_edge('B', 'F', 2)
graph.add_edge('C', 'F', 3)
graph.add_edge('E', 'F', 2)
graph.add_edge('C', 'E', 1)

print(dijkstra(graph, 'A'))  # {'A': 0, 'C': 3, 'B': 5, 'E': 4, 'D': 2, 'F': 6}
