import sys
import os

def DirctoryScanner(DirName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return

    for FolderName, SubFolder, FileName in os.walk(DirName):
        for fname in FileName:
            print(fname)

def main():
    Border = "-"*50
    print(Border)
    print("-------- Marvellous Directory Automation ---------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number of arguments")
        print("Please specify the name of directory")
        return

    DirctoryScanner(sys.argv[1])

if __name__ == "__main__":
    main()