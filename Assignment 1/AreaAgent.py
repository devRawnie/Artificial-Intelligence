from pade.behaviours.protocols import Behaviour
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.misc.utility import start_loop
from math import pi, sqrt

class SquareBehaviour(Behaviour):
    def __init__(self, agent):
        super().__init__(agent)
        self.a = int(input("Enter the side of Square: "))

    def area(self):
        return self.a**2

    def on_start(self):
        super().on_start()
        print('Area is ', self.area())

class RectangleBehaviour(Behaviour):
    def __init__(self, agent):
        super().__init__(agent)
        self.side1 = int(input("Enter the length of Rectangle: "))
        self.side2 = int(input("Enter the breadth of Rectangle: "))

    def area(self):
        return self.side1*self.side2

    def on_start(self):
        super().on_start()
        print('Area of rectangle is: ', self.area())

class CircleBehaviour(Behaviour):
    def __init__(self, agent):
        super().__init__(agent)
        self.r = int(input("Enter the radius of Circle: "))

    def area(self):
        return round(pi*(self.r**2))

    def on_start(self):
        super().on_start()
        print('Area of circle is: ', self.area())

class TriangleBehaviour(Behaviour):
    def __init__(self, agent):
        super().__init__(agent)
        self.side1 = int(input("Enter side 1 of Triangle: "))
        self.side2 = int(input("Enter side 2 of Triangle: "))
        self.side3 = int(input("Enter side 3 of Triangle: "))
    
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        p2 = s*(s-self.side1)*(s-self.side2)*(s-self.side3)
        return round(sqrt(p2))

    def on_start(self):
        super().on_start()
        print('Area of Triangle is: ', self.area())


class AreaAgent(Agent):
    def __init__(self, aid):
        super().__init__(aid=aid)
        ch = int(input("1. Square\n2. Rectangle\n3. Circle\n4. Triangle\n:"))        
        if ch == 1:
            self.behaviours.append(SquareBehaviour(self))
        elif ch == 2:
            self.behaviours.append(RectangleBehaviour(self))
        elif ch == 3:
            self.behaviours.append(CircleBehaviour(self))
        elif ch == 4:
            self.behaviours.append(TriangleBehaviour(self))
        else: 
            print("Invalid choice")

if __name__ == '__main__':
    agents = list()
    agent_name = 'agent_sum_{}@localhost:{}'.format(20000, 20000)
    agent_sum = AreaAgent(AID(name=agent_name))
    agents.append(agent_sum)
    start_loop(agents)

