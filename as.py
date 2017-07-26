import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import operator



def random_removal(graph, remove_frac):
    
    # First, lets copy the graph so we don't change the original
    graph = graph.copy()
    
    
    # Now lets calculat oute the current size of the largest component
    initial_largest = len(largest_component(graph))

    # remove some random nodes
    graph.remove_nodes_from(np.random.choice(graph.nodes(), size=int(remove_frac*len(graph)), replace=False))

    # the case that the graph is empty
    if len(graph) > 0:
        relative_size_of_largest = len(max(nx.connected_component_subgraphs(graph), key=len)) / initial_largest
    else:
        relative_size_of_largest = 0.0
        
    return relative_size_of_largest


def largest_component(g):

    # We need to calculate the current size of the largest component
    largest = max(nx.connected_component_subgraphs(g), key=len)
    return largest

    
def main():
    as_graph = nx.read_gml('as-22july06.gml')
    print(nx.info(as_graph))
    lgraph = largest_component(as_graph)
    print(nx.info(lgraph))

    # This will be our list of fractions to run the simulation over
    fractions = np.linspace(0.0, 1.0, 30)

    # Lets do 20 trials for each fraction and take the mean, then do that for each fraction
    #ran_results = [ np.mean([random_removal(as_graph, frac) for i in range(4)]) for frac in fractions ]
    #print (ran_results)

    #degree distribution
    degree_sequence=sorted(nx.degree(as_graph).values()) # degree sequence
    r_degree_sequence=sorted(nx.degree(as_graph).values(), reverse=True) # degree sequence
    print(degree_sequence[:40])
    plt.hist(degree_sequence[:50],bins=50)
    plt.title("Degree rank plot")
    plt.ylabel("degree")
    plt.xlabel("rank")
    plt.show()



main()
