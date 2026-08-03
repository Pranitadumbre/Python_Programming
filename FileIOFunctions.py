import os

def main():
    FileName = input("Enter the name of file : ")   # Demo.txt

    if(os.path.exists(FileName)):
       fobj = open(FileName,"r")

       print(fobj.name) # Demo.txt
       print(fobj.mode) # R
       print(fobj.closed)   # False

       fobj.close()
       print(fobj.closed)   # True

        
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()