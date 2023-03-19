def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Kérem a pozitív egész számot: "))
print(num, "! =", factorial(num))
