# DONE
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class SinglyLL:
    # DONE
    def __init__(self):
        self.first = None
        self.iCount = 0

    def InsertFirst(self,no):
        pass

    def InsertLast(self,no):
        pass
    
    def InsertAtPos(self,no, pos):
        pass

    def DeleteFirst(self):
        pass

    def DeleteLast(self):
        pass

    def DeleteAtPos(self, pos):
        pass
    
    def Display(self):
        pass
    
    # DONE
    def Count(self):
        return self.iCount
    
def main():
    sobj = SinglyLL()

if __name__ == "__main__":
    main()