(*
The following program is useful to simplify the transactions amongst a group of people.
Problem Description: Often, a group of people may transact money between each other. A situation may arise when each person
may have taken some money from someone else, thus owing the other person that much amount. A
good way to simplify the settlement process would be to make one of the people involved as the
bank, or the star. Everyone makes a transaction with this person only, only the net amount she
owes to anyone.

User Instruction:
1. Open the file in a editor.
2. Edit the variable g to reflect what each person owes any other.
3. Save the file
4. Open the OCaml REPL
5. enter the command: #use "hisaab.ml";;

The answer will appear on the standard output.
*)

(*
  Description: Takes an edge e = (n1, w, n2) and a node n, and returns a list of edges, to
    apply starification transform on e.

  Signature: 'a * int * 'a -> 'a -> ('a * int * 'a) list

  Example:
  1)
# reroute (1, 10, 2) 1;;
- : (int * int * int) list = [(2, -10, 1)]
# reroute (2, 10, 1) 1;;
- : (int * int * int) list = [(2, 10, 1)]
# reroute (2, 10, 3) 1;;
- : (int * int * int) list = [(2, 10, 1); (3, -10, 1)]
*)
let reroute (n1, w, n2) n =
  if      n1 = n then [(n2, -w, n1)]
  else if n2 = n then [(n1, w, n2)]
  else                [(n1, w, n); (n2, -w, n)]

(*
  Description: Takes a list of lists and returns the corresponding list

  Signature: 'a list list -> 'a list

  Example:
# flatten_list [[1;2]; [3;4;5];[6]];;
- : int list = [1; 2; 3; 4; 5; 6]
*)
let rec flatten_list = function
    [] -> []
  | h :: t -> List.append h (flatten_list t)
 
(*
  Description: Takes a graph (could be multigraph) g and and a node n and returns
  and equivalent graph g' which is starred at n, and preserves the net input/output
  at each node of g.

  Signature: ('a * int * 'a) list -> 'a -> ('a * int * 'a) list
  Example:
# starify_graph [(1, 160, 2); (2, 440, 1); (1, 300, 3); (3, 160, 2)] 1;;
- : (int * int * int) list =
[(3, 160, 1); (2, -160, 1); (3, -300, 1); (2, 440, 1); (2, -160, 1)]
*)
let starify_graph g n =
  let list_of_lists = List.map (fun g -> reroute g n) g in
    flatten_list list_of_lists

(*
  Description: Takes an edge e = (n1, w, n2) and a graph g, and returns a 
  new graph g' such that g' is same as g except that if g contains an edge
  e' with same source and target nodes as e, then e and e' are merged by
  adding their weights.

  Signature: 'a * int * 'b -> ('a * int * 'b) list -> ('a * int * 'b) list

  Assumption: g is not a multi-graph.

  Example:
# let g2 = [(3, -140, 1); (2, 120, 1)];;
val g2 : (int * int * int) list = [(3, -140, 1); (2, 120, 1)]
# merge (3, 140, 1) g2;;
- : (int * int * int) list = [(3, 0, 1); (2, 120, 1)]
# merge (3, 140, 2) g2;; 
- : (int * int * int) list = [(3, -140, 1); (2, 120, 1); (3, 140, 2)]
# merge (3, 140, 2) [];;
- : (int * int * int) list = [(3, 140, 2)]
*)
let rec merge (n1, w, n2) = function
    [] -> [(n1, w, n2)]
  | (n1', w', n2') :: t ->
      if n1 = n1' && n2 = n2' then ((n1, w + w', n2) :: t)
      else (n1', w', n2') :: (merge (n1, w, n2) t)

(*
  Description: Takes a multigraph mg and returns its corresponding graph g by merging
    all edges between common pairs of nodes.

  Signature: ('a * int * 'b) list -> ('a * int * 'b) list

  Example:
# graph_of_mgraph [(1, 160, 2); (2, 300, 1); (2, 140, 1); (1, 300, 3); (3, 160, 2)];;
- : (int * int * int) list =
[(1, 160, 2); (2, 440, 1); (1, 300, 3); (3, 160, 2)]
*)  
let graph_of_mgraph mg =
  let rec iter g = function
    [] -> g
  | e :: t -> iter (merge e g) t
  in
  iter [] mg

(*
  Description: Turns the weight of every edge of a given graph to positive value by inverting the direction of the edge if its weight is negative.

  Signature: ('a * int * 'a) list -> ('a * int * 'a) list
  
  Example:
# abs_weight [("Taru", -140, "Shraddha"); ("Shilpi", 20, "Shraddha")];;
- : (string * int * string) list =
[("Shraddha", 140, "Taru"); ("Shilpi", 20, "Shraddha")]    
*)
let abs_weight g =
  List.map (
    fun (n1, w, n2) -> if w >= 0 then (n1, w, n2) else (n2, -w, n1)
  ) g

let remove_empty_edges g =
  List.filter (fun (_, w, _) -> w <> 0) g
(*
  Example graph (Provided by Shilpi)
  node 1 -> Shilpi
  node 2 -> Shraddha
  node 3 -> Taru

  (1, 160, 2) -> Shilpi owes Rs. 160 to Shraddha
*)
(*
let g = [("Shilpi", 160, "Shraddha"); ("Shraddha", 300, "Shilpi"); ("Shraddha", 140, "Shilpi"); ("Shilpi", 300, "Taru"); ("Taru", 160, "Shraddha")]
let star_node = "Shraddha"
*)
let g = [
  ("Shilpi",	2658, "Dummy");
  ("Anupama",	1100, "Dummy");
  ("Pooja",	1170, "Dummy");
  ("Pranlee",	200, "Dummy");
  ("Mahuya",	0, "Dummy");
  ("Ronita",	0, "Dummy")
]

let star_node = "Shilpi"

(*
let _ = remove_empty_edges (
          abs_weight (
            graph_of_mgraph (
              starify_graph g star_node)))
*)

let _ = star_node |>  (starify_graph g) |> graph_of_mgraph |> abs_weight |> remove_empty_edges 

let e1 = [
  ("r2", 10, "r3");
  ("r1", 20, "r2");
  ("r2", 10, "r4");
  ("r4", 30, "r3");
  ("r1", 15, "r6");
  ("r6", 100,"r5");
  ("r7", 25, "r5");
  ("r5", 150,"r4");
  ("r3", 30, "r7");
  ("r7", 90, "r4");
]

let star_node = "r4"
let _ = remove_empty_edges (
          abs_weight (
            graph_of_mgraph (
              starify_graph e1 star_node)))
