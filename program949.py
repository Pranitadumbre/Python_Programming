def CheckPerfect(No):
    
    iSum = 0

    for i in range(1, int((No/2)+1)):
        if(No % i == 0):
            iSum = iSum + i

    return (iSum == No)

def main():
    Value = 0

    print("Enter number : ")
    Value = int(input())

    Ret = CheckPerfect(Value)
    
    if(Ret == True):
        print("It is perfect number")
    else:
        print("It is not a perfect number")

main()
