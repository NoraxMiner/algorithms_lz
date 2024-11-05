from random import randint
list = [randint(1, 1000000) for i in range(100)]
buble_list = list.copy()
simple_list = list.copy()


n = 100
count = 0
for i in range(n-1):
    count += 1
    for a in range(n-1-i):
        if buble_list[a] < buble_list[a+1]:
            buble_list[a], buble_list[a+1] = buble_list[a+1], buble_list[a]
    print(buble_list)
count1 = count



i = 0
count = 0
while i < n - 1:
    count += 1
    b = i
    j = i + 1
    while j < n: 
        if simple_list[j] > simple_list[b]: 
            b = j
        j += 1
    simple_list[i], simple_list[b] = simple_list[b], simple_list[i]
    i += 1
    print(simple_list)
count2 = count

print( "Первый список: " + str(buble_list))
print("Количество итераций в первом списке: " + str(count1))
print( "Второй список: " + str(simple_list))
print("Количество итераций во втором списке: " + str(count2))
