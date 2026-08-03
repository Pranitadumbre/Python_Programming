def Addition(A,B):
    Result = 0
    Result = A + B
    return Result

def main():
    No1 = 0
    No2 = 0
    Ans = 0

    print("Enter first number : ")
    No1 = int(input())

    print("Enter second number : ")
    No2 = int(input())

    Ans = Addition(No1,No2)

    print("Addition is : ",Ans)

main()      # OS / JVM