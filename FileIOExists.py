import os

def main():
    FileName = input("Enter the name of file : ")

    Ret = os.path.exists(FileName)

    if(Ret == True):
        fobj = open(FileName, "r")
        print("File gets succesfully opened")
    
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()