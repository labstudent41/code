import networkx as nx
import pylab as plt

# Create Blank graph
d = nx.DiGraph()
print(d)

# Feed page link to graph
d.add_weighted_edges_from([('A', 'B', 1), ('A', 'C', 1), ('C', 'A', 1), ('B', 'C', 1)])

# Print page rank for each page
print(nx.pagerank(d))

# Plot graph
nx.draw (d, with_labels = True)

x = y = 1
print(x, y)

