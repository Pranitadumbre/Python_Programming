class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

def main():
    head = None

    obj1 = Node(11)
    obj2 = Node(21)
    obj3 = Node(51)
    obj4 = Node(101)
    
    head = obj1
    obj1.next = obj2
    obj2.next = obj3
    obj3.next = obj4
    obj4.next = None

    print(head.data)
    print(head.next.data)
    print(head.next.next.data)
    print(head.next.next.next.data)

if __name__ == "__main__":
    main()