"""
Topological Sort (Kahn's algorithm)
------------------------------------
Time:  O(V + E)
Space: O(V)

Only works on DAGs (directed acyclic graphs). Returns a linear ordering
where for every edge u -> v, u comes before v.

Classic use cases: build systems, task scheduling, course prerequisites.
Returns None if the graph has a cycle.
"""

from collections import deque


def topological_sort(graph):
    """
    graph: dict of {vertex: [list of vertices it points to]}

    Returns a list with topological ordering, or None if there's a cycle.
    """
    # compute in-degrees
    in_degree = {v: 0 for v in graph}
    for v in graph:
        for neighbor in graph[v]:
            if neighbor not in in_degree:
                in_degree[neighbor] = 0
            in_degree[neighbor] += 1

    # start with all vertices that have no incoming edges
    queue = deque()
    for v in in_degree:
        if in_degree[v] == 0:
            queue.append(v)

    result = []

    while queue:
        v = queue.popleft()
        result.append(v)

        for neighbor in graph.get(v, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # if we didn't process all vertices, there's a cycle
    if len(result) != len(in_degree):
        return None

    return result
