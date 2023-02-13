from typing import Union, Optional, Any, Final, Callable

# Union - объединение нескольких типов в один тип (с версии 3.10 можно вместо Union[int, float] писать просто (x: int | float)
# Optional - позволяет указать только один какой-то тип данных и ещё автоматически добавляет значение NONE
# Any - любой тип данных
# Final - отметки констант в программе
# Callable - аннатация вызываемых объектов (например: если аргумент функция, она передается при вызове)


MAX_VALUE: Final = 1000  # пометить чтобы не присваивали константе новое значение по ходу кода


def mult2(x: int | float, y: Union[int, float] = 2) -> Union[int, float]:
    return x * y


str1 = Optional[str]  # это тоже самое, что и strType
strType = Union[str, None]


def show_x(x: Any, descr: Optional[str] = None) -> None:
    if descr:
        print(f"{descr} {x}")
    else:
        print(f"x = {x}")


res1 = mult2(5, 4)
print(res1)
print(mult2.__annotations__)

# ___________________________________________________________
# проверка (если интегрированная среда не отлавливает ошибки) в Терминале команда: mypy main.py (указать название файла)
list_1: list[int] = [1, 2, 3]  # с версии 3.9

book: tuple[str, str, int]  # прописывать тип данных для каждого элемента в кортеже
book = ("Подгорный О.Ю.", "Аннотация типов", 2022)
tuple_1: tuple[float, ...]  # все элементы кортежа должны быть float

# ____________________________________________________________
word: dict[str, int] = {"one": 1, "two": 2}

# ___________________________________________________________
personal: set[str] = {"sdfsdf", "sdfsd", " dgertert"}

# Callable[[.... , .....], тип который возвращается]
def get_digit(flt: Callable[[int], bool], lst: list[int] = None) -> list[int]:
    if lst is None:
        return []
    return list(filter(flt, lst))


print(get_digit(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def even(x: int):
    return bool(x % 2 == 0)
