#Дан список А размера N и целое число К (1 < K <4, K < N). Осуществить циклический сдвиг элементов спискка вправо на К позиций.
#(При этом А1 перейдет в Ак+1, А2- в Ак+2, Аn в Ак). Допускается использовать вспомогательный список из 4 элементов
try:
    import random
    K = random.randrange(2,4) #выбор сдвига 1<K<4
    N = random.randrange(K+1,12) #размер списка
    print("K = ", K)
    print("N = ", N)
    a = [i+1 for i in range(N)] #проход по всем элементам

    print("Первоначальный список:",a)
    b = []
    for i in range(N-K,N) :
        b.append(a[i])
    for i in range(N-1,K-1,-1) :
        a[i] = a[i-K]
    for i in range(0,K) :
        a[i] = b[i]
    print("Список со сдвигам вправо:", a)
except:
    print("Ошибка")