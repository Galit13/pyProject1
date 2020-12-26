Type_of_threat = int(input("Enter 1,2,3,4 for a threat:"))
X = int(input("X rate:"))
Y = int(input("Y rate:"))

if Type_of_threat == 1:
    Time = 30
    print("the time you have is", Time, "seconds")
elif Type_of_threat == 2:
    Time = 60
    print("the time you have is", Time, "seconds")
elif Type_of_threat == 3:
    Time = 120
    print("the time you have is", Time, "seconds")
elif Type_of_threat == 4:
    print("false alarm")
else:
    print("wrong action")

if X < 0 or X > 20 or Y < 0 or Y > 20:
    print("Out of range")
elif (X > 10 and X < 20) and (Y > 10 and Y < 20):
    print("area 1")
elif (X > 10 and X < 20) and (Y > 0 and Y < 10):
    print("area 2")
elif (X > 0 and X < 10) and (Y > 10 and Y < 20):
    print("area 3")
elif (X > 0 and X < 10) and (Y > 0 and Y < 10):
    print("Open area")
else:
    print("Borderline")


import math

d = math.sqrt(X ** 2 + Y ** 2)

if X < 0 or X > 20 or Y < 0 or Y > 20 or Type_of_threat == 4:
    print("no need to be intercepted")
elif d > 13 or Type_of_threat == 3:
    print("Cannot be intercepted")
else:
    print("Can be intercepted")
