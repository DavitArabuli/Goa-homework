# if ამოწმებს პირობას. თუ პირობა სწორია (True), სრულდება if-ის შიგნით დაწერილი კოდი.
# else სრულდება მაშინ, როდესაც if-ის პირობა არასწორია (False).


number = int(input("Enter number>"))
number2 = number % 2
if number2 > 0:
    print("Number is odd")
else:
    print("Number is even")


money = int(input("Enter the amount of money>"))
if money > 100:
    print("you have 10 precent discount")
else:
    print("No discount")


tempeture = int(input("Enter tempeture>"))
if tempeture > 25:
    print("It is hot outside")
else:
    print("It is not hot outside")

num1 = int(input("Enter first number>"))
num2 = int(input("Enter second number>"))
if num1 > num2:
    print(num1, "is bigger")
else:
    print(num2, "is bigger")
