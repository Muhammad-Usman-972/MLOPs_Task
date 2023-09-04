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
        print("Division by zero is not allowed")
        return None

if __name__ == "__main__":
    #Input Statement comment
    print("Enter The two numbers for calculator app: ")
    x = int(input())
    y = int(input())
    #Operation Statements
    print("Enter operation to be performed")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input())
    #Choice Selection
    if choice == 1:
        print(add(x,y))
    elif choice == 2:
        print(sub(x,y))
    elif choice == 3:
        print(mul(x,y))
    elif choice == 4:
        print(div(x,y))
    else:
        #Invalid Choice
        print("Invalid choice")