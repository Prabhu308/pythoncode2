def add(a, b):
 
    return a + b

def multiply(a, b):
   
    return a * b

if __name__ == "__main__":
    # Simple CLI interaction
    print("Simple Calculator")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} * {y} = {multiply(x, y)}")

