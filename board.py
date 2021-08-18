
class board:
    def __init__(self,board_position=None):
        if board_position is not None:
            self.board_position = board_position
        else:
            self.board_position = {
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
        
        self.parent = None
        self.depth = None
        self.child_positions = []
        self.ai_move = None
        self.last_move = None
        self.static_estimate = None

    
    def generate_moves(self,board=None,player=None):
        if player is None:
            player=1
        if board is None:
            board = self.board_position

        moves_list = []
        for pos in board:
            if board[pos] is None: 
                new_move = board.copy()
                if player==1:
                    # self.last_move = pos
                    new_move[pos] = "x"
                else:
                    # self.last_move = pos
                    new_move[pos] = "o"
                moves_list.append(new_move)

        return moves_list
        
            
                
    
    def check_for_win(self,board=None,move_pos=None):
        if board is None:
            board = self.board_position
        if move_pos is None:
            print("No new move position given to check for win returning false")
            return False
        
        player = board[move_pos] 

        mills = {
            "a1": [["a2","a3"],["b2","c3"],["b1","c1"]],
            "a2": [["a1","a3"],["b2","c2"]],
            "a3": [["a2","a1"],["b3","c3"],["b2","c1"]],

            "b1": [["a1","c1"],["b2","b3"]],
            "b2": [["a3","c1"],["a2","c2"],["a1","c3"],["b1","b3"]],
            "b3": [["a3","c3"],["b2","b1"]],

            "c1": [["a1","b1"],["a3","b2"],["c2","c3"]],
            "c2": [["a2","b2"],["c3","c1"]],
            "c3": [["a3","b3"],["a1","b2"],["c1","c2"]],
        }

        for mill in mills[move_pos]:
            if (board[mill[0]]==board[mill[1]]==player):
                return True

        return False


    def static_estimation(self,board=None):
        if board is None:
            board = self.board_position
        n_player1 = 0
        n_player2 = 0
        n_empty = 0
        for pos in board:
            if board[pos] == "x":
                if self.check_for_win(move_pos=pos):
                    # print("HI-e1")
                    n_player1+=10000
                else:
                    n_player1 +=1
            elif board[pos] == "o":
                if self.check_for_win(move_pos=pos):
                    # print("HI-e2")
                    n_player2+=10000
                else:
                    n_player2 +=1
            else:
                n_empty +=1


        return n_player1 - n_player2

    def static_estimation_black(self,board=None):
        if board is None:
            board = self.board_position
        n_player1 = 0
        n_player2 = 0
        n_empty = 0

        for pos in board:
            if board[pos] == "x":
                if self.check_for_win(move_pos=pos):
                    # print("HI")
                    n_player1+=10000
                else:
                    n_player1 +=1
            elif board[pos] == "o":
                if self.check_for_win(move_pos=pos):
                    # print("HI2")
                    n_player2+=10000
                else:
                    n_player2 +=1
            else:
                n_empty +=1

        return n_player2 - n_player1


    def display_position(self,board=None):
        if board is None:
            board = self.board_position
        
        files = ["a","b","c"]
        ranks = ["3","2","1"]
        b = board.copy()
        for i in ranks:
            for j in files:
                if b[j+i] is None:
                    b[j+i]="-"

        
        print(b["a3"],b["b3"],b["c3"])
        print(b["a2"],b["b2"],b["c2"])
        print(b["a1"],b["b1"],b["c1"])
        # print(self.board_position)


    def write(self,output_file):

        temp_board = self.board_position.copy()
        for _loc in temp_board:
            if temp_board[_loc] is None:
                temp_board[_loc]="-"
            else:
                temp_board[_loc]=temp_board[_loc].upper()

        text =""
        text += temp_board["a1"]
        text += temp_board["a2"]
        text += temp_board["a3"]
        text += temp_board["b1"]
        text += temp_board["b2"]
        text += temp_board["b3"]
        text += temp_board["c1"]
        text += temp_board["c2"]
        text += temp_board["c3"]


        with open(output_file,"w") as file_writer:
            file_writer.write(text)

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

b = board(pos)
print(b.static_estimation())
# b.test()