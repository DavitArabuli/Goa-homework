# 1.
# and – ორივე პირობა უნდა იყოს სწორი, რომ შედეგი იყოს True.
# or – ერთ-ერთი პირობის შესრულებაც საკმარისია, რომ შედეგი იყოს True.
# not – პირობის მნიშვნელობას საპირისპიროდ აქცევს (True-ს False-ად, ხოლო False-ს True-ად).

# 2.
username = "admin"
password = "admin123"
login = input("Enter username> ")
login2 = input("Enter password> ")
if login == username and login2 == password:
    print("Login successful")
else:
    print("login failed")

# 3.
day1 = "saturday"
day2 = "sunday"
day_of_week = input("What day is it?> ")
if day_of_week == day1 or day_of_week == day2:
    print("It' the weekend!")
else:
    print("It's a workign day!")

# 4.
money = int(input("Enter the amount> "))
if money >= 100 and money < 500:
    print("You received a 10% discount!")
else:
    print("No discout available!")

# 5.
temperature = int(input("Enter temperature> "))
if temperature < 0 or temperature > 35:
    print("Extreme temperature")
else:
    print("Temperature is normal")

# 6.
number = int(input("Enter number> "))
num1 = number % 3
num2 = number % 5
if num1 == 0 and num2 == 0:
    print("Special number")
else:
    print("Regular number")

# 7.
# A. not True or False and not True
# B. True and not False or False
# C. not (True or False) and True
# D. False or True and not (False or False)
# E. not True and (False or True) or False

# Answers
# A. False
# B. True
# C. False
# D. True
# E. False
