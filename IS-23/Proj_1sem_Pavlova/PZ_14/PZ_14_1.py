# Из исходного текстового файла (price.txt) выбрать все цены. Посчитать количество
# полученных элементов.
import re

 a = open("price.txt", "r", encoding="UTF-8") #открытие файла на чтение
text = a.read()
price = re.findall(r'\d+\sруб\.\s\d+\sкоп\.', text)
s = list(set(price))
print(s)
print("Количество элементов", len(s))

a.close()
# Регулярное выражение \d+\sруб\.\s\d+\sкоп\. ищет любую цену в формате "XX руб.XX коп.