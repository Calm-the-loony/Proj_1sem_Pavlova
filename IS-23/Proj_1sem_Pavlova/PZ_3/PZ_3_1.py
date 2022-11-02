try: # обработчик исключений
    a = int(input())
    b = int(input())
    c = int(input())

    if (a > 0 and b > 0 and c < 0) or (a < 0 and b > 0  and c > 0) or (a > 0 and b < 0  and c > 0): #если выполняется условие,то то ветка else пропускается
        print("Ровно 2 из них положительны")
    else:
        print("Нет")
except:
    print("Ошибка")