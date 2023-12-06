number = input("enter the numbers: " )
ab = number.split()
a = int(ab[0])
b = int(ab[1])
print(a)
print(b)

def add():
  print(a + b)
def sub():
  print(a -b)
def mul():
  print(a * b)
def div():
  print(a / b)
print("add = " + str(int(a) + int(b) ) )
print("sub = " + str(int(a) - int(b) ) )
print("multiply = " + str(int(a) * int(b) ) )
print("div = " + str(int(a) / int(b) ) )

add()
sub()
mul()
div()