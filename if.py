import math

x = int(input("Enter 1,2,3,4,5,6 for an action:"))

if x <= 5 and x >= 1:
    n1 = int(input("Enter the first number:"))
    n2 = int(input("Enter the first number:"))
    if x == 1:
       print(n1 + n2)
    elif x == 2:
       print(n1 - n2)
    elif x == 3:
       print(n1 * n2)
    elif x == 4:
       if  n2 != 0:
          print(n1 / n2)
       else:
          print("error")
    elif x == 5:
       print(n1 ** n2)
elif x == 6:
    n = int(input("Enter the number:"))
    if n >= 0:
        print(math.sqrt(n))
    else:
        print("error")
else:
    print("wrong action")