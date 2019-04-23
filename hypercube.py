import random

def vertex_is_odd(k):
	result = 0
	while k > 0:
		result ^= k & 1
		k >>= 1
	return result

def get_odd_vertices(n):
	out = []
	for i in range(2 ** n):
		if vertex_is_odd(i):
			out.append(i)
	return out

def pick_connected_vertices(k, n_connections, n):
	flips = random.sample([1 << i for i in range(n)], n_connections)
	return set([k ^ flip for flip in flips])

class Path:
	def __init__(self, n):
		self.__n = n
		self.__n_vertices = 2 ** n
		self.__edges = [set() for i in range(self.__n_vertices)]

	def generate_path(self):
		odd_vertices = get_odd_vertices(self.__n)
		for vertex in odd_vertices:
			connected = pick_connected_vertices(vertex, 2, self.__n)
			self.__edges[vertex] = self.__edges[vertex].union(connected)
			for c in connected:
				self.__edges[c].add(vertex)

	def print_edges(self):
		for vertex in range(self.__n_vertices):
			src_format_str = "{0:0" + str(self.__n) + "b} -> "
			print(src_format_str.format(vertex))

p = Path(2)
p.generate_path()
p.print_edges()
