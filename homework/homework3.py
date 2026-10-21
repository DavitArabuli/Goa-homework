name = input("What is your name > ")
print("Hello " + name)


age = int(input("How old are you > "))
print("In five years you will be", age + 5)


days_to_minuts = int(input("Enter the number of days: "))
print("The number of minutes is: ", days_to_minuts * 24)


number1 = int(input("Enter the first number > "))
number2 = int(input("Enter the second number > "))
print(float(number1) + float(number2),
      float(number1) - float(number2),
      float(number1) * float(number2),
      float(number1) / float(number2))

integer1 = int(input("Enter the first integer > "))
integer2 = int(input("Enter the second integer > "))
integer3 = int(input("Enter the third integer > "))
print("The average is: ",
      (float(integer1) + float(integer2) + float(integer3)) / 3)
