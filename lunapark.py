#lunapark.py – 4 תרגיל
First_name = input("Enter your first name:")
Last_name = input("Enter your last name:")
Height = int(input("Enter your height in cm:"))
Age = int(input("Enter your age:"))
check = ((Height <= 150) and (Height >= 120)) and ((Age >= 6) and (Age <= 12))
print("Can you get on the roller coaster?", str(check))