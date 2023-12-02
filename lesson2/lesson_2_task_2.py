def is_year_leap(year):
    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return True
    else:
        return False


def print_result(year):
    result = is_year_leap(year)
    print(f"Год {year}: {result}")


print_result(2000)
print_result(1700)
print_result(4)
