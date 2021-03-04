from pade.misc.utility import display_message
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from json import dumps

class ChatAgent(Agent):
    def __init__(self, aid, receiver_agent, start=False):
        super().__init__(aid)
        self.receiver_agent = receiver_agent
        self.start = start

    def chat(self):
        display_message(self.aid.localname, ':- ', "red", newline=False)
        message = input()
        if message=="q" or message=="Q":
            return
        self.send_message(message)

    def react(self, message):
        super().react(message)
        display_message(message.sender.name, ': "{}"\n'.format(message.content))
        self.chat()

    def on_start(self):
        super().on_start()
        if self.start:
            print("\nWelcome bots, chat away!!!\n(Press q to Quit)\n")
            self.chat()
    
    def send_message(self, text):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(self.receiver_agent)
        self.add_all_agents(message.receivers)
        message.set_content(text)        
        self.send(message)

    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver