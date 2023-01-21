#Из предложенного текстового файла (text18-16.txt) вывести на экран его содержимое,
#количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно заменив все знаки пунктуации на знак «!».'''

file = open(file='18-16.txt', mode='r', encoding='utf-8')
text = file.read()
file.close()
count_capitalize = 0
for i in text:
    if i.isupper():
        count_capitalize += 1
print(text, f'\n\nКоличество букв в верхнем регистре: {count_capitalize}')
sim = ',—:…' #знаки, имеющиеся в тексте
for i in sim:
    text = text.replace(i, "!") #замена знаков

file1 = open(file='text.txt', mode='w', encoding='utf-8')
file1.writelines(text)
file1.close()
#исправленный текст выводится в text.txt, а кол-во букв в регистре в консоль