"""
Dijkstra's Shortest Path
-------------------------
Time:  O((V + E) log V) with a priority queue
Space: O(V)

Finds shortest paths from a source to all other vertices in a
weighted graph with non-negative edge weights.

Returns both the distances and the actual paths (reconstructed
from a parent map).
"""

import heapq


def dijkstra(graph, start):
    """
    graph: dict of {vertex: [(neighbor, weight), ...]}
    start: source vertex

    Returns (distances, parents) where:
      - distances[v] = shortest distance from start to v
      - parents[v] = previous vertex on the shortest path
    """
    distances = {v: float('inf') for v in graph}
    parents = {v: None for v in graph}
    distances[start] = 0

    # (distance, vertex)
    pq = [(0, start)]

    visited = set()

    while pq:
        dist, u = heapq.heappop(pq)

        if u in visited:
            continue
        visited.add(u)

        for neighbor, weight in graph[u]:
            if neighbor in visited:
                continue
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                parents[neighbor] = u
                heapq.heappush(pq, (new_dist, neighbor))

    return distances, parents


def reconstruct_path(parents, start, end):
    """Builds the actual path from start to end using the parent map."""
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parents[current]

    path.reverse()

    # if path doesn't start with start, there's no valid path
    if path[0] != start:
        return []
    return path
