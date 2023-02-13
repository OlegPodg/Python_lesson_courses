def is_year_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year < 1582) or year % 400 == 0:
        return True
    else:
        return False


year_from_user = int(input("Введите год: "))
print(is_year_leap(year_from_user))
