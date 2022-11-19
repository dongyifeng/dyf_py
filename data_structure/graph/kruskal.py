from graph.my_graph import Graph
from graph.my_graph import create_graph

from graph.UnionFind import UnionFind

import heapq


def kruskal(graph: Graph):
    union_find = UnionFind(graph.nodes.values())

    priority_queue = []
    for edge in graph.edges:
        heapq.heappush(priority_queue, edge)

    result = set()
    while priority_queue:
        edge = heapq.heappop(priority_queue)
        if not union_find.same(edge.from_node, edge.to_node):
            result.add(edge)
            union_find.union(edge.from_node, edge.to_node)

    return result


matrix = [(0, 1, 4),
          (0, 7, 8),
          (1, 7, 11),
          (1, 2, 8),
          (2, 3, 7),
          (2, 5, 4),
          (2, 8, 2),
          (3, 4, 9),
          (3, 5, 14),
          (4, 5, 10),
          (5, 6, 2),
          (6, 7, 1),
          (6, 8, 6),
          (7, 8, 7)]

graph = create_graph(matrix)

for edge in kruskal(graph):
    print(edge.from_node.value, edge.to_node.value, edge.weight)
