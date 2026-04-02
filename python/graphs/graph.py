"""
Graph (adjacency list)
----------------------
Add vertex:  O(1)
Add edge:    O(1)
BFS/DFS:     O(V + E)

Supports both directed and undirected graphs.
Using a dict of sets for the adjacency list since it makes
edge lookup and deletion cleaner.
"""

from collections import deque


class Graph:
    def __init__(self, directed=False):
        self._adj = {}
        self._directed = directed

    def add_vertex(self, v):
        if v not in self._adj:
            self._adj[v] = set()

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self._adj[u].add(v)
        if not self._directed:
            self._adj[v].add(u)

    def remove_edge(self, u, v):
        if u in self._adj:
            self._adj[u].discard(v)
        if not self._directed and v in self._adj:
            self._adj[v].discard(u)

    def has_edge(self, u, v):
        return u in self._adj and v in self._adj[u]

    def neighbors(self, v):
        return list(self._adj.get(v, set()))

    def vertices(self):
        return list(self._adj.keys())

    def bfs(self, start):
        """Breadth-first traversal from start vertex."""
        if start not in self._adj:
            return []

        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []

        while queue:
            vertex = queue.popleft()
            result.append(vertex)

            for neighbor in sorted(self._adj[vertex]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def dfs(self, start):
        """Depth-first traversal from start (iterative)."""
        if start not in self._adj:
            return []

        visited = set()
        stack = [start]
        result = []

        while stack:
            vertex = stack.pop()
            if vertex in visited:
                continue
            visited.add(vertex)
            result.append(vertex)

            # add neighbors in reverse sorted order so we visit
            # the smallest first (matches what you'd expect)
            for neighbor in sorted(self._adj[vertex], reverse=True):
                if neighbor not in visited:
                    stack.append(neighbor)

        return result

    def dfs_recursive(self, start):
        """DFS but recursive — cleaner code, limited by call stack."""
        visited = set()
        result = []
        self._dfs_helper(start, visited, result)
        return result

    def _dfs_helper(self, vertex, visited, result):
        if vertex in visited or vertex not in self._adj:
            return
        visited.add(vertex)
        result.append(vertex)
        for neighbor in sorted(self._adj[vertex]):
            self._dfs_helper(neighbor, visited, result)
