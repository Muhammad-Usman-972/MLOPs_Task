def add(x,y):
    #For Addition
    return x+y
def sub(x,y):
    #For Subtraction
    return x-y
def mul(x,y):
    #For Multiplication
    return x*y
def div(x,y):
    #For Division
    try:
        return x/y
    except ZeroDivisionError:
        #Division Error Comment
        print("Division by zero is not allowed")
        return None

if __name__ == "__main__":
    #Input Statement comment
    print("Enter The two numbers for calculator app: ")
    x = int(input())
    y = int(input())
    #Operation Statements 

    print("Enter operation to be performed")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    choice = int(input())
    #Choice Selection
    if choice == 1:
        print(add(inp1,inp2))
    elif choice == 2:
        print(sub(inp1,inp2))
    elif choice == 3:
        print(mul(inp1,inp2))
    elif choice == 4:
        print(div(inp1,inp2))
    else:
        #Invalid Choice
        print("Invalid choice")