from chat_agent import ChatAgent
from pade.acl.aid import AID
from pade.misc.utility import start_loop
import sys

def main(different=False):
    agents = []
    name = input("Enter the sender's name: ")
    sender_port  = int(input("Enter port number for sender: "))
    aid = AID(name='{}@localhost:{}'.format(name, sender_port))

    receiver_name = input("Enter the receiver's name: ")
    receiver_port = int(input("Enter port number of receiver: "))
    host = "localhost"
    if different:
        host = input("Enter the host address of receiver: ")
    
    receiver_aid = AID(name='{}@{}:{}'.format(receiver_name, host, receiver_port))

    agents.append(ChatAgent(aid, receiver_aid))    
    start_loop(agents)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 2 and ("-d" in sys.argv or "--diff" in sys.argv):
        main(different=True)
    