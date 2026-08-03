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
    
    # DONE
    def Display(self):
        temp = self.first

        while(temp != None):
            print("| ",temp.data," |->",end=" ")
            temp = temp.next
        
        print("None")
    
    # DONE
    def Count(self):
        return self.iCount
    
def main():
    sobj = SinglyLL()

    sobj.InsertFirst(101)
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)
    
    print("Elements of LinkedList are : ")
    sobj.Display()

    print("Number of elements in LinkedList are : ",sobj.Count())
    
if __name__ == "__main__":
    main()