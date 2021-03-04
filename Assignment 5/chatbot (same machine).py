from chat_agent import ChatAgent
from pade.acl.aid import AID
from pade.misc.utility import start_loop

# def main():
#     agents = []
#     name = input("Enter name of User 1: ")
#     aid1 = AID(name='{}@localhost:{}'.format(name, 20000))
#     name = input("Enter name of User 2: ")
#     aid2 = AID(name='{}@localhost:{}'.format(name, 20001))

#     agents.append(ChatAgent(aid1, aid2, start=True))
#     agents.append(ChatAgent(aid2, aid1))
#     start_loop(agents)

def main():
    choice = int(input("Press 1 for Sender\nPress 2 for Receiver\n:-"))
    agents = []
    if choice == 1:
        name = input("Enter the name of Sender: ")
        aid = AID(name='{}@localhost:{}'.format(name, 20000))
        receiver_name = input("Enter the name of Receiver: ")
        port = int(input("Enter the port number of Receiver: "))
        receiver_aid = AID(name='{}@localhost:{}'.format(receiver_name, port))
        agents.append(ChatAgent(aid, receiver_aid))
    else:
        name = input("Enter the name of Receiver: ")
        aid = AID(name='{}@localhost:{}'.format(name, 20001))
        agents.append(ChatAgent(aid))
        print("Waiting for messages!!")
    
    start_loop(agents)

if __name__ == '__main__':
    main()
    