#3 цветовода выращивают розы. Определить, какие из известных сортов роз "Анжелика", "Виктория", "Гагарин", "Катарина",
#"Юбилейная", "Южная" имеются у каждого цветовода, есть хотя бы у одного из цветоводов и каких нет ни у одного из цветоводов
try:
    d = {"Анжелика", "Виктория", "Гагарин", "Катарина", "Юбилейная", "Южная"} #общий список сортов роз

    a = {"Анжелика", "Виктория", "Гагарин", "Катарина"} #список сортов 1 цветовода и тд
    b = {"Гагарин", "Катарина", "Виктория"}
    c = {"Виктория", "Юбилейная", "Анжелика"}

    print("Есть у каждого цветовода:", a & b & c)
    print("Есть хотя бы у одного цветовода:", c - b - a)
    print("Ни у кого нет:", d - a - b - c )
except:
    print("Ошибка")
#"Юбилейная" есть только у 3 садовника, ни у кого нет "Южная" и у всех повторяется "Виктория"