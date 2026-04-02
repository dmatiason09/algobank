/**
 * Graph (adjacency list)
 *
 * BFS/DFS: O(V + E)
 * Supports directed and undirected.
 */

class Graph {
  constructor(directed = false) {
    this.adj = new Map();
    this.directed = directed;
  }

  addVertex(v) {
    if (!this.adj.has(v)) {
      this.adj.set(v, new Set());
    }
  }

  addEdge(u, v) {
    this.addVertex(u);
    this.addVertex(v);
    this.adj.get(u).add(v);
    if (!this.directed) {
      this.adj.get(v).add(u);
    }
  }

  removeEdge(u, v) {
    if (this.adj.has(u)) this.adj.get(u).delete(v);
    if (!this.directed && this.adj.has(v)) this.adj.get(v).delete(u);
  }

  hasEdge(u, v) {
    return this.adj.has(u) && this.adj.get(u).has(v);
  }

  neighbors(v) {
    return this.adj.has(v) ? [...this.adj.get(v)] : [];
  }

  vertices() {
    return [...this.adj.keys()];
  }

  bfs(start) {
    if (!this.adj.has(start)) return [];

    const visited = new Set([start]);
    const queue = [start];
    const result = [];

    while (queue.length > 0) {
      const vertex = queue.shift();
      result.push(vertex);

      const sorted = [...this.adj.get(vertex)].sort();
      for (const neighbor of sorted) {
        if (!visited.has(neighbor)) {
          visited.add(neighbor);
          queue.push(neighbor);
        }
      }
    }

    return result;
  }

  dfs(start) {
    if (!this.adj.has(start)) return [];

    const visited = new Set();
    const stack = [start];
    const result = [];

    while (stack.length > 0) {
      const vertex = stack.pop();
      if (visited.has(vertex)) continue;

      visited.add(vertex);
      result.push(vertex);

      const sorted = [...this.adj.get(vertex)].sort().reverse();
      for (const neighbor of sorted) {
        if (!visited.has(neighbor)) {
          stack.push(neighbor);
        }
      }
    }

    return result;
  }
}

module.exports = Graph;
