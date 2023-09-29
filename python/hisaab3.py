'''
Instructions for Use
--------------------
To demonstrate the code, comment out either of the two implementations of the graph API:
- Edge List
- Adjacency List

On executing the code (python hisaab3.py), you will see similar results.
'''
import edges as E
#import adjacencylist   as G
#import edgelist        as G
import adjacencymatrix as G

def reroute(e, n):
  n1 = E.get_start_node(e)
  w  = E.get_weight(e)
  n2 = E.get_end_node(e)
  if(E.get_start_node(e) == n):
    return [E.make_edge(n1 = n2, w = -w, n2 = n1)]
  elif(n1 != n) and (n2 != n):
    e1 = E.make_edge(n1 = n1, w = w,  n2 = n)
    e2 = E.make_edge(n1 = n2, w = -w, n2 = n)
    return [e1, e2]
  else:
    return [e]

def starify_graph(g, n):
  new_g = G.empty_graph()
  edges = G.get_edges(g)
  for e in edges:
    new_edges = reroute(e, n)
    for e in new_edges:
      G.add_edge(g = new_g, e = e)
  return new_g

def t_gv():
  g = G.make_graph([
    ("Shilpi", 160, "Shraddha"),
    ("Shraddha", 300, "Shilpi"),
    ("Shraddha", 140, "Shilpi"),
    ("Shilpi", 300, "Taru"),
    ("Taru", 160, "Shraddha")
  ])
  star_node = "Shraddha"

  print("g = " + str(g))
  print(starify_graph(g, star_node))

def t_g1():
  g1 = G.make_graph([
    ("A", 15, "F"),
    ("A", 20, "B"),
    ("B", 10, "D"),
    ("B", 10, "C"),
    ("D", 30, "C"),
    ("C", 30, "G"),
    ("G", 25, "E"),
    ("F", 100, "E"),
    ("E", 150, "D"),
    ("G", 90, "D")
  ])
  print(g1)
  print(starify_graph(g1, "D"))

'''
{
  'A': [('F', 15), ('B', 20)],
  'C': [('G', 30)],
  'B': [('D', 10), ('C', 10)],
  'E': [('D', 150)],
  'D': [('C', 30)],
  'G': [('E', 25), ('D', 90)],
  'F': [('E', 100)]
}
'''

if __name__ == "__main__":
  t_gv()
