from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.behaviours.protocols import TimedBehaviour

class SquareBehaviour(TimedBehaviour):
    def __init__(self, agent, time):
        super().__init__(agent, time)
        self.no = int(input("Enter the number to be squared: "))

    def on_time(self):
        super().on_time()
        output = "Square of {} is {}".format(self.no, self.no**2)
        display_message(self.agent.aid.localname, output)


class SquareAgent(Agent):
    def __init__(self, aid):
        super().__init__(aid=aid)
        behaviour = SquareBehaviour(self,  60.0)
        self.behaviours.append(behaviour)

if __name__ == '__main__':
    agents = []
    agent_name = 'square_agent_{}@localhost:{}'.format(20000, 20000)
    timed_agent = SquareAgent(AID(name=agent_name))
    agents.append(timed_agent)
    start_loop(agents)