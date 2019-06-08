while 1:
    num = []
    e = 0
    o = 0
    i = 0
    j = 0
    even = []
    odd = []
    while 1:
        j += 1
        x = int(input("enter number"))
        num.append(x)
        y = int(input("enter 1 to enter the number again:"))
        if y == 1:
            continue
        else:
            break
    # from above a set of number list is taken
    for i in range(j):
        if num[i-1] % 2 == 0:
            e += 1
            even.append(num[i-1])
        else:
            o += 1
            odd.append(num[i-1])
    # from above all the entered even and odd numbers were sorted out
    total = e + o
    odd1 = odd.sort()
    even1 = even.sort()
    print("Total no.of numbers entered is", total)
    print("Total no of odd numbers is:", o)
    print("odd numbers list =", odd1)
    print("total no of even numbers :", e)
    print("even numbers list =", even)
    z = int(input("enter 1 to repaeat program,else enter other number:"))
    if z==1:
        continue
    else:
        break
