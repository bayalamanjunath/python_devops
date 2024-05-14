#calculator
#addition
def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def multi(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : multi,
    "/" : div,
}
for operation in operations:
    print(operation)
n1 = int(input("enterthe number1:  "))
n2 = int(input("enterthe number2:  "))
operator = input("enter the operator:  ")
cal_operations = operations[operator]
answer = cal_operations(n1,n2)
print(f"{n1} {operator} {n2} = {answer}")