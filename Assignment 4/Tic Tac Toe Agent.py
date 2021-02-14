from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
from time import sleep
from tictactoe import *

 #### Computer Agent Class
lookup = {
    1:(0,0), 2:(0,1), 3:(0,2),
    4:(1,0), 5:(1,1), 6:(1,2),
    7:(2,0), 8:(2,1), 9:(2,2)
}
available = {
    1:True, 2:True, 3:True,
    4:True, 5:True, 6:True,
    7:True, 8:True, 9:True
}
game_board = [[EMPTY for i in range(3)] for i in range(3)]

class ComputerAgent(Agent):
    def __init__(self, aid, receiver_agent):
        super().__init__(aid)
        self.receiver_agent = receiver_agent
        self.move = O

    def play_move(self):
        optimal = minimax_helper(game_board, self.move)
        for key in lookup.keys():
            if lookup[key] == optimal[0]:
                return key

    def play(self):
        pos = self.play_move()
        available[pos] = False
        position = lookup[pos]
        game_board[position[0]][position[1]] = self.move
        display_message(self.aid.localname, "Thinking...")
        sleep(1)
        for i in range(3):
            for j in range(3):
                if game_board[i][j] is None:
                    if j < 2:
                        print("-", end=" | ")
                    else:
                        print("-")
                else:
                    if j < 2:
                        print(game_board[i][j], end=" | ")
                    else:
                        print(game_board[i][j])

        # Check for winner
        if terminal(game_board):
            game_result = winner(game_board) 
            if game_result is None:
                print("\nIts a TIE!!")
            else:
                print("\nWinner: %s" % game_result)
        else:
            self.send_message(pos)


    def on_start(self):
        super().on_start()
        pos = self.play()        

    def react(self, message):
        super().react(message)
        display_message(self.aid.localname, "Human: {}".format(message.content))
        self.play()

    def send_message(self, content):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(self.receiver_agent)
        self.add_all_agents(message.receivers)
        msg = "Played at position {}".format(content)
        message.set_content(msg)
        sleep(1)
        self.send(message)

    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver


#### Human Agent Class

class HumanAgent(Agent):
    def __init__(self, aid, receiver):
        super().__init__(aid)
        self.receiver_agent = receiver
        self.move = X

    def play_move(self):
        display_message(self.aid.localname, "Enter a spot for your move: ")
        sleep(1)
        count = 0
        for i in range(3):
            for j in range(3):
                count += 1
                if game_board[i][j] is None:
                    if j < 2:
                        print(count, end=" | ")
                    else:
                        print(count)
                else:
                    if j < 2:
                        print(game_board[i][j], end=" | ")
                    else:
                        print(game_board[i][j])

        move = int(input(""))

        if move < 1 or move > 9:
            print("Pick a spot on the board!!")
            return self.play_move()

        if not available[move]:
            print("Pick an empty spot only!!")
            return self.play_move()
        return move

    def play(self):
        pos = self.play_move()
        available[pos] = False
        position = lookup[pos]
        game_board[position[0]][position[1]] = self.move
        if terminal(game_board):
            game_result = winner(game_board) 
            if game_result is None:
                print("\nIts a TIE!!")
            else:
                print("\nWinner: %s" % game_result)
        else:
            self.send_message(pos)

        
    def react(self, message):
        super().react(message)
        display_message(self.aid.localname, "Computer: {}".format(message.content))
        self.play()

    def send_message(self, content):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(self.receiver_agent)
        self.add_all_agents(message.receivers)
        msg = "Played at position {}".format(content)
        message.set_content(msg)
        self.send(message)

    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver


if __name__ == '__main__':
    agents = list()
    human_agent_aid = AID(name='human_agent@localhost:{}'.format(30010))
    computer_agent_aid = AID(name='computer_agent@localhost:{}'.format(30000))
    human_agent = HumanAgent(human_agent_aid, computer_agent_aid)
    computer_agent = ComputerAgent(computer_agent_aid, human_agent_aid)
    agents.append(computer_agent)
    agents.append(human_agent)

    start_loop(agents)

