try:# обработчик исключений
    a = int(input())
    b = int(input())
    c = int(input())
    if (a == b and a != c and b != c) or (a != b and a == c and b != c) or (a != b and a != c and b == c): #при проверке условия выполняется одна из веток
        if a == b:
            print(3)
        elif a == c:
            print(2)
        elif b == c:
            print(1)
except:
    print("Ошибка")