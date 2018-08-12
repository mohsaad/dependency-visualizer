#!/usr/bin/env python

import os
import sys
from graph_tool.all import *

'''
A class wrapping the GraphTool library for our specific purpose.
'''
class DependencyGraph(object):

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
		v1 = self.add_vertex()
		self.name_map[name] = v1

	'''
	add_edge
	name1 - The name of the first vertex as a string
	name2 - The name of the second vertex as a string
	Creates an undirected edge between the two vertices
	'''
	def add_edge(self, name1, name2):
		self.add_edge(self.name_map[name1], self.name_map[name2])

	def draw(self, output_size = (500, 500), output_name = "output.png"):
		graph_draw(self.graph)
