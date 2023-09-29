# Adjacency matrix - start
## Graph - start

import edges as E

def empty_graph():     return ([], [])

def make_graph(edges):
  g = empty_graph()
  for e in edges:
    add_edge(e, g)
  return g 

def get_edges(g):
  (nodes, matrix) = g
  edges = []
  for row_num in range(len(matrix)):
    row = matrix[row_num]
    for col_num in range(len(row)):
      if(matrix[row_num][col_num] != 0):
        edges.append(E.make_edge(
                       n1 = nodes[row_num],
                       w  = matrix[row_num][col_num],
                       n2 = nodes[col_num]))
  return edges

def add_node(g, nid):
  (nodes, matrix) = g
  matrix.append([0] * len(nodes))
  for row in matrix:
    row.append(0) # by default, the newly added node is not connected to any 
                  # other node. Hence, the edge weight is 0 for all edges 
                  # between it and other nodes.

  nodes.append(nid)

# assumption: g is not a multigraph.
def add_edge(e, g):
  start = E.get_start_node(e)
  end  = E.get_end_node(e)
  w    = E.get_weight(e)
  
  (nodes, matrix) = g

  new_start = False
  if(start in nodes): # start node already present in g
    for i in range(len(nodes)):
      if(nodes[i] == start):
        row_num = i
  else:
    new_start = True

  new_end = False
  if(end in nodes): # end node already present in g
    for i in range(len(nodes)):
      if(nodes[i] == end):
        col_num = i
  else:
    new_end = True

  if(new_start == True): # start node not present already in g
    add_node(g, start)
    row_num = len(nodes) - 1
  if(new_end == True):   # end noden not present already in g
    add_node(g, end)
    col_num = len(nodes) - 1

  # Adding the weight w to the already existing weight of the edge.
  # For a newly added edge, the earlier weight would be 0 (see add_node).
  matrix[row_num][col_num] += w
