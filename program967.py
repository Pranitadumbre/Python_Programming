def CountCapital(Brr):
    iCount = 0

    for i in range(len(Brr)):
        if(Brr[i] >= 'A' and Brr[i] <= 'Z'):
            iCount = iCount + 1

    return iCount

def main():
    print("Enter string : ")
    Arr = input() 

    Ret = CountCapital(Arr)

    print("Number of captial characters are : ",Ret)
    
main()
