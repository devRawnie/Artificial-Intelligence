from chat_agent import ChatAgent
from pade.acl.aid import AID
from pade.misc.utility import start_loop
import socket
from contextlib import closing

# def main():
#     agents = []
#     name = input("Enter name of User 1: ")
#     aid1 = AID(name='{}@localhost:{}'.format(name, 20000))
#     name = input("Enter name of User 2: ")
#     aid2 = AID(name='{}@localhost:{}'.format(name, 20001))

#     agents.append(ChatAgent(aid1, aid2, start=True))
#     agents.append(ChatAgent(aid2, aid1))
#     start_loop(agents)
# def get_port():
#     port = int(input("Enter port number for sender: "))
#     with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
#         if sock.connect_ex(("127.0.0.1", port)) == 0:
#             return port
#         else:
#             print("Error: Port- {} already in use".format(port))
#             return get_port()
def main():
    choice = int(input("Press 1 for Sender\nPress 2 for Receiver\n:-"))
    agents = []
    if choice == 1:
        name = input("Enter the sender's name: ")
        sender_port  = int(input("Enter port number for sender: "))
        aid = AID(name='{}@localhost:{}'.format(name, sender_port))
        receiver_name = input("Enter the receiver's name: ")
        receiver_port = int(input("Enter port number of receiver: "))
        receiver_aid = AID(name='{}@localhost:{}'.format(receiver_name, receiver_port))
        agents.append(ChatAgent(aid, receiver_aid))
    else:
        name = input("Enter the name of receiver: ")
        aid = AID(name='{}@localhost:{}'.format(name, 20001))
        agents.append(ChatAgent(aid))
        print("Waiting for messages!!")
    
    start_loop(agents)

if __name__ == '__main__':
    main()
    