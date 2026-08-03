Addition = lambda A,B : A+B

Substraction = lambda A,B : A-B

No1 = 0
No2 = 0
Ans = 0

No1 = int(input("Enter first number : "))       # 11
No2 = int(input("Enter second number : "))      # 10

Ans = Addition(No1,No2)         # Ans = No1+No2     -> Ans = 11+10
print("Addition is : ",Ans)     

Ans = Substraction(No1,No2)     # Ans = No1-No2     -> Ans = 11-10
print("Substraction is : ",Ans)