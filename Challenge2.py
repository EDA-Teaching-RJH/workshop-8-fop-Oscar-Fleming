import re
id = input("Input student id ")
if re.search(r"^[a-zA-Z]{4}\d{4}$", id):
    print ("valid id")
else:
    print("invalid id")