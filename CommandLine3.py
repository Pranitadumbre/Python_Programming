# python3  CommandLine3.py  11  21  pune  89.90 

import sys

def main():
    print("Command line arguments are : ")

    for i in range(len(sys.argv)):
        print(sys.argv[i])
    
if __name__ == "__main__":
    main()