i = 0
ans = 0
try: #обработка исключений
    a = float(input())
    n = int(input())
    while i != n: #пока выполняется условие
        i += 1
        ans += a **i *(-1)**i
    print(ans + 1)  # вывод результата
except ValueError:
    print('Неверный формат') # вывод исключения
