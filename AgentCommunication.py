from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.acl.messages import ACLMessage


class SenderAgent(Agent):
    def __init__(self, aid, receiver_agent):
        super().__init__(aid)
        self.receiver_agent = receiver_agent

    def react(self, message):
        super().react(message)
        display_message(self.aid.localname, 'Message received from {}'.format(message.sender.name))
        display_message(self.aid.localname, 'Message is {}'.format(message.content))

    def on_start(self):
        super().on_start()
        display_message(self.aid.localname, ' Sending Message...')
        self.call_later(3.0, self.send_message)

    def send_message(self):
        # print('Test')
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(self.receiver_agent)
        self.add_all_agents(message.receivers)
        message.set_content('Test Message')
        self.send(message)

    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver


class ReceiverAgent(Agent):
    def __init__(self, aid):
        super().__init__(aid)

    def react(self, message):
        super().react(message)
        display_message(self.aid.localname, 'Message received from {}'.format(message.sender.name))
        display_message(self.aid.localname, 'Message is {}'.format(message.content))
        self.send_message(AID(message.sender.name))

    def send_message(self, receiver_agent):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(receiver_agent)
        self.add_all_agents(message.receivers)
        message.set_content('I have received message successfully')
        self.send(message)

    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver


if __name__ == '__main__':
    agents = list()
    receiver_agent_aid = AID(name='receiver@localhost:{}'.format(30001))
    receiverAgent = ReceiverAgent(receiver_agent_aid)
    agents.append(receiverAgent)
    sender_agent = SenderAgent(AID(name='sender@localhost:{}'.format(30000)), receiver_agent_aid)
    agents.append(sender_agent)

    start_loop(agents)
