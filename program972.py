def CountCapital(Brr):
    iCount = 0

    for ch in Brr:
        if(ord(ch) >= 65 and ord(ch) <= 90):
            iCount = iCount + 1

    return iCount

def main():
    print("Enter string : ")
    Arr = input() 

    Ret = CountCapital(Arr)

    print("Number of captial characters are : ",Ret)
    
main()
