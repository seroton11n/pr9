def get_numbers():
    numbers = []
    while True:
        user_input = input("введите число (или 'end' для завершения): ")
        if user_input.lower() == 'end':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("пожалуйста, введите корректное число.")
    return numbers

def get_odd_numbers(numbers):
    return [num for num in numbers if num.is_integer() and int(num) % 2 != 0]
if __name__ == "__main__":
    numbers = get_numbers()
    odd_numbers = get_odd_numbers(numbers)
    print("нечетные целые числа из списка:", odd_numbers)
