while 1:
    month = input("enter the month name:")
    month1 = month.lower()
    months =["january","february","march","april","may","june","july","august","september","october","november","december"]
    month31 = ["january", "march","may","july","august","october","december"]
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month1 in months:
        i = months.index(month1)
        print("no of days in ",month1,"is :",days[i])
    x = int(input("enter 1 to repeat the program and enter any other num to exit :"))
    if x==1:
        continue
    else:
        break



