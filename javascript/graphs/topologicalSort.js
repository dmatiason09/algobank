/**
 * Topological Sort (Kahn's algorithm)
 *
 * Time:  O(V + E)
 * Space: O(V)
 *
 * Returns null if graph has a cycle.
 */

function topologicalSort(graph) {
  const inDegree = {};

  // init in-degrees
  for (const v of Object.keys(graph)) {
    if (!(v in inDegree)) inDegree[v] = 0;
    for (const neighbor of graph[v]) {
      if (!(neighbor in inDegree)) inDegree[neighbor] = 0;
      inDegree[neighbor]++;
    }
  }

  // vertices with no incoming edges
  const queue = [];
  for (const v of Object.keys(inDegree)) {
    if (inDegree[v] === 0) queue.push(v);
  }

  const result = [];

  while (queue.length > 0) {
    const v = queue.shift();
    result.push(v);

    for (const neighbor of (graph[v] || [])) {
      inDegree[neighbor]--;
      if (inDegree[neighbor] === 0) {
        queue.push(neighbor);
      }
    }
  }

  // cycle check
  if (result.length !== Object.keys(inDegree).length) {
    return null;
  }

  return result;
}

module.exports = topologicalSort;
