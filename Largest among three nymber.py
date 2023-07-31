num1 = int(input("Enter a num1: "))
num2 = int(input("Enter a num2: "))
num3 = int(input("Enter a num3: "))

if (num1 > num2) and (num1 > num3):
    print(num1, "is greater then", num2, num3)
elif (num2 > num1) and (num2 > num3):
    print(num2, " is greater then ", num1, num3)
else:
    print(num3, "is greater then", num1, num2)