class Graph:
    def __init__(self):
        self.adj_list  = {}

    def add_vertex(self,v1):
        if v1 not in self.adj_list:
            self.adj_list[v1] = []
            return True
        return False

    def add_edge(self,v1,v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self,v1,v2):
        if v1 in self.adj_list[v2] and v2 in self.adj_list[v1]:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False
    
    def remove_vertex(self,v1):
        if v1 in self.adj_list:
            for othervertex in self.adj_list:
                if v1 in self.adj_list[othervertex]:
                    self.adj_list[othervertex].remove(v1)
            del self.adj_list[v1]
            return True
        return False
    
    def print_graph(self):
        for i in self.adj_list:
            print(f'vertex {i} has edges with {self.adj_list[i]}')
        

my_graph = Graph()
my_graph.add_vertex(10)

my_graph.add_vertex(20)

my_graph.add_edge(10,20)
my_graph.add_vertex(50)
my_graph.add_edge(10,30)
my_graph.print_graph()
my_graph.remove_vertex(10)
my_graph.print_graph()

