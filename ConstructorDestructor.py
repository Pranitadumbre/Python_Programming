import gc

class Demo:
    def __init__(self):
        print("Inside constructor")

    def __del__(self):
        print("Inside Destructor")
    
# Allocate    
obj = Demo()

# Use

# Deallocate
del obj

gc.collect()

print("End of application")