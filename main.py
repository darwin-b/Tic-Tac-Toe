from alpha_beta  import alphabeta_opening

from board import board
import sys
import os


cwd = os.getcwd()
try:
    arg = sys.argv[1]
except:
    print("\n","        No argument provided for Input Board position: Defauting to board1.txt  ")
    print("\n")
    arg = "board1.txt"
    

try:
    depth = int(sys.argv[2])
except:
    print("\n","        No argument provided for depth: Defauting to depth = 3  ")
    print("\n")
    depth =7

input_file = cwd +os.path.sep+arg
output_file = cwd+os.path.sep+"board2.txt"
output_file2 = cwd+os.path.sep+"board4.txt"


# def read(file_path):
#     with open(file_path) as file:
#         _input = file.read()
#     return _input

# try:
#     _input = read(input_file)
# except:
#     print("Please check if input file exist")
#     exit()

# change this initialization for different order of filling when there is tie in static estimate
input_pos = {
    "a1":None,
    "a2":None,
    "a3":None,
    "b1":None,
    "b2":None,
    "b3":None,
    "c1":None,
    "c2":None,
    "c3":None,
}

# for count,_location in enumerate(input_pos):
#     if _input[count] =="-":
#         input_pos[_location]=None
#     else:
#         input_pos[_location]= _input[count].lower()

pos = {
    "a1":"x",
    "a2":"o",
    "a3":"o",
    "b1":"x",
    "b2":"x",
    "b3":None,
    "c1":"x",
    "c2":None,
    "c3":"o",
}

input_pos=pos

# pos = {
#         "a0" : None,
#         "a3" : None,
#         "a6" : "b",
#         "b1" : None,
#         "b3" : None,
#         "b5" : "w",
#         "c2" : None,
#         "c3" : None,
#         "c4" : "w",
#         "d4" : None,
#         "d5" : None,
#         "d6" : None,
#         "e2" : None,
#         "e3" : None,
#         "e4" : None,
#         "f1" : None,
#         "f3" : None,
#         "f5" : None,
#         "g0" : None,
#         "g3" : None,
#         "g6" : "b",
# }
# input_pos2 = pos
depth=7
# computer_move=minimax_opening(input_pos,depth,move="w")
# computer_move=minimax_opening(input_pos,depth,move="b")
# computer_move = alphabeta_opening(input_pos,depth,move="w")
# computer_move = alphabeta_opening(input_pos,depth,move="b")

# computer_move = minimax_midgame(input_pos,depth,move="w")
# computer_move = minimax_midgame(input_pos2,depth,move="b")
# computer_move = alphabeta_midgame(input_pos,depth,move="w")
# computer_move = alphabeta_midgame(input_pos2,depth,move="b")
# computer_move.write(output_file)


computer_move=alphabeta_opening(input_pos,depth=7,move=1)
computer_move.write(output_file)
