numbers = []
even= 0
odd= 0

while True:
    user_input = input("Введите число (или 'end' для завершения): ")

    if user_input == 'end':
        break
    try:
        number = float(user_input)
        numbers.append(number)
        if '.' in str(user_input):
            continue
        if number % 2 == 0:
            even+= 1
        else:
            odd+= 1

    except ValueError:
        print(f"'{user_input}' это не число, попробуйте снова.")

print(f"Четных чисел: {even}")
print(f"Нечетных чисел: {odd}")
print(f"Список чисел: {numbers}")
