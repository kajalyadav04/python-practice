num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 == num2 == num3:
    print("All numbers are equal")
elif num1 != num2 and num2 != num3 and num1 != num3:
    print("All numbers are different")
else:
    print("Neither all are equal nor different")