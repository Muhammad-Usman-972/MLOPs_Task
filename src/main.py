def add(x,y):
    #"For addition"
    return x+y
def sub(x,y):
    #"For subtraction"
    return x-y
def mul(x,y):
    #"For Multiplication"
    return x*y
def div(x,y):
    #"For Divison"
    try:
        return x/yS
    except ZeroDivisionError:
        #"Error Check"
        print("Division by zero is not allowed")
        return None

if __name__ == "_main_":
    
    print("Enter two numbers")
    inp1 = int(input())
    inp2 = int(input())
    print("Enter operation to be performed")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input())
    if choice == 1:
        print(add(inp1,inp2))
    elif choice == 2:
        print(sub(inp1,inp2))
    elif choice == 3:
        print(mul(inp1,inp2))
    elif choice == 4:
        print(div(inp1,inp2))
    else:
        print("Invalid choice")