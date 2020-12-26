#circle.py – 3 תרגיל
X = int(input("Enter the X rate of the center point of the circle:"))
Y = int(input("Enter the Y rate of the center point of the circle:"))
R = int(input("Enter the radius length of the circle:"))
X1 = int(input("Enter the X rate of another point:"))
Y1 = int(input("Enter the Y rate of another point:"))
check = (R**2) > ((X-X1)**2+(Y-Y1)**2)
print("Is the point inside the circle?", str(check))