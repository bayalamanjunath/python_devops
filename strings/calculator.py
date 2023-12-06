import sys
def add(num1, num2):
    a = (num1 + num2)
    return a
def sub(num1, num2):
    a = (num1 - num2)
    return a
def multi(num1, num2):
    a = (num1 * num2)
    return a
def div(num1, num2):
    a = (num1 / num2)
    return a    
num1 = float(sys.argv[1])
operator = sys.argv[2]
num2 = float(sys.argv[3])

if operator == "add":
    output = add(num1, num2)
    print(output)
elif operator == "sub":
    output = sub(num1, num2)
    print(output)
elif operator == "multi":
    output = multi(num1, num2)
    print(output)
elif operator == "div":
    output = div(num1, num2)
    print(output)


