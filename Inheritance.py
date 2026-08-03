class Parent:
    def __init__(self):
        print("Inside Parent constructor")
        self.No1 = 10
        self.No2 = 20
    
    def fun(self):
        print("Inside fun method of parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside child constructor")
        self.A = 11
        self.B = 21

    def sun(self):
        print("Inside sun method of child")

cobj = Child()
