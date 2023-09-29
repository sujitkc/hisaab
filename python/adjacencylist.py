# Adjacency List - start
## Graph - start

import edges as E

def empty_graph():     return {}

def make_graph(edges):
  new_g = empty_graph()
  for e in edges:
    add_edge(e = e, g = new_g)
  return new_g 

def get_edges(g):
  edges = []
  for n in g:
    for (n1, w) in g[n]:
      edges.append(E.make_edge(n1 = n, w = w, n2 = n1))
  return edges

def add_edge_to_edge_list(edge_list, (n, w)):
  for i in range(len(edge_list)):
    (n1, w1) = edge_list[i]
    if(n1 == n):
      edge_list[i] = (n, w + w1)
      return
  edge_list.append((n, w))

# assumption: g is not a multigraph.
def add_edge(e, g):
  n = E.get_start_node(e)
  if(not n in g):
    g[n] = []
  edge_list = g[n]
  add_edge_to_edge_list(edge_list, (E.get_end_node(e), E.get_weight(e)))
  return g
## Graph - end
# Adjacency List - end
