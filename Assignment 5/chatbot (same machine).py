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
    agents = []
    name = input("Enter name of User 1: ")
    aid1 = AID(name='{}@localhost:{}'.format(name, 20000))
    name = input("Enter name of User 2: ")
    aid2 = AID(name='{}@localhost:{}'.format(name, 20001))

    agents.append(ChatAgent(aid1, aid2, start=True))
    agents.append(ChatAgent(aid2, aid1))
    start_loop(agents)    
if __name__ == '__main__':
    main()
    