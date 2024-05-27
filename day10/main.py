# Exercise 1 Leap year


def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return  False
    else:
      return True
  else: False


# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month -1]



#🚨 Do NOT change any of the code below 
year = int(input("Enter years: ")) # Enter a year
month = int(input("Enter a month")) # Enter a month
day = days_in_month(year, month)
print(day)



# Exercise 2 Calculator


from art import logo

def add(num1,num2):
    
    return num1 + num2

def subtract (num1, num2):
    return num1 - num2

def multiply (num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


operation = { "+" : add, "-" : subtract, "*" : multiply, "/" : divide}


def calculator():  
  print(logo)
  rerun = True    
  num1 = float(input("Enter number:"))


  while rerun:
    for value in operation:
      print(value)

    operation_symbol = input("Please selcet any one of the following operation from the given list above: ")


    num2 = float(input("Enter number :"))


    calculation_function = operation[operation_symbol]

    output1 = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} is {output1}")

    new_operation = input(f"Type y to continue with {output1} or type q to exit or type n to start new calculation: ")

    if new_operation == "y":
      num1 = output1
    else:
       rerun = False
       calculator()

calculator()