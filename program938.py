
# templete<class T>
# T Addition(T A, T B)

# Generic
def Addition(A,B):
    Result = 0
    Result = A + B
    return Result

def main():
    print(Addition(10,11))
    print(Addition(10.3,11.2))
    print(Addition("Hello","World"))
        
main()