#### Exercise 5

```textile
Suppose now that the BaceFook network can be any graph. Design and implement a Greedy algorithm for the problem.
Moreover, generate 100 different graphs of 100 nodes. To do this, you may use the random Python library: in particular, the function bool(random.getrandbits(1)) can be used to return a random Boolean, that in turn can be used to decide whether to add or not a given edge.
Finally, evaluate how the greedy algorithm performs on these graphs. Does the algorithm return an optimal solution? If not, can you bound the approximation ratio of the algorithm?
```

We designed and implemented a greedy algorithm for the exercise 5 that is linear in m -> **O(m)**

```textile
Let C be a collection of vertices
Let E contain all the edges of the graph

C <- empty

While E is not empty:
    select an edge {(u,v)}
    C <- C U {(u,v)}
    delete all incident edges of u and v
Return C
```


