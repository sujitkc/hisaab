# Adds an edge (n, w) to edge list if an edge with the same node doesn't exist.
# Otherwise, it replaces the existing one with another whose weight is w + w1.
def add_edge(edge_list, e):
  (n, w) = e
  for i in range(len(edge_list)):
    (n1, w1) = edge_list[i]
    if(n1 == n):
      edge_list[i] = (n, w + w1)
      return
  edge_list.append((n, w))

def starify_graph(g, n):
  new_g = {} # instantiating a dictionary
  for n1 in g: #initialising the empty graph
    new_g[n1] = []
  for n1 in g:
    # invert and add every node starting with n.
    if(n1 == n):
      for (n2, w) in g[n1]:
        add_edge(new_g[n2], (n1, -w))
    else:
      for (n2, w) in g[n1]:
        # add every node ending at n.
        if(n2 == n):
          add_edge(new_g[n1], (n2, w))
        # reroute all other nodes.
        else:
          add_edge(new_g[n1], (n, w))
          add_edge(new_g[n2], (n, -w))
  return new_g

g = {
  "Shilpi"   : [("Shraddha", 160), ("Taru", 300)],
  "Shraddha" : [("Shilpi", 300), ("Shilpi", 140)],
  "Taru"     : [("Shraddha", 160)]
}
star_node = "Shraddha"

print(starify_graph(g, star_node))
