 # the below python code is to take inputs from the user and reprint them in upper and lower case

while 1:
    name1 = input("enter your string:")
    name2 = name1.upper()
    name3 = name1.lower()
    print("your string in UPPER case is :",name2)
    print("your string in LOWER case is :",name3)
    x = int(input("enter 1 to repeat the program and any other number to exit :"))
    if x == 1:
       continue
    else:
        break