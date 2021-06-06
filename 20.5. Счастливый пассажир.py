def test(a):
 
    b1 = a % 10# получаем элементы строки
    b2 = a % 100 / 10
    b3 = a % 1000 / 100
    S1 = b1 + b2 + b3
    b4 = a % 10000 / 1000
    b5 = a % 100000 / 10000
    b6 = a % 1000000 / 100000
    S2 = b4 + b5 + b6# суммируем 3 слева и справа
    if S1 == S2:# сравниваем
        result="Счастливый"
        return result# проверяем
        print(result)
    else:
        result="Не счастливый"
        return result
        print(result)
    if b1 == b6 and b2 == b5 and b3 == b4:
        print("Зеркальные числа")
    else:
        print("Не зеркальные числа")
 
if __name__ == '__main__':# точка входа 
    a = input("Номер:")# ввод строки
    test(a)# ф-ция