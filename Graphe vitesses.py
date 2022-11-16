import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

G = nx.DiGraph()

nodes = np.arange(0, 8).tolist()
G.add_nodes_from(nodes)

G.add_weighted_edges_from([(0,1,0.8), (0,2, 0),
 (1,3,0.2), (1, 4,0),
 (2, 5, 0.9), (2, 6,0), (3, 7,0),(4, 7,0.2),(5, 8,0),(6, 8,0.6),(7,9,0),(8,9,0.3) ])



elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

pos = {0:(0, 10),
 1:(10, 15), 2:(10, 5),
 3:(20, 20), 4:(20, 12.5),
 5:(20, 7.5), 6:(20, 0),7:(30,15),8:(30,5),9:(40,10)}

labels = {0:25,
 1:30, 2: 22,
 3: 32, 4: 28,
 5: 26, 6: 19, 7:29,8:22,9:25}

L=[]
for i in range (0,len(labels)) :
    L+=[labels[i]]
    i+=1
print(L)


# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6, edge_color="r", style="dashed")
nx.draw_networkx_edges(
    G, pos, edgelist=esmall, width=6)

# # node labels
nx.draw_networkx_labels(G, pos, labels,  font_size=6, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

plt.title("Graphe des vitesses")
plt.show()


