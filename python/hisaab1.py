def reroute(e, n):
  (n1, w, n2) = e
  if(n1 == n): return [(n2, -w, n1)]
  elif(n1 != n) and (n2 != n): return [(n1, w, n), (n2, -w, n)]
  else: return [(n1, w, n2)]

def starify_graph(g, n):
  new_g = []
  for e in g:
    new_edge = reroute(e, n)
    new_g.extend(new_edge)
  return new_g

# assumption: g is not a multigraph.
def merge(e, g):
  (n1, w, n2) = e
  for i in range(len(g)):
    (m1, w1, m2) = g[i]
    if(m1 == n1 and m2 == n2):
      g[i] = (n1, w + w1, n2)
      return g
  g.append((n1, w, n2))
  return g

def graph_of_mgraph(mg):
  g = []
  for e in mg:
    g = merge(e, g)
  return g

g = [
  ("Shilpi", 160, "Shraddha"),
  ("Shraddha", 300, "Shilpi"),
  ("Shraddha", 140, "Shilpi"),
  ("Shilpi", 300, "Taru"),
  ("Taru", 160, "Shraddha")
]
star_node = "Shraddha"

















print (graph_of_mgraph(starify_graph(g, star_node)))
