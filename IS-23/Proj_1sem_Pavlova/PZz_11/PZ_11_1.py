#Средствами языка Python формировать текстовый файл (.txt), содержащий последовательность из целых полож и отриц чисел.
#Сформировать новый текстовый файл следующего вида, предварительно выполнив требуемую обработку элементов:
#Исходные файлы:Количество элементов, положительные числа, кол-во полож чисел, отриц числа, кол-во отриц чисел.
l = [-9, -8,  -7,  -6,  -5,  -4,  -3,  -2,  -1,  0, 1,  2,  3,  4,  5,  6,  7,  8,  9]
f1 = open('file1.txt', 'w')
f1.writelines([str(i)+' ' for i in l])
f1.close()

f1 = open('file1.txt')
k = f1.read()
k = k.split()
count_num = len(k)
pol_num = []
for i in k:
    if int(i) > 0: #условие на выборку цифр
        pol_num.append(i)
count_num_pol = len(pol_num)

otriz_num = []
for i in k:
    if int(i) < 0: #условие на выборку цифр
        otriz_num.append(i)
count_num_otriz = len(otriz_num)
f1.close()

f2 = open('file2.txt', 'w', encoding='utf-8')
f2.writelines(f'''Исходные данные: {l}
Количество элементов: {count_num}
Положительные числа: {pol_num}
Количество положительных чисел: {count_num_pol}
Отрицательные числа: {otriz_num}
Количество отрицательных чисел: {count_num_otriz}''')
f2.close()
