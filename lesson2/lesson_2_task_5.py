def month_to_season(month_num):
    if (month_num in range(1, 2) or month_num == 12): return "Зима"
    if (month_num >= 3 and month_num <= 5): return "Весна"
    if (month_num >= 6 and month_num <= 8): return "Лето"
    if (month_num >= 9 and month_num <= 11): return "Осень"


print(month_to_season(12))
print(month_to_season(1))
print(month_to_season(3))
print(month_to_season(5))
print(month_to_season(6))
print(month_to_season(8))
print(month_to_season(9))
print(month_to_season(11))
