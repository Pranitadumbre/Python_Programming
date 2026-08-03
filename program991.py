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

    # DONE
    def InsertFirst(self,no):
        newn = Node(no)

        # LL is empty
        if self.first == None:
            self.first = newn
        # It contains atleast 1 node
        else:
            newn.next = self.first
            self.first = newn
        
        self.iCount = self.iCount + 1

    # DONE
    def InsertLast(self,no):
        newn = Node(no)

        # LL is empty
        if self.first == None:
            self.first = newn
        # It contains atleast 1 node
        else:
            temp = self.first

            while(temp.next != None):
                temp = temp.next

            temp.next = newn
        
        self.iCount = self.iCount + 1

    #DONE
    def InsertAtPos(self,no, pos):
        # Invalid position filter
        if(pos < 1 or pos > (self.iCount+1)):
            print("Invalid position")
            return

        if(pos == 1):
            self.InsertFirst(no)
            return
        elif(pos == self.iCount+1):
            self.InsertLast(no)
            return
        else:
            newn = Node(no)
            temp = self.first

            for i in range(1,pos-1):
                temp = temp.next

            newn.next = temp.next
            temp.next = newn

            self.iCount = self.iCount + 1

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
    
    sobj.InsertLast(111)
    sobj.InsertLast(121)
    
    print("Elements of LinkedList are : ")
    sobj.Display()

    print("Number of elements in LinkedList are : ",sobj.Count())
    
    sobj.InsertAtPos(75,4)
    
    print("Elements of LinkedList are : ")
    sobj.Display()

    print("Number of elements in LinkedList are : ",sobj.Count())
    
if __name__ == "__main__":
    main()