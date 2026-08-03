import os

def main():
    FileName = input("Enter the name of file : ")

    if(os.path.exists(FileName)):
        Ret = os.path.isabs(FileName)

        if(Ret == True):
            print("It is absolute path")
        else:
            print("It is relative path")
            NewPath = os.path.abspath(FileName)
            print("Updated path : ",NewPath)
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()