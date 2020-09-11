from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    def __init__(self):
        self.vertices = {}
        self.last_move = None
        self.last_room_visited = None
        self.last_unknown_room = {}

    def add_exit(self, vertex):
        current_exits = {}
        for exits in player.current_room.get_exits():
            current_exits.update({exits: "?"})
        self.vertices[vertex] = current_exits

    def add_movement(self, move):
        opposite_direction = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
        last_room = opposite_direction[move]

        if self.last_room_visited in self.vertices:
            self.vertices[self.last_room_visited][move] = player.current_room.id 
            self.vertices[player.current_room.id].update({last_room: self.last_room_visited})
        else:
            print("vertex doesnt exist")

    def check_exits(self, id):
        all_exits = []
        for exit in self.vertices[id]:
            all_exits.append(self.vertices[id][exit])
        if '?' in all_exits:
            return True
        else:
            return False

    def previous_room(self, id):
        self.last_room_visited = id

    def dft(self, vertex):
        i = 0
        stack = Stack()
        visited = set()
        if vertex not in graph.vertices:
            self.add_exit(player.current_room.id)
            if self.last_move != None:
                self.add_movement(self.last_move)
        for exits in player.current_room.get_exits():
            stack.push({exits: '?'})
            self.last_unknown_room[vertex] = visited
        for exit in self.vertices[vertex]:
            if self.vertices[vertex][exit] == '?':
                if self.last_room_visited != vertex:
                    self.last_room_visited = vertex
                player.travel(exit)
                self.last_move = exit
                return traversal_path.append(exit)
        
    # def bfs(self, starting_vertex, destination_vertex):
    #     queue = Queue()
    #     visited = set()
    #     for exit in self.vertices[starting_vertex]:
    #         self.last_unknown_room[len(self.last_unknown_room) - 1]
    #         if self.vertices[starting_vertex][exit] == self.last_unknown_room[len(self.last_unknown_room) - 1]:
    #             return player.travel(self.vertices[starting_vertex][exit])

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
                
graph = Graph()

while len(graph.vertices) < 3:
    graph.dft(player.current_room.id)
    if player.current_room.id in graph.vertices:
        print(player.current_room.id)
        if graph.check_exits(player.current_room.id) == False:
            graph.last_unknown_room.pop(player.current_room.id)   
            graph.bfs(player.current_room.id, graph.last_unknown_room)   
       





# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")

