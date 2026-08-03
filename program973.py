# HeLlo -> hello
# HELLO -> hello
# hello -> hello

def LowerCase(Brr):
    Result = ""

    for ch in Brr:
        if(ch >= 'A' and ch <= 'Z'):
            Result = Result + chr(ord(ch) + 32)
        else:
            Result = Result + ch
            
    return Result

def main():
    print("Enter string : ")
    Arr = input() 

    Ret = LowerCase(Arr)

    print("Updated string is : ",Ret)

main()
