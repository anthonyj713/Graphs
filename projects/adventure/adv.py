from room import Room
from player import Player
from world import World

import random
from random import choice
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

visited = set()
prev_move = ''
next_move = ''
rooms = {}


next_move = 'n'
traversal_path.append(next_move)

while len(visited) < 500:
    player.travel(next_move)
    visited.add(player.current_room.id)

    prev_move = next_move
    
    if prev_move == 'n':
        if 'e' in player.current_room.get_exits():
            next_move = 'e'
        elif 'n' in player.current_room.get_exits():
            next_move = 'n'
        elif 'w' in player.current_room.get_exits():
            next_move = 'w'
        else:
            next_move = 's'

    elif prev_move == 'e':
        if 's' in player.current_room.get_exits():
            next_move = 's'
        elif 'e' in player.current_room.get_exits():
            next_move = 'e'
        elif 'n' in player.current_room.get_exits():
            next_move = 'n'
        else:
            next_move = 'w'

    elif prev_move == 's':
        if 'w' in player.current_room.get_exits():
            next_move = 'w'
        elif 's' in player.current_room.get_exits():
            next_move = 's'
        elif 'e' in player.current_room.get_exits():
            next_move = 'e'
        else:
            next_move = 'n'

    elif prev_move == 'w':
        if 'n' in player.current_room.get_exits():
            next_move = 'n'
        elif 'w' in player.current_room.get_exits():
            next_move = 'w'
        elif 's' in player.current_room.get_exits():
            next_move = 's'
        else:
            next_move = 'e'

   

    if len(player.current_room.get_exits()) == 4:
        current = player.current_room.id 

        if current not in rooms:
            rooms[current] = []

        if next_move not in rooms[current]:
            rooms[current].append(next_move)

        elif len(rooms[current]) < 4:
            next_move = choice([i for i in ['n', 'e', 's', 'w']if i not in rooms[current]])
            rooms[current].append(next_move)

        else:
            next_move = rooms[current][len(rooms[current])%4]
            rooms[current].append(next_move)

    traversal_path.append(next_move)


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

