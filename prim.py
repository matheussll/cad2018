infinity = float('inf')

def createAdjacentMatrix(vertices, graph):
  matrix = []
  for i in range(0, vertices):
    matrix.append([])
    for j in range(0, vertices):
      matrix[i].append(0)
  for i in range(0, len(graph)):
    matrix[graph[i][0]][graph[i][1]] = graph[i][2]
    matrix[graph[i][1]][graph[i][0]] = graph[i][2]
  return matrix

def prim(vertices, graph):
  adjMatrix = createAdjacentMatrix(vertices, graph)
  vertex = 0

  MST = []
  edges = []
  visited = []
  minEdge = [None,None,infinity]

  while len(MST) != vertices-1:
    visited.append(vertex)
    for r in range(0, vertices):
      if adjMatrix[vertex][r] != 0:
        edges.append([vertex,r,adjMatrix[vertex][r]])

    for e in range(0, len(edges)):
      if edges[e][2] < minEdge[2] and edges[e][1] not in visited:
        minEdge = edges[e]

    edges.remove(minEdge)

    MST.append(minEdge)

    vertex = minEdge[1]
    minEdge = [None,None,infinity]
  return MST

lines = open('prim_entries.txt').read().split('\n')
entries = [line.split(" ") for line in lines]

nodes = []
for entrie in entries:
  for index, e in enumerate(entrie):
    entrie[index] = int(entrie[index])
  if (entrie[0] not in nodes):
    nodes.append(entrie[0])
  if (entrie[1] not in nodes):
    nodes.append(entrie[1])

mst = prim(len(nodes), entries)
weight = 0
for node in mst:
  weight += node[2]
print "MINIMUM SPANNING TREE: " + str(mst)
print "WEIGHT: " + str(weight)

