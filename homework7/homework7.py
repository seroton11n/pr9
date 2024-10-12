numbers = []
user_input = input("Введите числа через пробел: ").split()
for item in user_input:
    item = item.replace(',', '.')
    try:
        numbers.append(float(item))
    except ValueError:
        print(f"'{item}' не является числом и будет проигнорирован.")
if numbers:
    last_element = numbers[-1]
    for i in range(len(numbers) - 1, 0, -1):
        numbers[i] = numbers[i - 1]
    numbers[0] = last_element
    print("Список после циклического сдвига вправо:", numbers)
else:
    print("Список пуст. Невозможно выполнить сдвиг.")
