# 1
name = input("What is your name > ")
last_name = input("What is your last name > ")
age = int(input("How old are you > "))
print(f"Hello my name is {name} {last_name}, and I am {age} years old")


# 2
bread = int(input("enter prise>"))
milk = int(input("enter prise>"))
apple = int(input("enter prise>"))
total = (bread + milk + apple)
print("total>"total)


# 3
age1 = int(input("How old are you > "))
years = int(input("How many years > "))
plus = (age1 + years)
print(F"in {years} years you will be {plus} years old")


# 4
walk = int(input("How many > "))
time = int(input("How many > "))
speed = (walk / time)
print("your speed> "speed)


# 5
distance = int(input("How far > "))
print = ("you will need> " (distance*8) / 100)


# 6
distance = int(input("How far > "))
fuel = int(input("Fuel consumption per 100 km > "))
price = int(input("Fuel price > "))

liters = (distance * fuel) / 100
cost = liters * price
print("Fuel used>", liters)
print("Total cost>", cost)


# 7
salary = int(input("Hourly salary > "))
hours = int(input("Hours worked per week > "))
total = salary * hours
print("Your weekly salary is> ", total)


# 8
money = int(input("Enter money > "))
people = int(input("Enter number of people > "))

each = money // people
left = money % people

print("Each person gets> ", each)
print("Money left> ", left)


# 9
price = int(input("Enter total price > "))
discount = int(input("Enter discount percentage > "))

discount_amount = (price * discount) / 100
final_price = price - discount_amount

print("Discount amount:", discount_amount)
print("Final price:", final_price)


# 10
pages = int(input("Enter number of pages > "))
daily = int(input("Pages per day > "))
days = pages / daily
print("You will need", days, "days")
