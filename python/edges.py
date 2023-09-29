## Edge - start
def make_edge(n1, w, n2):        return (n1, w, n2)
def get_start_node(e):
  (n1, w, n2) = e
  return n1
def get_end_node(e):
  (n1, w, n2) = e
  return n2
def get_weight(e):
  (n1, w, n2) = e
  return w
## Edge - end
