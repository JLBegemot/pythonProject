def bank(sum, term):
    for i in range(term):
        sum = sum * 1.1

    return sum


print(bank(10, 1))
print(bank(10, 2))
print(bank(10, 17))
