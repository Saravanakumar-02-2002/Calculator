def calculate(a,b,operation):
    if operation == '+':
        return a+b
    elif operation == '-':
        return a-b
    elif operation == '*':
        return a*b
    elif operation == '%':
        return a%b
    elif operation == '/':
        return a/b
    elif operation == '//':
        return a//b
    else:
        return "Not a valid operator"
    
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operation = input("Enter the operation you want to perform (+,-,*,%,//,/): ")
print(calculate(a,b,operation))


