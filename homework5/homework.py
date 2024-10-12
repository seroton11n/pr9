numbers = []
user_input = input("введите числа через пробел: ").split()
for item in user_input:
    item = item.replace(',', '.')
    try:
        numbers.append(float(item))
    except ValueError:
        print(f"'{item}' не является числом и будет проигнорирован")
result = []
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        result.append(numbers[i])
print("элементы больше предыдущего:", result)
