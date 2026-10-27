# 1.
# input გამოიყენება მომხმარებლისგან ინფორმაციის მისაღებად.
# მაგალითად:
# name = input("შეიყვანე შენი სახელი> ")

# 2.
# Type casting არის მონაცემის ერთი ტიპიდან
# მეორე ტიპში გადაყვანა. მაგალითად, str-ის int-ში გადაყვანა.
# age = int("16")

# 3.
# ნასწავლი მონაცემთა ტიპები:
# int - მთელი რიცხვი, მაგალითად: 10
# str - ტექსტი, მაგალითად: "Hello"
# float - ათწილადი რიცხვი, მაგალითად: 3.5
# bool - ლოგიკური მნიშვნელობა, მაგალითად: True ან False

# 4.
# შედარების ოპერატორები:
# == ამოწმებს, არის თუ არა ორი მნიშვნელობა ტოლი.
# != ამოწმებს, არის თუ არა ორი მნიშვნელობა განსხვავებული.
# > ამოწმებს, არის თუ არა მარცხენა მნიშვნელობა მარჯვენაზე მეტი.
# < ამოწმებს, არის თუ არა მარცხენა მნიშვნელობა მარჯვენაზე ნაკლები.
# >= ამოწმებს, არის თუ არა მარცხენა მნიშვნელობა მეტი ან ტოლი.
# <= ამოწმებს, არის თუ არა მარცხენა მნიშვნელობა ნაკლები ან ტოლი.

# 5.
number1 = int(input("Enter the first number > "))
number2 = int(input("Enter the second number > "))
print(float(number1) + float(number2),
      float(number1) - float(number2),
      float(number1) * float(number2),
      float(number1) / float(number2),
      float(number1) ** float(number2),
      float(number1) // float(number2),
      float(number1) == float(number2),
      float(number1) != float(number2),
      float(number1) > float(number2),
      float(number1) < float(number2),
      float(number1) >= float(number2),
      float(number1) <= float(number2))

# 6.
age = int(input("Enter your age > "))
if age > 18:
    print("You are an adult")
else:
    print("You are not an adult")

# 7.
car_speed = int(input("Enter the speed> "))
distance = int(input("Enter the distance> "))
time = int(input("Enter the time> "))
time_taken = (car_speed / distance)
print("You will make it. True of False>",
      bool(distance / car_speed < time))

# 8.
item1_price = int(input("Enter the price> "))
item2_price = int(input("Enter the price> "))
item3_price = int(input("Enter the price> "))
money = int(input("Enter the amout of money you have> "))
print("You have enough to buy them. True of False>",
      bool(item1_price + item2_price + item3_price < money))

# 9.
program_size = int(input("Enter the size> "))
storage = int(input("Enter the amount of storage you have> "))
print("You have enough storage to download it. True of False>",
      bool(program_size < storage))

# 10
math = float(input("Enter your grade"))
history = float(input("Enter your grade"))
art = float(input("Enter your grade"))
average_grade = ((math + history + art) / 3)
if average_grade >= 5:
    print("you have passed")
else:
    print("You have failed")

# 11.1
# num1 = input("Enter first number: ")
# num2 = int(input("Enter second number: "))

# result = num1 + num2
# print(result)

# you can not add an integer to a string and sence they forgot to add an "int" the input will returned the answer as an string as it always does.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 + num2
print(result)

# 11.2
# num1 = int(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# result = num1 - "5" * num2
# print(result)

# when calculating the resuit instead of - 5 they wrote - "5" wich is a spring

num1 = int(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = num1 - 5 * num2
print(result)

# 11.3
# hours = input("Enter hours worked: ")
# rate = float(input("Enter hourly rate: "))
# bonus = input("Enter bonus: ")

# salary = hours * rate
# total = salary + bonus
# final_salary = total / "2"

# print(final_salary)

# when calculating the final_salary instead of 2 they wrote "2" wich is a spring


hours = input("Enter hours worked: ")
rate = float(input("Enter hourly rate: "))
bonus = input("Enter bonus: ")

salary = hours * rate
total = salary + bonus
final_salary = total / 2

print(final_salary)

# 11.4
# price = float(input("Enter product price: "))
# quantity = input("Enter quantity: ")
# discount = float(input("Enter discount percentage: "))

# subtotal = price + quantity
# discount_amount = subtotal * discount
# final_price = subtotal - "10"

# print(int(final_price))

# when calculating the final_price instead of 10 they wrote "10" wich is a spring. also while printing the final_price they wote (int(finale_price)) which is wron and should be (finale_price)

price = float(input("Enter product price: "))
quantity = input("Enter quantity: ")
discount = float(input("Enter discount percentage: "))

subtotal = price + quantity
discount_amount = subtotal * discount
final_price = subtotal - 10

print(final_price)

# 11.5
# num1 = int(input("Enter first number: "))
# num2 = input("Enter second number: ")
# num3 = float(input("Enter third number: "))

# total = num1 + num2
# average = total / num3
# remainder = average % "2"
# result = int(remainder + num1)

# print(result)

# thwy forgot to write int in the second line, wrote "2" intead of 2 in the sixth line and in the last line wrote int which is wrong.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = float(input("Enter third number: "))

total = num1 + num2
average = total / num3
remainder = average % 2
result = (remainder + num1)

print(result)
