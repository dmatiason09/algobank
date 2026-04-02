import pytest
from graphs.graph import Graph
from graphs.dijkstra import dijkstra, reconstruct_path
from graphs.topological_sort import topological_sort


class TestGraph:
    def test_add_edge_undirected(self):
        g = Graph()
        g.add_edge("A", "B")
        assert g.has_edge("A", "B")
        assert g.has_edge("B", "A")

    def test_add_edge_directed(self):
        g = Graph(directed=True)
        g.add_edge("A", "B")
        assert g.has_edge("A", "B")
        assert not g.has_edge("B", "A")

    def test_neighbors(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        assert sorted(g.neighbors(1)) == [2, 3]

    def test_remove_edge(self):
        g = Graph()
        g.add_edge("X", "Y")
        g.remove_edge("X", "Y")
        assert not g.has_edge("X", "Y")

    def test_bfs(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        g.add_edge(3, 4)
        result = g.bfs(1)
        assert result[0] == 1
        assert set(result) == {1, 2, 3, 4}

    def test_dfs(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        g.add_edge(3, 4)
        result = g.dfs(1)
        assert result[0] == 1
        assert set(result) == {1, 2, 3, 4}

    def test_dfs_recursive(self):
        g = Graph()
        g.add_edge("A", "B")
        g.add_edge("A", "C")
        g.add_edge("B", "D")
        result = g.dfs_recursive("A")
        assert result[0] == "A"
        assert set(result) == {"A", "B", "C", "D"}

    def test_bfs_disconnected(self):
        """BFS from one component shouldn't reach the other."""
        g = Graph()
        g.add_edge(1, 2)
        g.add_vertex(3)
        result = g.bfs(1)
        assert 3 not in result

    def test_bfs_nonexistent_start(self):
        g = Graph()
        assert g.bfs(999) == []


class TestDijkstra:
    def setup_method(self):
        # simple weighted graph
        self.graph = {
            "A": [("B", 1), ("C", 4)],
            "B": [("A", 1), ("C", 2), ("D", 5)],
            "C": [("A", 4), ("B", 2), ("D", 1)],
            "D": [("B", 5), ("C", 1)],
        }

    def test_shortest_distances(self):
        distances, _ = dijkstra(self.graph, "A")
        assert distances["A"] == 0
        assert distances["B"] == 1
        assert distances["C"] == 3  # A -> B -> C
        assert distances["D"] == 4  # A -> B -> C -> D

    def test_reconstruct_path(self):
        _, parents = dijkstra(self.graph, "A")
        path = reconstruct_path(parents, "A", "D")
        assert path[0] == "A"
        assert path[-1] == "D"

    def test_path_to_self(self):
        distances, parents = dijkstra(self.graph, "A")
        assert distances["A"] == 0
        path = reconstruct_path(parents, "A", "A")
        assert path == ["A"]

    def test_unreachable_vertex(self):
        graph = {
            "A": [("B", 1)],
            "B": [("A", 1)],
            "C": [],  # isolated
        }
        distances, _ = dijkstra(graph, "A")
        assert distances["C"] == float('inf')


class TestTopologicalSort:
    def test_basic_dag(self):
        graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["D"],
            "D": [],
        }
        result = topological_sort(graph)
        assert result is not None

        # verify ordering: for every edge u->v, u appears before v
        idx = {v: i for i, v in enumerate(result)}
        assert idx["A"] < idx["B"]
        assert idx["A"] < idx["C"]
        assert idx["B"] < idx["D"]
        assert idx["C"] < idx["D"]

    def test_linear_chain(self):
        graph = {"A": ["B"], "B": ["C"], "C": []}
        result = topological_sort(graph)
        assert result == ["A", "B", "C"]

    def test_cycle_returns_none(self):
        graph = {
            "A": ["B"],
            "B": ["C"],
            "C": ["A"],  # cycle!
        }
        assert topological_sort(graph) is None

    def test_single_vertex(self):
        assert topological_sort({"X": []}) == ["X"]

    def test_course_schedule_example(self):
        """
        Classic interview scenario:
        CS101 -> CS201 -> CS301
        MATH101 -> CS201
        """
        graph = {
            "CS101": ["CS201"],
            "MATH101": ["CS201"],
            "CS201": ["CS301"],
            "CS301": [],
        }
        result = topological_sort(graph)
        idx = {v: i for i, v in enumerate(result)}
        assert idx["CS101"] < idx["CS201"]
        assert idx["MATH101"] < idx["CS201"]
        assert idx["CS201"] < idx["CS301"]
