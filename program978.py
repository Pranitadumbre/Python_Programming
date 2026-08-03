class Demo:

    def __init__(self,A,B):
        print("Inside constructor")
        self.No1 = A
        self.No2 = B

    def Display(self):
        print("Inside Display")

def main():
    dobj1 = Demo(11,21)

    print(dobj1.No1)
    print(dobj1.No2)
    
    dobj1.Display()
    
main()
