import sys
import os

def DirctoryScanner(DirName = "Marvellous"):
    Border = "-"*50

    fobj = open("Marvellous.log","w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a Directory Cleaner Script\n")
    fobj.write(Border+"\n")
    
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return

    FileCount = 0
    EmptyFileCount = 0

    for FolderName, SubFolder, FileName in os.walk(DirName):

        for fname in FileName:
            FileCount = FileCount + 1

            fname = os.path.join(FolderName,fname)
            
            if(os.path.getsize(fname) == 0):    # Empty file
                EmptyFileCount = EmptyFileCount + 1
                os.remove(fname)

    fobj.write("Total files scnned : "+str(FileCount)+"\n")
    fobj.write("Total empty files found : "+str(EmptyFileCount)+"\n")
    fobj.write(Border+"\n")

    fobj.close()

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

    print(Border)
    print("-------- Marvellous Directory Automation ---------")
    print(Border)

if __name__ == "__main__":
    main()