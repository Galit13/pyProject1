# תרגיל 3 - מיסתורי
DIGITS = 5
message = "Enter a number with" + str(DIGITS) + "digits: "
number = int(input(message))
print(number % 10)
number //= 10
print(number % 10)
number //= 10
print(number % 10)
number //= 10
print(number % 10)
number //= 10
print(number)
# התוכנית מפרקת את המספר לספרותיו וכותבת אותו מהסוף להתחלה