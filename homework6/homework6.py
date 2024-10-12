numbers = []
user_input = input("введите числа через пробел: ").split()
for item in user_input:
    item = item.replace(',', '.')
    try:
        numbers.append(float(item))
    except ValueError:
        print(f"'{item}' не является числом и будет проигнорирован.")
if len(numbers) > 1:
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))
    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
    print("список после замены мин и макс элементов:", numbers)
else:
    print("список должен содержать хотя бы два элемента.")
