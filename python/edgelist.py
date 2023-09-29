import edges as E

# Edge List - start
## Graph - start
def empty_graph():     return []
def make_graph(edges): return edges
def get_edges(g):      return g
 
# assumption: g is not a multigraph.
def add_edge(e, g):
  edges = get_edges(g)
  for i in range(len(edges)):
    e2 = edges[i]
    if(E.get_start_node(e2) == E.get_start_node(e) and E.get_end_node(e2) == E.get_end_node(e)):
      edges[i] = E.make_edge(E.get_start_node(e), E.get_weight(e) + E.get_weight(e2), E.get_end_node(e))
      return g
  g.append(e)
  return g
## Graph - end
# Edge List - end
