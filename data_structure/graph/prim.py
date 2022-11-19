'''
最小生成树：prim 算法
'''

from graph.my_graph import Graph

import heapq


def prim(graph: Graph):
    # 解锁的边进入小根堆
    priority_queue = []
    seen = set()
    res = set()

    # 如果 graph 是个森林，那么遍历形式可以找到所有子图的最小生成树
    for node in graph.nodes.values():
        # 随便挑选一个节点：node
        if node in seen: continue
        seen.add(node)
        # 由一个节点，解锁相连的边
        for edge in node.edges:
            heapq.heappush(priority_queue, edge)
        # 以上只是初始化以 node 开始图的探索

        while priority_queue:
            # 弹出解锁的边中，最小的边
            edge = heapq.heappop(priority_queue)
            to_node = edge.to_node

            if to_node in seen: continue
            seen.add(to_node)
            res.add(edge)
            for edge in to_node.edges:
                heapq.heappush(priority_queue, edge)

    return res
