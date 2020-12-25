from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.behaviours.protocols import TimedBehaviour


class MyTimedBehaviour(TimedBehaviour):
    def __init__(self, agent, time):
        super().__init__(agent, time)

    def on_time(self):
        super().on_time()
        display_message(self.agent.aid.localname, 'Hello World!')


class TimedAgent(Agent):
    def __init__(self, aid):
        super().__init__(aid=aid)
        behaviour = MyTimedBehaviour(self, 60.0)
        self.behaviours.append(behaviour)


if __name__ == '__main__':
    agents = list()
    agent_name = 'agent_hello_{}@localhost:{}'.format(20000, 20000)
    timed_agent = TimedAgent(AID(name=agent_name))
    agents.append(timed_agent)
    start_loop(agents)