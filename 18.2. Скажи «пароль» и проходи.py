def ask_password():
    for i in range(0,3):
        s = input()
        if s == 'password':
            print("Пароль принят.")
            break
        else:
            print("В доступе отказано")


ask_password()
