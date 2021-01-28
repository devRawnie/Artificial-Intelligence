from random import choice
from time import sleep

class TicTacToe:
    def __init__(self):
        self.players = ["O", "X"];
        self.magic_board = [[4, 9, 2],[3,5,7],[8,1,6]]
        self.game_board = [["-" for i in range(3)] for i in range(3)]
        self.available = {
                    1:(0,0), 2:(0,1), 3: (0,2),
                    4:(1,0), 5:(1,1), 6: (1,2),
                    7:(2,0), 8:(2,1), 9: (2,2)
                            }
        self.current_player = choice([0,1])
    
    def display_board(self):
        print("\nBOARD: \n")
        for i in range(3):
            print(*self.game_board[i], sep=" | ")

    def update_board(self, pos, move):
        self.game_board[pos[0]][pos[1]] = move
        self.display_board()

    def next_move(self):
        randomChoice = choice([*self.available])
        self.update_board(self.available.pop(randomChoice), self.players[self.current_player])
        self.current_player = (self.current_player + 1) % 2

    def equals3(self, a,b,c):
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
        
        if winner is None and len(self.available) == 0:
            return "TIE!!"
        return winner

    def play(self):
        while True:
            self.next_move()
            result = self.check_winner()
            if result is not None:
                if result == "TIE!!":
                    print(result)
                else:
                    print("Winner: %s" % result)
                break
            sleep(1)


ob = TicTacToe()
ob.play()