def SumDigits(No):
    
    Digit = 0
    iSum = 0

    while(No != 0):
        Digit = No % 10
        iSum = iSum + Digit
        No = No // 10

    return iSum

def main():
    No = 0

    print("Enter number : ")
    No = int(input())

    Ret = SumDigits(No)

    print("Summation of digits : ",Ret)
    
main()
