const { Graph, dijkstra, reconstructPath, topologicalSort } = require('../graphs');

describe('Graph', () => {
  test('undirected edges', () => {
    const g = new Graph();
    g.addEdge('A', 'B');
    expect(g.hasEdge('A', 'B')).toBe(true);
    expect(g.hasEdge('B', 'A')).toBe(true);
  });

  test('directed edges', () => {
    const g = new Graph(true);
    g.addEdge('A', 'B');
    expect(g.hasEdge('A', 'B')).toBe(true);
    expect(g.hasEdge('B', 'A')).toBe(false);
  });

  test('neighbors', () => {
    const g = new Graph();
    g.addEdge(1, 2);
    g.addEdge(1, 3);
    expect(g.neighbors(1).sort()).toEqual([2, 3]);
  });

  test('remove edge', () => {
    const g = new Graph();
    g.addEdge('X', 'Y');
    g.removeEdge('X', 'Y');
    expect(g.hasEdge('X', 'Y')).toBe(false);
  });

  test('bfs', () => {
    const g = new Graph();
    g.addEdge(1, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 4);
    g.addEdge(3, 4);
    const result = g.bfs(1);
    expect(result[0]).toBe(1);
    expect(new Set(result)).toEqual(new Set([1, 2, 3, 4]));
  });

  test('dfs', () => {
    const g = new Graph();
    g.addEdge(1, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 4);
    g.addEdge(3, 4);
    const result = g.dfs(1);
    expect(result[0]).toBe(1);
    expect(new Set(result)).toEqual(new Set([1, 2, 3, 4]));
  });

  test('bfs on disconnected graph', () => {
    const g = new Graph();
    g.addEdge(1, 2);
    g.addVertex(3);
    expect(g.bfs(1)).not.toContain(3);
  });

  test('bfs nonexistent start', () => {
    const g = new Graph();
    expect(g.bfs(999)).toEqual([]);
  });
});

describe('dijkstra', () => {
  const graph = {
    A: [['B', 1], ['C', 4]],
    B: [['A', 1], ['C', 2], ['D', 5]],
    C: [['A', 4], ['B', 2], ['D', 1]],
    D: [['B', 5], ['C', 1]],
  };

  test('shortest distances', () => {
    const { distances } = dijkstra(graph, 'A');
    expect(distances.A).toBe(0);
    expect(distances.B).toBe(1);
    expect(distances.C).toBe(3);
    expect(distances.D).toBe(4);
  });

  test('reconstruct path', () => {
    const { parents } = dijkstra(graph, 'A');
    const path = reconstructPath(parents, 'A', 'D');
    expect(path[0]).toBe('A');
    expect(path[path.length - 1]).toBe('D');
  });

  test('path to self', () => {
    const { distances, parents } = dijkstra(graph, 'A');
    expect(distances.A).toBe(0);
    expect(reconstructPath(parents, 'A', 'A')).toEqual(['A']);
  });

  test('unreachable vertex', () => {
    const g = {
      A: [['B', 1]],
      B: [['A', 1]],
      C: [],
    };
    const { distances } = dijkstra(g, 'A');
    expect(distances.C).toBe(Infinity);
  });
});

describe('topologicalSort', () => {
  test('basic DAG', () => {
    const graph = {
      A: ['B', 'C'],
      B: ['D'],
      C: ['D'],
      D: [],
    };
    const result = topologicalSort(graph);
    expect(result).not.toBeNull();

    const idx = {};
    result.forEach((v, i) => { idx[v] = i; });
    expect(idx.A).toBeLessThan(idx.B);
    expect(idx.A).toBeLessThan(idx.C);
    expect(idx.B).toBeLessThan(idx.D);
  });

  test('linear chain', () => {
    const graph = { A: ['B'], B: ['C'], C: [] };
    expect(topologicalSort(graph)).toEqual(['A', 'B', 'C']);
  });

  test('cycle returns null', () => {
    const graph = { A: ['B'], B: ['C'], C: ['A'] };
    expect(topologicalSort(graph)).toBeNull();
  });

  test('single vertex', () => {
    expect(topologicalSort({ X: [] })).toEqual(['X']);
  });
});
