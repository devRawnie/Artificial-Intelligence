from pade.misc.utility import display_message
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
from json import dumps

class ChatAgent(Agent):
    receiver_agent=None
    def __init__(self, aid, receiver_agent=None):
        super().__init__(aid)
        if receiver_agent is not None:
            self.receiver_agent = receiver_agent
    
    def chat(self, receiver=None):
        display_message(self.aid.localname, ':- ', "red", newline=False)
        message = input()
        if message=="q" or message=="Q":
            return

        self.send_message(message, receiver)

    def react(self, message):
        super().react(message)
        display_message(message.sender.name, ': "{}"\n'.format(message.content))
        if self.receiver_agent is not None:
            self.chat()
        else:
            self.chat(AID(message.sender.name))

    def on_start(self):
        super().on_start()
        if self.receiver_agent is not None:
            print("\nWelcome bots, chat away!!!\n(Press q to Quit)\n")
            self.chat()
    
    def send_message(self, text, receiver=None):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        if self.receiver_agent is not None:
            message.add_receiver(self.receiver_agent)
        else:
            message.add_receiver(receiver)
        self.add_all_agents(message.receivers)
        message.set_content(text)        
        self.send(message)
        # if self.receiver_agent is not None:
        #     self.chat()

    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver