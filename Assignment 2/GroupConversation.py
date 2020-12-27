from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.acl.messages import ACLMessage

primes = []

def SieveOfEratosthenes():
     
    n = 1000005
     
    prime = [True for i in range(n + 1)] 
     
    p = 2
    while (p * p <= n): 
           
        # If prime[p] is not changed, 
        # then it is a prime 
        if (prime[p] == True):                
            # Update all multiples of p 
            for i in range(p * p, n + 1, p): 
                prime[i] = False

        p += 1

    # Print all prime numbers 
    for p in range(2, n + 1): 
        if prime[p]: 
            primes.append(p)

AIDArray = [AID(name="Agent{}@localhost:{}".format(i, 30000+i)) for i in range(1,6)]


class FriendAgent(Agent):
    n = None
    def __init__(self, aid, recieverAgent, n=None):
        super().__init__(aid)
        self.recieverAgent = recieverAgent
        if n is not None:
            self.n = n
    
    def on_start(self):
        super().on_start()
        if self.n is not None:
            display_message(self.aid.localname, ' Sending Message...')
            n = self.n
            self.call_later(2.0, self.send_message)

    def react(self, message):
        super().react(message)
        display_message(self.aid.localname, 'Message received from {}'.format(message.sender.name))
        display_message(self.aid.localname, 'Message is: {}'.format(message.content["text"]))
        display_message(self.aid.localname, 'Response : {}th prime number is {}'.format(message.content["n"], primes[message.content["n"]]))
        self.n = message.content["n"]
        self.call_later(4.0, self.send_message)
    
    
    def send_message(self):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(self.recieverAgent)
        self.add_all_agents(message.receivers)
        nextn = self.n + 1
        text = "Give me the {}th prime number".format(nextn) 
        display_message(self.aid.localname, "Sending message to next agent\n")
        msg = {
            "n":nextn,
            "text": text
        }
        message.set_content(msg)
        self.send(message)

    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver


if __name__ == "__main__":
    SieveOfEratosthenes()
    agentlist = []
    n = int(input("Enter the value of n: "))
    
    for i in range(1,5):
        agentlist.append(FriendAgent(AIDArray[i], AIDArray[(i+1)%5]))
    
    agentlist.append(FriendAgent(AIDArray[0], AIDArray[1], n))
    
    start_loop(agentlist)
    