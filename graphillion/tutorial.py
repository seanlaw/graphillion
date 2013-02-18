# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

def grid(m, n=None, edge_probability=1.0):
    import networkx as nx
    from random import shuffle
    # critical edge probability is 0.5 in the percolation theory
    assert 0.6 < edge_probability and edge_probability <= 1
    m += 1
    if n is None:
        n = m
    else:
        n += 1
    edges = []
    for v in xrange(1, m * n + 1):
        if v % n != 0:
            edges.append((v, v + 1))
        if v <= (m - 1) * n:
            edges.append((v, v + n))
    g = nx.Graph(edges)
    while edge_probability < 1.0:
        g = nx.Graph(edges)
        edges_removed = edges[:]
        shuffle(edges_removed)
        p = 1 - edge_probability
        g.remove_edges_from(edges_removed[:int(len(edges)*p)])
        if nx.is_connected(g):
            break
    return g

def draw(g, universe):
    import networkx as nx
    import matplotlib.pyplot as plt
    if not isinstance(g, nx.Graph):
        g = nx.Graph(list(g))
    if not isinstance(universe, nx.Graph):
        universe = nx.Graph(list(universe))
    n = sorted(universe[1].keys())[1] - 1
    m = universe.number_of_nodes() / n
    g.add_nodes_from(universe.nodes())
    pos = {}
    for v in xrange(1, m * n + 1):
        pos[v] = ((v - 1) % n, (m * n - v) / n)
    nx.draw(g, pos)
    plt.show()
