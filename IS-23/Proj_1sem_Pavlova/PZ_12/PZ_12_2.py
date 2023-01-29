def upper_case_generator(string):
    for char in string:
        yield char.upper()

my_string =input("Введите текст в нижнем регистре:")
for char in upper_case_generator(my_string):
    print(char, end=" ")
# сначала создается функция upper_case_generator(), которая принимает строку и использует итератор for для
# перебора каждого символа в строке. Для каждого символа используется генератор yield, чтобы преобразовать его в верхний
# регистр. Затем используется итератор for для печати каждого символа, который возвращается из генератора.





