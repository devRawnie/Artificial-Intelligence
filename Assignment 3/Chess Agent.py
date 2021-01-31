from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
from tictactoe import *

 #### Computer Agent Class

class ComputerAgent(Agent):
    def __init__(self, aid, receiver_agent):
        super().__init__(aid)
        self.receiver_agent = receiver_agent
        self.move = MOVE_O

    def check_winning_move(self):
        all_moves = combinations(computer_moves, 2)
        for pair in all_moves:
            move = get_possible_move(pair)
            if move is not None:
                return move
        randomChoice = choice([*available])
        while not available[randomChoice]:
            randomChoice = choice([*available])
        return randomChoice

    def play_move(self):
        if len(player_moves) > 1:
            all_moves = combinations(player_moves, 2)
            for pair in all_moves:
                move = get_possible_move(pair)
                if move is None:
                    return self.check_winning_move()
                else:
                    return move
        elif len(player_moves) == 1:
            randomChoice = choice([*available])
            while not available[randomChoice]:
                randomChoice = choice([*available])
            return randomChoice
        else:
            return 5

    def play(self):
        sleep(1)
        pos = self.play_move()

        computer_moves.append(pos)
        available[pos] = False
        update_board(lookup[pos], self.move)
        # Check for winner
        result = check_winner()
        if result is not None:
            if result == "TIE!!":
                print("\n%s"%result)
            else:
                print("\nWinner: %s" % result)
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
        self.send(message)

    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver


#### Human Agent Class

class HumanAgent(Agent):
    def __init__(self, aid, receiver):
        super().__init__(aid)
        self.receiver_agent = receiver
        self.move = MOVE_X

    def play_move(self):
        count = 0
        for i in range(3):
            for j in range(3):
                count += 1
                if game_board[i][j] == "-":
                    if j < 2:
                        print(count, end=" | ")
                    else:
                        print(count)
                else:
                    if j < 2:
                        print(game_board[i][j], end=" | ")
                    else:
                        print(game_board[i][j])

        display_message(self.aid.localname, "Enter a spot for your move: " )
        move = int(input(""))

        if move < 1 or move > 9:
            print("Pick a spot on the board!!")
            return self.play_move()

        if not available[move]:
            print("Pick an empty spot only!!")
            return self.play_move()
        return move

    def play(self):
        sleep(1)
        pos = self.play_move()
        available[pos] = False
        player_moves.append(pos)
        update_board(lookup[pos], self.move)
        result = check_winner()
        if result is not None:
            if result == "TIE!!":
                print("\n%s"%result)
            else:
                print("\nWinner: %s" % result)
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
