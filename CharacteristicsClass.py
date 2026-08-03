import gc

class Demo:
    # Class variable
    No1 = 10
    No2 = 11

    def __init__(self):
        print("Inside constructor")

    def __del__(self):
        print("Inside Destructor")
    
print(Demo.No1)
print(Demo.No2)
