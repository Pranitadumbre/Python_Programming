class Arithematic:
    def Addition(self,A,B):
        return A+B

    def Substraction(self,A,B):
        return A-B

No1 = 0
No2 = 0
Ans = 0

No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))

Ans = Arithematic().Addition(No1,No2)
print("Addition is : ",Ans)

Ans = Arithematic().Substraction(No1,No2)
print("Substraction is : ",Ans)