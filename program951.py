
def DisplayDigits(No):
    Digit = 0
    while(No != 0):
        Digit = No % 10
        print(Digit)
        No = No // 10

def main():
    No = 0

    print("Enter number : ")
    No = int(input())

    DisplayDigits(No)

main()
