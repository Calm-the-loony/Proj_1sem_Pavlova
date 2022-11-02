a = int(input())
b = int(input())
k = int(input())
try: #обработка исключений
    while a > b : #выполнение цикла
        a = a - b
        k = k + 1
    print(k)
except:
    print("Неверный формат")
