"""
Alex Petrov
CPE 202
Project 5
"""
from queues import QueueLinked
UNDISCOVERED = 0
DISCOVERED = 1
PROCESSED = 2
WHITE = "White"
BLACK = "Black"

class Graph:
    """
    This class reresents the graph ADT
    Attr:
        verticies(dict) - a dictionary of verticies
        num_verticies(int) - the number of verticies
        reverse_lookup(hashmap) - a lookup table for verticies by serial id
        adjacency_list(list) - adjacency matrix for vertecies
        current_serial_id(int) - current serial id for vertex
    """
    def __init__(self, filename):
        self.verticies = []
        self.reverse = []
        self.current_serial_id = 1
        self.is_bicolor = True
        file = open(filename, "r")
        conn = file.readlines()
        file.close()
        for i in range(1, int(conn[0])+1):
            name = '%s' % (i)
            self.add_vertex(name)
        new_list = []
        for string in conn:
            new = string.split()
            new_list.append(new)
        for j in range(2, len(new_list)):
            self.add_edge(int(new_list[j][0]), int(new_list[j][1]))
        self.num_verticies = conn[0]
        self.queue = QueueLinked(len(self.verticies))

    def add_vertex(self, name):
        """adds a vertex to the graph
            Attr:
                name(str) - the name of the vertex
        """
        vertex = Vertex(self.current_serial_id, name)
        self.verticies.append(vertex)
        self.current_serial_id += 1

    def add_edge(self, vert1, vert2):
        """adds an undirected edge between two verticies
            Attr:
                v1(Vertex) - a vertex
                v2(Vertex) - other vertex
                weight(int) - optional weight of edge
        """
        vertex1 = self.verticies[vert1-1]
        vertex2 = self.verticies[vert2-1]
        vertex1.adjacent.append(vertex2.name)
        vertex2.adjacent.append(vertex1.name)

    def get_conn_components(self, vertex_list=[None]):
        """This function returns a list of list that shows the groups of connected verticies.
        This function utilizes breadth fist search
            Attr:
                vertex_list(list) - the list of lists that begins empty
            Returns:
                This function returns the vertex_list that contains list of connected verticies
        """
        vertex_list = []
        component = []
        for vertex in self.verticies:
            if vertex.status == UNDISCOVERED:
                self.dfs(vertex, component)
                if component not in vertex_list and component is not None:
                    vertex_list.append(component)
            component = []
        return vertex_list

    def get_conn_components_bfs(self, vertex_list=[None]):
        """This function returns a list of list that shows the groups of connected verticies.
            This function utilizes breadth fist search
            Attr:
                vertex_list(list) - the list of lists that begins empty
            Returns:
                This function returns the vertex_list that contains list of connected verticies
        """
        vertex_list = []
        component = []
        for vertex in self.verticies:
            if vertex.status == UNDISCOVERED:
                self.bfs(vertex, component)
                if component not in vertex_list and component is not None:
                    vertex_list.append(component)
            vertex.status = PROCESSED
            component = []
        return vertex_list

    def dfs(self, current, component=[None]):
        """does depth first search by recursion
            Args:
                current(Vertex) - the current vertex
                component(list) - an accumulator
            Returns:
                component(list) - the updated list of connections
        """
        current.status = DISCOVERED
        component.append(current.vid)
        for i in current.adjacent:
            vertex = self.verticies[int(i)-1]
            _color_vertex(current, vertex)
            if vertex.status == UNDISCOVERED:
                vertex.status = DISCOVERED
                self.dfs(vertex, component)
            bipar = bicolor(current, vertex)
            if not bipar:
                self.is_bicolor = False
        current.status = PROCESSED
        return component

    def bfs(self, current, component=[None]):
        """does depth first search by recursion
            Args:
                current(Vertex) - the current vertex
                time(int) - the current time. 0 if not passed
                component(list) - an accumulator
            Returns:
                component(list) - the updated list of connections
        """
        if current.vid in component:
            self.queue.dequeue()
        if current.vid not in component:
            component.append(current.vid)
        current.status = DISCOVERED
        for item in current.adjacent:
            vertex = self.verticies[int(item)-1]
            _color_vertex(current, vertex)
            bicolor(current, vertex)
            if vertex.status == UNDISCOVERED:
                vertex.status = DISCOVERED
                self.queue.enqueue(vertex)
                component.append(vertex.vid)
            bipar = bicolor(current, vertex)
            if not bipar:
                self.is_bicolor = False
        if not self.queue.is_empty():
            self.bfs(self.queue.items.head.first, component)
        return component

def _color_vertex(current, vertex):
    """This function makes sure that adjacent verteces are different colors
        Attr:
            current(Vertex) - a vertex
            vertex(Vertex) - a vertex adjacent to current
        Returns:
            This function switches the color of a vertex if needed
    """
    if current.color == WHITE:
        vertex.color = BLACK
    if current.color == BLACK:
        vertex.color = WHITE

def bicolor(current, vertex):
    """This function takes two adjacent verteces and checks whether or
        not they are the same color
        Args:
            current(Vertex) - One vertex
            vertex(Vertex)  - The other vertex
        Returns:
            This function returns true if the colors are the same and false if they are not
    """
    if current.color == vertex.color:
        return False
    return True

class Vertex:
    """
    Vertex of graph. Graph is on vertex or none
    Attr:
        vid(int) - id of vertex
        name(str) - name of vertex
        entry_time(int) - the process entry time
        exit_time(int) - the process exit time
        status(int) - the process status
        predecessor(Vertex) - the predecessor
    """
    def __init__(self, vid, name):
        self.vid = vid
        self.name = name
        self.status = UNDISCOVERED
        self.predecessor = None
        self.color = WHITE
        self.adjacent = []

    def __repr__(self):
        if self.status == 2:
            self.status = "PROCESSED"
        elif self.status == 1:
            self.status = "DISCOVERED"
        else:
            self.status = "UNDISCOVERED"
        return ">|Vertex: %s, Adj: %s, Color:%s, Status: %s|<" %\
         (self.name, self.adjacent, self.color, self.status)

    def __eq__(self, other):
        return isinstance(other, Vertex) and other.vid == self.vid
