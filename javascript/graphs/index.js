module.exports = {
  Graph: require('./Graph'),
  ...require('./dijkstra'),
  topologicalSort: require('./topologicalSort'),
};
