# print("hello world")
# print("Davit Arabuli")
from turtle import *
forward(200)
exitonclick()


my_age = int(input("what is you age> "))
my_birth_month = int(input("what is your birth month> "))
number = my_age + my_birth_month
print(number * 12)


age = int(input("what is you age> "))
if age < 18:
    print("you are a kid")
elif age >= 18:
    print("you are adult")


number4 = int(input("tell me the number> "))
if number4 == 90:
    print("A")
elif number4 == 70:
    print("B")
elif number4 == 50:
    print("C")
else:
    print("F")
