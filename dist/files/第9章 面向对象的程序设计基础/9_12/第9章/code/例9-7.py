# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:05:55 2021

@author: lx
"""
import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
G.add_weighted_edges_from([(1,2,2),(1,3,8),(1,4,1),
                            (2,3,6),(2,5,1),
                            (3,4,7),(3,5,5),(3,6,1),(3,7,2),
                            (4,7,9),
                            (5,6,3),(5,8,2),(5,9,9),
                            (6,7,4),(6,9,6),
                            (7,9,3),(7,10,1),
                            (8,9,7),(8,11,9),
                            (9,10,1),(9,11,2),
                            (10,11,4)])
minWPath_v1_v11 = nx.dijkstra_path(G, source=1, target=11)
print("顶点 v1 到 顶点 v11 的最短加权路径: ", minWPath_v1_v11)
lMinWPath_v1_v11 = nx.dijkstra_path_length(G, source=1, target=11)
print("顶点 v1 到 顶点 v11 的最短加权路径长度: ", lMinWPath_v1_v11)
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, alpha=0.5)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = labels)
plt.show()