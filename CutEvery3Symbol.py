#Дана строка. Удалите из нее все символы, чьи индексы делятся на 3. 

k = str(input())
rezult = ''
for i in range (len(k)):
    if i%3 != 0:
        rezult += k[i]
print (rezult)