from pade.behaviours.protocols import Behaviour
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.misc.utility import start_loop, display_message
from tictactoe import TicTacToe


class ChessBehaviour(Behaviour):
    def __init__(self, agent):
        super().__init__(agent)
        self.count = 0
        self.object = TicTacToe()

    def on_start(self):
        super().on_start()
        choice = int(input("Press 1 to play\nPress 0 to exit\n: "))
        if choice == 1:
            self.object.play()
        elif choice == 0:
            return
        else:
            print("Invalid choice")

class ChessAgent(Agent):
    def __init__(self, aid):
        super().__init__(aid=aid)
        self.behaviours.append(ChessBehaviour(self))


if __name__ == '__main__':
    agents = []
    agent_name = 'chess_agent{}@localhost:{}'.format(20000, 20000)
    chess_agent = ChessAgent(AID(name=agent_name))
    agents.append(chess_agent)
    start_loop(agents)

