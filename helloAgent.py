from pade.core.agent import Agent
from pade.misc.utility import display_message, start_loop
from pade.acl.aid import AID


class HelloAgent(Agent):
    def __init__(self, aid):
        super().__init__(aid=aid)
        display_message(self.aid.localname, 'Hello, Agent!!')

# ! pip install pade


if __name__ == '__main__':
    agents_per_process = 5
    c = 10
    agents = list()
    port = 20000
    for i in range(agents_per_process):
        port = port + c
        agent_name = 'hello_agent_{}@localhost:{}'.format(port, port)
        hello_agent = HelloAgent(AID(name=agent_name))
        agents.append(hello_agent)

    start_loop(agents)
