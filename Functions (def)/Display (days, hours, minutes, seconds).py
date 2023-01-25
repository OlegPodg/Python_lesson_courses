"""

Задача №4
написать функцию и сделать так, чтобы число секунд отображалось в виде - дни:часы:минут:секунды


"""


def sec_in_a_day(number):
    if number - 86400 >= 0:
        return number // 86400
    else:
        return 0


def sec_in_a_hour(number):
    return (number - (sec_in_a_day(number) * 86400)) // 3600


def sec_in_a_minute(number):
    return (number - (sec_in_a_day(number) * 86400) - (sec_in_a_hour(number) * 3600)) // 60


def sec(number):
    seconds = number - (sec_in_a_day(number) * 86400) - (sec_in_a_hour(number) * 3600) - (sec_in_a_minute(number) * 60)
    return seconds


second = int(input("Введите число секунд: "))

print(f"дни:часы:минуты:секунды\n"
      f"{sec_in_a_day(second)}:{sec_in_a_hour(second)}:{sec_in_a_minute(second)}:{sec(second)}")
