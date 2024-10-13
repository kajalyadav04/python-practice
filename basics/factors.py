def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors
num = int(input("Enter a number: "))
result = find_factors(num)
print(f"The factors of {num} are: {result}")
