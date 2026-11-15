print("hello world")

# # if expected expression
if True:  # თუ გაიშვება
    print("starting...")  # რა გაისჰვება
    print("hello world")
else:  # გაიშვება მხოლოდ მაშინ თუ if არ გაიშვა
    print("you are underage")


print("this is global")


# defalt is True = yes if False = no
# if შემდეგ იწერება მარტო bool (True, False, <, >,...)
# str და int შედარება არ შეგიძლია
# == და != შეგიძლია ნებისმიერ დროს("18" == 18)


number = int(input("Enter a number>"))
if number > 0:
    print("number is positive")
else:
    print("number is negative")
