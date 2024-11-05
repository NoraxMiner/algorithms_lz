from random import randint

list = [] 
opr_lin = 1
iskomi_ind = 0
opr_lin2 = 0

for i in range (0, 100): 
    a = randint(1, 1_000_000) 
    list.append(a) 
list.sort() 



print('Список: ' + str(list))
print('Введите искомый элемент: ')
iskomi = int(input())





print('Линейный поиск:')
if iskomi in list:
    for i in range(len(list)):
        if list[i] == iskomi:
            break
        else:
            opr_lin += 1
            iskomi_ind += 1 
    print("Искомый элемент под индексом: " + str(iskomi_ind) + "\n Кол-во операций: " + str(opr_lin))
else:
    print("Данного элемента в этом списке нет")






print("Бинарный поиск:")

left = 0
right = len(list) - 1

while left <= right:
    center = (left + right) // 2
    if iskomi == list[center]:
        print("Номер искомого элемента: " + str(center) + "\n Количество операций: " +str(opr_lin2))
        break
    if iskomi > list[center]:
        left = center + 1
    else:
        right = center - 1
    opr_lin2 += 1
else:
    print('Нет такого значения')