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
    
print(calculate(2,5,'*'))
print(calculate(2,5,'+'))


