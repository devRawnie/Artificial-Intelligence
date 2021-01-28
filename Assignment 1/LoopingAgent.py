from pade.behaviours.protocols import Behaviour
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.misc.utility import start_loop

class LoopBehaviour(Behaviour):
    def __init__(self, agent):
        super().__init__(agent)
        self.count = 0
    
    def on_start(self):
        super().on_start()
        for i in range(10):
            print("Case ", i+1)
            a = int(input("Enter the value of a: "))
            b = int(input("Enter the value of b: "))
            if b == 0:
                if self.count < 5:
                    self.count += 1
                    print("Error({}/5): Value of b cannot be 0".format(self.count))
                else:
                    print("Error limit exceeded")
                    break
            else:
                print("a/b: {}".format(a/b))        

class LoopingAgent(Agent):
    def __init__(self, aid):
        super().__init__(aid=aid)
        self.behaviours.append(LoopBehaviour(self))


if __name__ == '__main__':
    agents = []
    agent_name = 'agent_sum_{}@localhost:{}'.format(20000, 20000)
    agent_sum = LoopingAgent(AID(name=agent_name))
    agents.append(agent_sum)
    start_loop(agents)

