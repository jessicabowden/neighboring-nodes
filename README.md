* see file neighboringnodes.py

* an instance of the NeighboringNodes class can be created as follows:
```
NeighboringNodes(6, True)
NeighboringNodes(3, True)
```
* the first parameter indicates the size of the grid, and the second indicates whether debug is on/off

* the function `construct_grid` is called during `__init__` and creates the grid representation using a 2-d list

* the function `get_position` returns a tuple (x, y) for the location of a valid node in the grid. If an invalid node is passed, a ValueError is thrown

##### the function `get_neighbors_coordinates` takes the following arguments:
* m: an integer value which represents the neighborhood radius in which to search
* n_type: an enum of type NeighborhoodShape
* x, y: coordinates x & y for the target node (optional parameter)
* i: value for the target node (optional parameter)

Example:
```
neighboring_nodes_instance = NeighboringNodes(6, False)
neighboring_nodes_instance.get_neighbors_coordinates(3, NeighborhoodShape.SQUARE, i=13)
```

* this function calls one of 3 private functions, depending on which neighborhood shape is selected

* N.B.: see file testneighboringnodes.py for relevant unit tests


### Sample Code:
```
neighboring_nodes_test = NeighboringNodes(6, False)

print(neighboring_nodes_test.get_position(14))

print(neighboring_nodes_test.get_neighbors_coordinates(2, NeighborhoodShape.CROSS, i=15))
print(neighboring_nodes_test.get_neighbors_coordinates(3, NeighborhoodShape.SQUARE, i=13))
print(neighboring_nodes_test.get_neighbors_coordinates(2, NeighborhoodShape.DIAMOND, i=14))
```

* see file schema.sqlite for NeighborhoodNodes database schema representation

Example insertion (1 grid, 3 nodes):
```
INSERT INTO neighboring_nodes VALUES(1, 3);
INSERT INTO nodes VALUES(0, 0, 0, 1);
INSERT INTO nodes VALUES(1, 1, 0, 1);
INSERT INTO nodes VALUES(2, 2, 0, 1);
```

Example selection of all nodes from 1 grid:
```
SELECT * from nodes WHERE nn_id == 1;
```
