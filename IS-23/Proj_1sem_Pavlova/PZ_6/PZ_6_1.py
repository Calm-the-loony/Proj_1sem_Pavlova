#Дан список A размера N. Вывести его элементы в следующем порядке: A1, A2, AN,AN-1, A3, A4, AN-2, … .
import random
n = random.randint(0,11)
k = int(n/4)
print("n =", n) # вывод рандомного размера списка
try: #обработчик исключений
    a =[i + 1 for i in range(n)] #проходит по всем элементам списка
    a1 = [] #
    for i in range(0, k): #
        a1.append(a[2*i])
        a1.append(a[2 * i + 1])
        a1.append(a[n -1 -2 * i])
        a1.append(a[n -2 -2 * i])
    for i in range(0, n - 4 * k):
        a1.append(a[2 * k + i])
    print(a1) #вывод конечного списка
except:
    print("Ошибка, проверьте правильность выполнения программы")
