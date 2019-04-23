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
			print(src_format_str.format(vertex), end="")
			targets = []
			for dest in self.__edges[vertex]:
				target_format_str = "{0:0" + str(self.__n) + "b}"
				targets.append(target_format_str.format(dest))
			print(str(targets))

	def is_hamiltonian(self):
		print(self.__edges)
		nodes_hit = [False for i in range(self.__n_vertices)]
		nodes_hit[0] = True

		cur = 0
		if len(self.__edges[0]) != 2:
			return False

		next_vertex = next(iter(self.__edges[0]))
		self.__edges[next_vertex].remove(cur)

		print("{} -> ".format(cur), end="")
		cur = next_vertex

		while next_vertex != 0:
			nodes_hit[cur] = True

			if len(self.__edges[cur]) != 1:
				return False

			next_vertex = next(iter(self.__edges[cur]))
			self.__edges[next_vertex].remove(cur)

			print("{} -> ".format(cur), end="")
			cur = next_vertex
		print(next_vertex)
		#print(nodes_hit)
		return all(nodes_hit)

p = Path(3)
p.generate_path()
#p.print_edges()

print(p.is_hamiltonian())
