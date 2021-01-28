from random import choice
from time import sleep

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
        self.available = {
                    1:(0,0), 2:(0,1), 3: (0,2),
                    4:(1,0), 5:(1,1), 6: (1,2),
                    7:(2,0), 8:(2,1), 9: (2,2)
                            }
        self.current_player = COMPUTER
    
    def display_board(self):
        # Displays the board as a 3x3 matrix after each move

        print("\nBOARD:")
        for i in range(3):
            print(*self.game_board[i], sep=" | ")

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

        if move not in self.available:
            print("Pick an empty spot only!!")
            return self.wait_for_player()

        return move

    def wait_for_computer(self):
        randomChoice = choice([*self.available])
        return randomChoice

    def next_move(self):
        # Checks whose move is next, and calls update_board() with the position of the move
        # If PLAYER has to play next
        move = None
        if self.current_player == PLAYER:
            print("\nPLAYER\'S MOVE")
            move = self.wait_for_player()
        else:
            print("\nCOMPUTER\'S MOVE")
            move = self.wait_for_computer()

        self.update_board(self.available.pop(move), self.players[self.current_player])
            
        # Updates the current player

        self.current_player = (self.current_player + 1) % 2

    def equals3(self, a,b,c):
        # Helper function to check whether 3 inputs are equal or not

        return (a==b and b==c and a!="-")

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

        if winner is None and len(self.available) == 0:
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
