def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator(n1, n2, operation):
  return operation(n1, n2)

num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))

for operation in operations:
  print(operation)

operation_symbol = input("Pick an operation from the line above: ")

result = calculator(num1, num2, operations[operation_symbol])
print(f"{num1} {operation_symbol} {num2} = {result}")
