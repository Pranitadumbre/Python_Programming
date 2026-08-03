import hashlib

def CalculateChecksum(FileName):        # 4567
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)
    
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def main():
    
    Ret = CalculateChecksum("Demo.txt")

    print("Checksum is : ",Ret)

if __name__ == "__main__":
    main()