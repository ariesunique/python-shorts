"""
Given an undirected graph ↴ with maximum degree ↴ DD, find a graph coloring ↴ using at most D+1D+1 colors.

For example: [nocolorgraph.svg](https://recurse.zulipchat.com/user_uploads/13/KZup7eIej0NlQNO6egIOeuWM/nocolorgraph.svg)

First described by Robert Frucht in 1939, the Frucht graph is a 3-regular graph with 12 vertices, 18 edges, and no nontrivial symmetries.
This graph's maximum degree (DD) is 3, so we have 4 colors (D+1D+1). Here's one possible coloring: [coloredgraph.svg](https://recurse.zulipchat.com/user_uploads/13/NebSzdytPcHp2EkEP4yWaAw6/coloredgraph.svg)

The Frucht graph with legal coloring.
Graphs are represented by a list of NN node objects, each with a label, a set of neighbors, and a color and provided to you in the GraphNode Class.


What is a graph?
A graph organizes items in an interconnected network.

Each item is a node (or vertex). Nodes are connected by edges

A graph is composed of nodes (or vertices) that are connected by edges.
Strengths:
Representing links. Graphs are ideal for cases where you're working with things that connect to other things. Nodes and edges could, for example, respectively represent cities and highways, routers and ethernet cables, or Facebook users and their friendships.
Weaknesses:
Scaling challenges. Most graph algorithms are O(n*lg(n))O(n∗lg(n)) or even slower. Depending on the size of your graph, running algorithms across your nodes may not be feasible.
Terminology
Directed or undirected
In directed graphs, edges point from the node at one end to the node at the other end. In undirected graphs, the edges simply connect the nodes at each end.
"""

import unittest
import pytest


class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None
        
    def __repr__(self):
        return "Node {} has {} neighbors and is color {}".format(self.label, len(self.neighbors), self.color)


def color_graph(graph, colors):

    max_degree = max( len(node.neighbors) for node in graph)
    max_colors = max_degree + 1
    color_index = 0
    
    sorted_by_neighbors = sorted( graph, key=lambda node: len(node.neighbors), reverse=True  )
    
    for node in sorted_by_neighbors:
        #print(node)
        if not node.color:
            node.color = colors[color_index]
            color_inde += 1
            
        for child in node.neighbors:
            if not child.color:
                pass
    
    
    print("Max degree is {}".format(max_degree))
     
    return 0


















# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.colors = frozenset([
            'red',
            'green',
            'blue',
            'orange',
            'yellow',
            'white',
        ])

    def assertGraphColoring(self, graph, colors):
        self.assertGraphHasColors(graph, colors)
        self.assertGraphColorLimit(graph)
        for node in graph:
            self.assertNodeUniqueColor(node)

    def assertGraphHasColors(self, graph, colors):
        print("Testing graphHasColors")
        for node in graph:
            msg = 'Node %r color %r not in %r' % (node.label, node.color, colors)
            self.assertIn(node.color, colors, msg=msg)

    def assertGraphColorLimit(self, graph):
        print("Testing graphColorLimit")
        max_degree = 0
        colors_found = set()
        for node in graph:
            print(node)
            degree = len(node.neighbors)
            max_degree = max(degree, max_degree)
            colors_found.add(node.color)
        max_colors = max_degree + 1
        used_colors = len(colors_found)
        msg = 'Used %d colors and expected %d at most' % (used_colors, max_colors)
        self.assertLessEqual(used_colors, max_colors, msg=msg)

    def assertNodeUniqueColor(self, node):
        print("Testing unique colors")
        for adjacent in node.neighbors:
            print(node)
            msg = 'Adjacent nodes %r and %r have the same color %r' % (
                node.label,
                adjacent.label,
                node.color,
            )
            self.assertNotEqual(node.color, adjacent.color, msg=msg)

    
    def test_line_graph(self):
        node_a = GraphNode('a')
        node_b = GraphNode('b')
        node_c = GraphNode('c')
        node_d = GraphNode('d')

        node_a.neighbors.add(node_b)
        node_b.neighbors.add(node_a)
        node_b.neighbors.add(node_c)
        node_c.neighbors.add(node_b)
        node_c.neighbors.add(node_d)
        node_d.neighbors.add(node_c)

        graph = [node_a, node_b, node_c, node_d]
        tampered_colors = list(self.colors)
        color_graph(graph, tampered_colors)
        self.assertGraphColoring(graph, self.colors)

    def test_separate_graph(self):
        node_a = GraphNode('a')
        node_b = GraphNode('b')
        node_c = GraphNode('c')
        node_d = GraphNode('d')

        node_a.neighbors.add(node_b)
        node_b.neighbors.add(node_a)
        node_c.neighbors.add(node_d)
        node_d.neighbors.add(node_c)

        graph = [node_a, node_b, node_c, node_d]
        tampered_colors = list(self.colors)
        color_graph(graph, tampered_colors)
        self.assertGraphColoring(graph, self.colors)

    def test_triangle_graph(self):
        node_a = GraphNode('a')
        node_b = GraphNode('b')
        node_c = GraphNode('c')

        node_a.neighbors.add(node_b)
        node_a.neighbors.add(node_c)
        node_b.neighbors.add(node_a)
        node_b.neighbors.add(node_c)
        node_c.neighbors.add(node_a)
        node_c.neighbors.add(node_b)

        graph = [node_a, node_b, node_c]
        tampered_colors = list(self.colors)
        color_graph(graph, tampered_colors)
        self.assertGraphColoring(graph, self.colors)

    @pytest.mark.webtest
    def test_envelope_graph(self):
        node_a = GraphNode('a')
        node_b = GraphNode('b')
        node_c = GraphNode('c')
        node_d = GraphNode('d')
        node_e = GraphNode('e')

        node_a.neighbors.add(node_b)
        node_a.neighbors.add(node_c)
        node_b.neighbors.add(node_a)
        node_b.neighbors.add(node_c)
        node_b.neighbors.add(node_d)
        node_b.neighbors.add(node_e)
        node_c.neighbors.add(node_a)
        node_c.neighbors.add(node_b)
        node_c.neighbors.add(node_d)
        node_c.neighbors.add(node_e)
        node_d.neighbors.add(node_b)
        node_d.neighbors.add(node_c)
        node_d.neighbors.add(node_e)
        node_e.neighbors.add(node_b)
        node_e.neighbors.add(node_c)
        node_e.neighbors.add(node_d)

        graph = [node_a, node_b, node_c, node_d, node_e]
        tampered_colors = list(self.colors)
        color_graph(graph, tampered_colors)
        self.assertGraphColoring(graph, self.colors)

    def test_loop_graph(self):
        node_a = GraphNode('a')

        node_a.neighbors.add(node_a)

        graph = [node_a]
        tampered_colors = list(self.colors)
        with self.assertRaises(Exception):
            color_graph(graph, tampered_colors)


#unittest.main(verbosity=2)