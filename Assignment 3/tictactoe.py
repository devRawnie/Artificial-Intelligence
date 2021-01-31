from random import choice
from time import sleep
from itertools import combinations

COMPUTER = 0
HUMAN = 1
MOVE_X = "X"
MOVE_O = "O"

magic_board = [[4, 9, 2],[3,5,7],[8,1,6]]
game_board = [["-" for i in range(3)] for i in range(3)]
player_moves = []
computer_moves = []
lookup = {
            1:(0,0), 2:(0,1), 3: (0,2),
            4:(1,0), 5:(1,1), 6: (1,2),
            7:(2,0), 8:(2,1), 9: (2,2)
                    }
available = {
                1:True, 2:True, 3:True,
                4:True, 5:True, 6:True,
                7:True, 8:True, 9:True
            }
# players = [MOVE_O, MOVE_X]
        # To map game board position to numeric positions
rev_lookup = {
        4:1, 9:2, 2:3,
        3:4, 5:5, 7:6,
        8:7, 1:8, 6:9
    }
def get_possible_move(pair):
    potential = 15 - at_pos(pair[0], magic=True) - at_pos(pair[1], magic=True)
    if potential < 1 or potential > 9:
        return None
    if available[rev_lookup[potential]]:
        return rev_lookup[potential]
    return None

def at_pos(val, magic = False):
    pos = lookup[val]
    if not magic:
        return game_board[pos[0]][pos[1]]
    else:
        return magic_board[pos[0]][pos[1]]    

def is_board_full():
        count = 0
        for i in available.keys(): 
            if available[i]:
                count += 1
        
        return (count == 0)

def display_board():
        print("\nBOARD:")
        for i in range(3):
            print(game_board[i], sep=" | ")

def update_board(pos, move):
    # Updates the board, with the current played move
    
    game_board[pos[0]][pos[1]] = move
    # display_board()

def equals3(a,b,c):
        # Helper function to check whether 3 inputs are equal or not
        return (a==b and b==c and a!="-")


def check_winner():
        winner = None

        # Check rows and columns
        for i in range(len(game_board)):
            for j in range(len(game_board)):
                if equals3(game_board[0][i], game_board[1][i], game_board[2][i]):
                    winner = game_board[0][i]
                    break
                if equals3(game_board[i][0], game_board[i][1], game_board[i][2]):
                    winner = game_board[i][0]
                    break

        # Check diagonals
        if equals3(game_board[0][0], game_board[1][1], game_board[2][2]):
            winner = game_board[0][0]
        
        if equals3(game_board[0][2], game_board[1][1], game_board[2][0]):
            winner = game_board[0][2]
        
        # Check for tie, i.e. when there is no winner and no available moves

        if winner is None and is_board_full():
            return "TIE!!"
        return winner