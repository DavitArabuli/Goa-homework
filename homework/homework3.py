name = input("What is your name > ")
print("Hello " + name)


age = input("How old are you > ")
print("In five years you will be", int(age) + 5)


days_to_minuts = input("Enter the number of days: ")
print("The number of minutes is: ", int(days_to_minuts) * 24)


number1 = input("Enter the first number > ")
number2 = input("Enter the second number > ")
print(float(number1) + float(number2),
      float(number1) - float(number2),
      float(number1) * float(number2),
      float(number1) / float(number2))

integer1 = input("Enter the first integer > ")
integer2 = input("Enter the second integer > ")
integer3 = input("Enter the third integer > ")
print("The average is: ",
      (float(integer1) + float(integer2) + float(integer3)) / 3)
