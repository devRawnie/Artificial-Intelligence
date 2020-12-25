from pade.behaviours.protocols import Behaviour
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.misc.utility import start_loop


def sum(a, b):
    return a + b


class SumBehaviour(Behaviour):
    def __init__(self, agent, a, b):
        super().__init__(agent)
        self.a = a
        self.b = b

    def on_start(self):
        super().on_start()
        c = sum(self.a, self.b)
        print('Sum is', c)


class SumAgent(Agent):
    def __init__(self, aid):
        super().__init__(aid=aid)
        agent_behaviour = SumBehaviour(self, 4, 5)
        self.behaviours.append(agent_behaviour)


if __name__ == '__main__':
    agents = list()
    agent_name = 'agent_sum_{}@localhost:{}'.format(20000, 20000)
    agent_sum = SumAgent(AID(name=agent_name))
    agents.append(agent_sum)

    start_loop(agents)

