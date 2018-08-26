#!/usr/bin/env python

import os
import sys
from graph_tool.all import *
from find_includes import *


'''
A class wrapping the GraphTool library for our specific purpose.
'''
class GraphWrapper(object):

	'''
	Constructor.
	self.graph - The underlying data structure for our purposes.
	self.name_map - A utility map to make accessing vertices easier
	Note that we initialize an undirected graph.
	'''
	def __init__(self):
		self.graph = Graph()
		self.graph.set_directed(False)
		self.name_map = {}		

	'''
	add_vertex
	Adds a vertex to our dependency graph.
	We also store the vertex in the map for easy access
	'''
	def add_vertex(self, name):
		v1 = self.graph.add_vertex()
		self.name_map[name] = v1

	'''
	check_name_vertex
	If the node is not in the graph, return False
	Return true otherwise
	'''
	def check_name_vertex(self, name):
		if name not in self.name_map:
			return False

		return True

	'''
	add_edge
	name1 - The name of the first vertex as a string
	name2 - The name of the second vertex as a string
	Creates an undirected edge between the two vertices
	'''
	def add_edge(self, name1, name2):
		self.graph.add_edge(self.name_map[name1], self.name_map[name2])

	def draw(self, output_size = (2000, 1000), output_name = "output.png"):
		pos = sfdp_layout(self.graph)
		graph_draw(self.graph, pos, output_size=output_size, p = 0.5)


class DependencyGraph(object):
	
	def __init__(self):
		self.graph = GraphWrapper()
		self.dep_map = {}
	
	def build_map(self, directory):
		self.dep_map = build_map_includes(directory)
	
	def build_graph(self):
		for k in self.dep_map.keys():
			v = self.dep_map[k]
			if not self.graph.check_name_vertex(k):
				self.graph.add_vertex(k)

			for value in v:
				if not self.graph.check_name_vertex(value):
					self.graph.add_vertex(value)

				self.graph.add_edge(k, value)

	def visualize(self):
		print self.graph.graph
		self.graph.draw()

if __name__ == '__main__':
	d = DependencyGraph()
	d.build_map(sys.argv[1])
	d.build_graph()
	d.visualize()
