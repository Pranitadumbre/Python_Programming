def CheckEven(No):
    if(No % 2 == 0):
        print("It is Even number")
    else:
        print("It is Odd number")

def main():
    Value = 0

    print("Enter number : ")
    Value = int(input())

    CheckEven(Value)
    
main()
