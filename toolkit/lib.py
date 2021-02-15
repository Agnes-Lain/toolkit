def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)



def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return (number * 3 + 1)
