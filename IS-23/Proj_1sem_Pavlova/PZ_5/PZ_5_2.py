#Описать функцию Power1(А,В) вещественного типа, находящую величину АВ по формуле АВ = exp(B*ln(A)) (параметры А и В - вещественные). В случае нулевого или отрицательного параметра А функция возвращает 0
import math

def Powerl(A, B):
    if A <= 0:    # Если A меньше 1, то функция возвращает  0.
        return 0
    AB = math.exp(B*math.log(A))    # Возведение в степень.
    return round(AB, 5)   # Возвращение округлённого значения AB до 5 знаков после запятой.

try:                                # обработчик исключений.
    num_A = float(input("Введите вещ число"))    # Ввод данных вещественного типа
    num_B = float(input("Введите вещ число"))
    num_C = float(input("Введите вещ число"))
    num_P = float(input("Введите вещ число"))
    print(Powerl(num_A, num_P))   # Вывод полученного значения
    print(Powerl(num_B, num_P))
    print(Powerl(num_C, num_P))
except Exception:
    print("Введите число вещественного типа")