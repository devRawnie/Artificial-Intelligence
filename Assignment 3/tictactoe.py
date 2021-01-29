from random import choice
from time import sleep
from itertools import combinations

COMPUTER = 0
PLAYER = 1
MOVE_X = "X"
MOVE_O = "O"
class TicTacToe:
    players = {COMPUTER:"", PLAYER: ""}
    def __init__(self, player=MOVE_X):
        if player == MOVE_X:
            self.players[COMPUTER] = MOVE_O
            self.players[PLAYER] = MOVE_X
        else:
            self.players[COMPUTER] = MOVE_X
            self.players[PLAYER] = MOVE_O

        self.magic_board = [[4, 9, 2],[3,5,7],[8,1,6]]
        self.game_board = [["-" for i in range(3)] for i in range(3)]
        self.player_moves = []
        self.computer_moves = []
        # To map user's input to board position
        self.lookup = {
                    1:(0,0), 2:(0,1), 3: (0,2),
                    4:(1,0), 5:(1,1), 6: (1,2),
                    7:(2,0), 8:(2,1), 9: (2,2)
                            }
        
        # To map game board position to numeric positions
        self.rev_lookup = {
            4:1, 9:2, 2:3,
            3:4, 5:5, 7:6,
            8:7, 1:8, 6:9
        }

        self.available = {
                1:True, 2:True, 3:True,
                4:True, 5:True, 6:True,
                7:True, 8:True, 9:True
            }
        self.current_player = COMPUTER
    
    def display_board(self):
        # Displays the board as a 3x3 matrix after each move

        print("\nBOARD:")
        for i in range(3):
            print(*self.game_board[i], sep=" | ")

    def at_pos(self, val, magic_board = False):
        pos = self.lookup[val]
        if not magic_board:
            return self.game_board[pos[0]][pos[1]]
        else:
            return self.magic_board[pos[0]][pos[1]]    

    def update_board(self, pos, move):
        # Updates the board, with the current played move

        self.game_board[pos[0]][pos[1]] = move
        self.display_board()

    def wait_for_player(self):
        # randomChoice = choice([*self.available])
        # return randomChoice
        count = 0
        for i in range(3):
            for j in range(3):
                count += 1
                if self.game_board[i][j] == "-":
                    if j < 2:
                        print(count, end=" | ")
                    else:
                        print(count)
                else:
                    if j < 2:
                        print(self.game_board[i][j], end=" | ")
                    else:
                        print(self.game_board[i][j])

        move = int(input("\nEnter a spot for your move: "))

        if move < 1 or move > 9:
            print("Pick a spot on the board!!")
            return self.wait_for_player()

        if not self.available[move]:
            print("Pick an empty spot only!!")
            return self.wait_for_player()
        return move

    def get_possible_move(self, pair):
        potential = 15 - self.at_pos(pair[0], magic_board=True) - self.at_pos(pair[1], magic_board=True)
        if potential < 1 or potential > 9:
            return None
        if self.available[self.rev_lookup[potential]]:
            return self.rev_lookup[potential]
        return None

    def check_winning_move(self):
        all_moves = combinations(self.computer_moves, 2)
        for pair in all_moves:
            move = self.get_possible_move(pair)
            if move is not None:
                return move
        randomChoice = choice([*self.available])
        while not self.available[randomChoice]:
            randomChoice = choice([*self.available])
        return randomChoice

    def wait_for_computer(self):
        if len(self.player_moves) > 1:
            all_moves = combinations(self.player_moves, 2)
            for pair in all_moves:
                move = self.get_possible_move(pair)
                if move is None:
                    return self.check_winning_move()
                else:
                    return move
        elif len(self.player_moves) == 1:
            randomChoice = choice([*self.available])
            while not self.available[randomChoice]:
                randomChoice = choice([*self.available])
            return randomChoice
        else:
            return 5

    def next_move(self):
        # Checks whose move is next, and calls update_board() with the position of the move
        # If PLAYER has to play next
        move = None
        if self.current_player == PLAYER:
            print("\nPLAYER\'S MOVE")
            move = self.wait_for_player()
            self.player_moves.append(move)
        else:
            print("\nCOMPUTER\'S MOVE")
            move = self.wait_for_computer()
            self.computer_moves.append(move)

        self.available[move] = False
        self.update_board(self.lookup[move], self.players[self.current_player])
            
        # Updates the current player

        self.current_player = (self.current_player + 1) % 2

    def equals3(self, a,b,c):
        # Helper function to check whether 3 inputs are equal or not

        return (a==b and b==c and a!="-")

    def is_board_full(self):
        count = 0
        for i in self.available.keys(): 
            if self.available[i]:
                count += 1
        
        return (count == 0)

    def check_winner(self):
        winner = None

        # Check rows and columns
        for i in range(len(self.game_board)):
            for j in range(len(self.game_board)):
                if self.equals3(self.game_board[0][i], self.game_board[1][i], self.game_board[2][i]):
                    winner = self.game_board[0][i]
                    break
                if self.equals3(self.game_board[i][0], self.game_board[i][1], self.game_board[i][2]):
                    winner = self.game_board[i][0]
                    break

        # Check diagonals
        if self.equals3(self.game_board[0][0], self.game_board[1][1], self.game_board[2][2]):
            winner = self.game_board[0][0]
        
        if self.equals3(self.game_board[0][2], self.game_board[1][1], self.game_board[2][0]):
            winner = self.game_board[0][2]
        
        # Check for tie, i.e. when there is no winner and no available moves

        if winner is None and self.is_board_full():
            return "TIE!!"
        return winner

    def play(self):
        # Play until TIE or someone wins

        while True:
            self.next_move()
            result = self.check_winner()
            if result is not None:
                if result == "TIE!!":
                    print("\n%s"%result)
                else:
                    print("\nWinner: %s" % result)
                return 0
            sleep(1)

ob = TicTacToe()
ob.play()