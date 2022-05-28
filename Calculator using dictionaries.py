from art import logo2

def add(n1,n2):
  return n1 + n2

def substract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2


operations = {
  "+" : add,
  "-" : substract,
  "*" : multiply,
  "/" : divide,}


def calculator():
    print(logo2)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
      print(symbol)

    should_continue = True
    while should_continue == True:

         operation_symbol = input("Pick an operation from the above?: ")
         num2 = float(input("What's the next number?: "))
         calculation_function = operations[operation_symbol]
         answer = calculation_function(num1, num2)

        #The calculation_function is either add, substract, multiply or divide
        #The calculation_function will call the functions above accordingly

         print(f"{num1} {operation_symbol} {num2} = {answer}")

         con = input(f"Press 'y' to continue with {answer} ,press 'n' to start new, press 'e' to exit")
         if con == "y":
           num1 = answer
         elif con == "e":
           should_continue = False
         elif con == "n":
           calculator()
         else:
           print("Invalid Input")

calculator()

#The calculator() works as a recursive functions which starts the calculations from num 1 for a fresh calculation




















