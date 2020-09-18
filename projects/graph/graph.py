"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue to hold nodes to visit
        to_visit = Queue()
        # Create a set to hold visited nodes
        visited = set()
        # Initialize: Add the starting node to the queue
        to_visit.enqueue(starting_vertex)
        # While queue not empty:
        while to_visit.size() > 0:
            # Dequeue first entry
            v = to_visit.dequeue()
            # if not visited
            if v not in visited:
                print(v)
                # Add to the visited set
                visited.add(v)
                # Enqueue all its neighbors
                for edge in self.vertices[v]:
                    to_visit.enqueue(edge)

            

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack to hold nodes to visit
        to_visit = Stack()
        # Create a set to hold visited nodes
        visited = set()
        # Initialize: Add the starting node to the stack
        to_visit.push(starting_vertex)
        # While queue not empty:
        while to_visit.size() > 0:
            # Pop first entry
            v = to_visit.pop()
            # if not visited
            if v not in visited:
                print(v)
                # Add to the visited set
                visited.add(v)
                # Enqueue all its neighbors
                for edge in self.vertices[v]:
                    to_visit.push(edge)

    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)

            for neighbor in self.vertices[starting_vertex]:
                self.dft_recursive(neighbor, visited)
                

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue enqueue A PATH TO the starting vertex ID
        to_visit = Queue()
        # Create a Set to store visited vertices
        visited = set()
        # Enqueue A PATH TO the starting vertex ID
        to_visit.enqueue([starting_vertex])
        # While the queue is not empty...
        while to_visit.size() > 0:
        # Dequeue the first PATH
            path = to_visit.dequeue()
        # Grab the last vertex from the PATH
            v = path[-1]
        # If that vertex has not been visited...
            if v not in visited:
            # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                # IF SO, RETURN PATH
                    return path
            # Then add A PATH TO its neighbors to the back of the queue
            for neighbor in self.vertices[v]:
                # COPY THE PATH
                copy_path = path[:]
                # APPEND THE NEIGHOR TO THE BACK
                copy_path.append(neighbor)
                # Mark it as visited...
                to_visit.enqueue(copy_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
         # Create an empty stack 
        to_visit = Stack()
        # Create a Set to store visited vertices
        visited = set()
        # Pop A PATH TO the starting vertex ID
        to_visit.push([starting_vertex])
        # While the stack is not empty...
        while to_visit.size() > 0:
        # Pop the first PATH
            path = to_visit.pop()
        # Grab the last vertex from the PATH
            v = path[-1]
        # If that vertex has not been visited...
            if v not in visited:
            # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                # IF SO, RETURN PATH
                    return path
            # Then add A PATH TO its neighbors to the back of the queue
            for neighbor in self.vertices[v]:
                # COPY THE PATH
                copy_path = path[:]
                # APPEND THE NEIGHBOR TO THE BACK
                copy_path.append(neighbor)
                # Mark it as visited...
                to_visit.push(copy_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))