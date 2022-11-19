class Edge:
    def __init__(self, weight, from_node=None, to_node=None):
        self.weight = weight
        self.from_node = from_node
        self.to_node = to_node

    def __lt__(self, other):
        return self.weight < other.weight



class Node:
    def __init__(self, value):
        self.value = value
        self.in_degree = 0
        self.out_degree = 0
        self.nexts = []
        self.edges = []


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = set()


# [ from, to, weight ]

# [ [1, 2, 0.5],
#  [2, 3, 0.6] ]
def create_graph(matrix):
    graph = Graph()

    for i in range(len(matrix)):
        from_val = matrix[i][0]
        to_val = matrix[i][1]
        weight = matrix[i][2]

        if from_val not in graph.nodes:
            graph.nodes[from_val] = Node(value=from_val)
        if to_val not in graph.nodes:
            graph.nodes[to_val] = Node(value=to_val)

        from_node = graph.nodes[from_val]
        to_node = graph.nodes[to_val]
        from_node.nexts.append(to_node)
        from_node.out_degree += 1
        to_node.in_degree += 1

        edge = Edge(weight, from_node, to_node)
        from_node.edges.append(edge)
        graph.edges.add(edge)

    return graph


graph_map = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def create_graph2(graph_map):
    graph = Graph()

    for from_val, to_list in graph_map.items():

        weight = 0
        for to_val in to_list:

            if from_val not in graph.nodes:
                graph.nodes[from_val] = Node(value=from_val)
            if to_val not in graph.nodes:
                graph.nodes[to_val] = Node(value=to_val)

            from_node = graph.nodes[from_val]
            to_node = graph.nodes[to_val]
            from_node.nexts.append(to_node)
            from_node.out_degree += 1
            to_node.in_degree += 1

            edge = Edge(weight, from_node, to_node)
            from_node.edges.append(edge)
            graph.edges.add(edge)

    return graph


# graph = create_graph2(graph_map)

# 带权无向图
matrix = [[0, 5, 3, 0],
          [5, 0, 2, 6],
          [3, 2, 0, 1],
          [0, 6, 1, 0]]


def create_graph3(matrix):
    graph = Graph()

    n = len(matrix)
    for from_val in range(n):

        for to_val in range(n):
            weight = matrix[from_val][to_val]
            if weight == 0: continue

            if from_val not in graph.nodes:
                graph.nodes[from_val] = Node(value=from_val)
            if to_val not in graph.nodes:
                graph.nodes[to_val] = Node(value=to_val)

            from_node = graph.nodes[from_val]
            to_node = graph.nodes[to_val]
            from_node.nexts.append(to_node)
            from_node.out_degree += 1
            to_node.in_degree += 1

            edge = Edge(weight, from_node, to_node)
            from_node.edges.append(edge)
            graph.edges.add(edge)

    return graph

