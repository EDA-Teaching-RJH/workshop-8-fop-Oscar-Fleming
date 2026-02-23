import re
number = input("What's your phone number? ")
if re.search(r"^07\d{9}", number):
    print("Valid nuber")
else:
    print ("invalid number")