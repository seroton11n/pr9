import random
ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
def display_ticket():
    print("лотерейный билет:")
    for row in ticket:
        print(row)
user_numbers = []
for i in range(len(ticket)):
    while True:
        try:
            number = int(input(f"выберите число из строки {i + 1} {ticket[i]}: "))
            if number in ticket[i] and number not in user_numbers:
                user_numbers.append(number)
                break
            else:
                print("неправильный ввод,пожалуйста, выберите число из строки, которое вы еще не выбрали.")
        except ValueError:
            print("пожалуйста, введите целое число.")
lottery_numbers = [random.choice(row) for row in ticket]
print("\nваши выбранные числа:", user_numbers)
print("случайные числа лотереи:", lottery_numbers)

matches = set(user_numbers) & set(lottery_numbers)
print(f"кол-во совпадений: {len(matches)}")
if matches:
    print("совпадающие числа:"," ".join(map(str, matches)))
else:
    print("совпадающих чисел нет.")
