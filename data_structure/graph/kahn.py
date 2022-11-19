'''
拓扑排序
'''

from graph.my_graph import Graph


def sorted_topology(graph: Graph):
    # 节点剩余出度：
    # key:node,value : in_degree
    in_degree_map = {(node, node.in_degree) for node in graph.nodes}

    queue = [node for node in graph.nodes if node.in_degree == 0]

    res = []
    while queue:
        node = queue.pop(0)
        res.append(node)
        for child in node.nexts:
            in_degree_map[child].in_degree -= 1
            if in_degree_map[child].in_degree == 0:
                queue.append(child)
    return res
