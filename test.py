# This function will return the sum of two numbers
def add_numbers(a, b):
    result = a + b
    print(result)

coke = 2
burger = 4
myOrder = add_numbers(coke, burger)
print(myOrder)
myBill = myOrder * 1.1
print(myBill)

def subtract_numbers(a,b):
    return a - b

if __name__ == "__main__":
    print(subtract_numbers(4,1))