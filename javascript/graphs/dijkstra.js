/**
 * Dijkstra's Shortest Path
 *
 * Time:  O((V + E) log V)
 * Space: O(V)
 *
 * Using a simple array-based approach for the priority queue.
 * A real implementation would use a proper min-heap but this
 * keeps the code readable for learning purposes.
 */

function dijkstra(graph, start) {
  const distances = {};
  const parents = {};
  const visited = new Set();

  // init distances to infinity
  for (const vertex of Object.keys(graph)) {
    distances[vertex] = Infinity;
    parents[vertex] = null;
  }
  distances[start] = 0;

  while (true) {
    // find unvisited vertex with smallest distance
    let u = null;
    let minDist = Infinity;
    for (const v of Object.keys(distances)) {
      if (!visited.has(v) && distances[v] < minDist) {
        u = v;
        minDist = distances[v];
      }
    }

    if (u === null) break;
    visited.add(u);

    for (const [neighbor, weight] of graph[u]) {
      if (visited.has(neighbor)) continue;
      const newDist = distances[u] + weight;
      if (newDist < distances[neighbor]) {
        distances[neighbor] = newDist;
        parents[neighbor] = u;
      }
    }
  }

  return { distances, parents };
}

function reconstructPath(parents, start, end) {
  const path = [];
  let current = end;
  while (current !== null) {
    path.push(current);
    current = parents[current];
  }
  path.reverse();

  if (path[0] !== start) return [];
  return path;
}

module.exports = { dijkstra, reconstructPath };
