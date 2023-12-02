def fizz_buzz(num):
    if (num % 5 == 0 and num % 3 == 0):
        return "FizzBuzz"
    elif (num % 5 == 0):
        return "Fizz"
    elif (num % 3 == 0):
        return "Buzz"


print(fizz_buzz(15))
print(fizz_buzz(9))
print(fizz_buzz(25))
print(fizz_buzz(32))
