# // — მთელ რიცხვზე გაყოფისას გვიჩვენებს შედეგის მთელ ნაწილს.
# მაგალითად: 10 // 3 = 3

# % — გვიჩვენებს გაყოფისას მიღებულ ნაშთს.
# მაგალითად: 10 % 3 = 1 (დამაშთვა)

number = int(input("enter a number > "))
print(number**2, number**3)


number1 = int(input("enter the first number > "))
number2 = int(input("enter athe second number > "))
print(float(number1) + float(number2),
      float(number1) - float(number2),
      float(number1) * float(number2),
      float(number1) / float(number2),
      float(number1) ** float(number2),
      float(number1) // float(number2),
      float(number1) % float(number2))


number_of_candy_taken = int(input("How much candy woud you like? > "))
print("The number of boxes that will fill is> ",
      (number_of_candy_taken // 12))
print("The number of candy left is> ",
      (number_of_candy_taken % 12))


minutes = int(input("enter the number of minuts> "))
print("The number of hours is> ", minutes // 60)
print("The number of minuts is> ", minutes % 60)
