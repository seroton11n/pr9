import re
while True:
    email = input("введите ваш email: ")
    pattern = r"^[^\d][a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    matched = re.search(pattern, email)
    if matched:
        try:
            at_index = email.index("@")
            username = email[:at_index]
            domain = email[at_index + 1:]
            print(f"имя пользователя: {username}")
            print(f"домен имя почты: {domain}")
            break
        except ValueError:
            print("ошибка: символ '@' не найден.")
    else:
        print("ошибка: введите корректный email, который не начинается с цифры или содержит хотя бы одну точку в домене.")
