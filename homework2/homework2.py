import math
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("ошибка: введите корректное число")
def get_squares_between(a, b):
    start = math.ceil(min(a, b))
    end = math.floor(max(a, b))
    if a == start:
        start += 1
    if b == end:
        end -= 1
    return [i**2 for i in range(start, end + 1) if start <= i <= end]
while True:
    a = get_float_input("введите число a: ")
    b = get_float_input("введите число b: ")
    squares = get_squares_between(a, b)
    if squares:
        print(f"квадраты целых чисел между {a} и {b}: {squares}")
    else:
        print(f"нет целых чисел между введенными a и b")
    continue_input = input("\nпродолжить выполение программы? (ответьте да или нет): ").strip().lower()
    if continue_input != "да":
        print("программа завершена.")
        break
