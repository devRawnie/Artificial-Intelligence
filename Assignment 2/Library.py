from Books import findbook
from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.acl.messages import ACLMessage

class Student(dict):
    def __init__(self, name, rollnumber):
        super().__init__(self, name=name, rollnumber=rollnumber)


class QueryAgent(Agent):
    def __init__(self, aid, receiver_agent, message):
        super().__init__(aid)
        self.receiver_agent = receiver_agent
        self.message = title


    def displayBook(self, books):
        for book in books:
            output = "Title: {}\nAuthor(s): {}\nDescription: {}".format(book["title"], ", ".join(book["authors"]), book["shortDescription"])
            print(output)

    def react(self, message):
        super().react(message)
        display_message(self.aid.localname, 'Message received from {}'.format(message.sender.name))
        if message.content is None:
            display_message(self.aid.localname, message.content)
        else:
            display_message(self.aid.localname, "Book found in the library.")
            self.displayBook(message.content)

    def on_start(self):
        super().on_start()
        display_message(self.aid.localname, ' Sending Query...')
        self.call_later(2.0, self.send_message)

    def send_message(self):
        message = ACLMessage(ACLMessage.QUERY_IF)
        message.set_protocol(ACLMessage.FIPA_QUERY_PROTOCOL)
        message.add_receiver(self.receiver_agent)
        self.add_all_agents(message.receivers)
        message.set_content(self.message)
        self.send(message)

    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver


class LibraryAgent(Agent):
    def __init__(self, aid):
        super().__init__(aid)

    def react(self, message):
        super().react(message)
        display_message(self.aid.localname, 'Query received from {} for book with title "{}"'.format(message.sender.name, message.content))
        book = findbook(message.content)
        self.send_message(message.sender.name, book)

    def send_message(self, receiver_agent, book):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(receiver_agent)
        self.add_all_agents(message.receivers)
        if book is None:
            message.set_content('Requested book is not available')
        else:
            message.set_content(book)
        self.send(message)

    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver


if __name__ == '__main__':
    agents = list()
    libraryAgentAID = AID(name='library_agent@localhost:{}'.format(30001))
    libraryAgent = LibraryAgent(libraryAgentAID)
    title = input("Enter the title of book you want to search in the library: ")
    queryAgent = QueryAgent(AID(name='query_agent@localhost:{}'.format(30000)), libraryAgentAID, message=title)
    agents.append(queryAgent)
    agents.append(libraryAgent)

    start_loop(agents)
